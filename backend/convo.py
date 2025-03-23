import torch
from transformers import AutoTokenizer, DistilBertForSequenceClassification, AutoModelForCausalLM

fraud_model_path = "fine_tuned_fraud_model"
fraud_tokenizer = AutoTokenizer.from_pretrained(fraud_model_path)
fraud_model = DistilBertForSequenceClassification.from_pretrained(fraud_model_path)

response_model_path = "microsoft/DialoGPT-small"
response_tokenizer = AutoTokenizer.from_pretrained(response_model_path)
response_model = AutoModelForCausalLM.from_pretrained(response_model_path)

def detect_fraud(text):
    inputs = fraud_tokenizer(text, padding="max_length", truncation=True, return_tensors="pt")
    with torch.no_grad():
        outputs = fraud_model(**inputs)
    logits = outputs.logits
    prediction = torch.argmax(logits, dim=1).item()
    return prediction 

def generate_response(user_input):
    inputs = response_tokenizer.encode(user_input + response_tokenizer.eos_token, return_tensors="pt")
    response_ids = response_model.generate(inputs, max_length=100, pad_token_id=response_tokenizer.eos_token_id)
    response = response_tokenizer.decode(response_ids[:, inputs.shape[-1]:][0], skip_special_tokens=True)
    return response

def chatbot_conversation(user_message):
    is_fraud = detect_fraud(user_message)
    
    if is_fraud == 1:
        return "⚠️ Warning: This conversation might be fraudulent. Call terminated."
    else:
        return generate_response(user_message)

ques=input("Enter the conversation:")
sample_text = ques
response = chatbot_conversation(sample_text)
print(f"Bot: {response}")
