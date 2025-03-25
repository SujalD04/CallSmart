import speech_recognition as sr
import joblib
import re
import string

# Load your model and vectorizer
model = joblib.load("fraud_detection_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

def clean_text(text):
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def Ques(input_text):
    cleaned_text = clean_text(input_text)
    input_vectorized = vectorizer.transform([cleaned_text])
    prediction = model.predict(input_vectorized)
    return "❌ Potential Fraudulent Conversation Detected!" if prediction[0] == 1 else "✅ No Fraud Detected"

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"📝 Recognized Text: {text}")
        return text
    except sr.UnknownValueError:
        return "Could not understand the audio"
    except sr.RequestError:
        return "Error with speech recognition service"

# Main execution
if __name__ == "__main__":
    voice_input = get_voice_input()
    if voice_input not in ["Could not understand the audio", "Error with speech recognition service"]:
        result = Ques(voice_input)
        print(result)
