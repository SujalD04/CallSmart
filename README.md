# CallSmart - AI-Based Call Handler

CallSmart is an AI-powered call management system that intelligently handles incoming calls, detects fraudulent calls, and takes appropriate actions against potential threats. It provides smart responses to calls and ensures users' security by identifying scams and suspicious activities.

---

## 🚀 Features
- **AI-Powered Call Handling** - Responds intelligently to incoming calls.
- **Fraud & Scam Detection** - Identifies and warns about potential scam calls.
- **Call Management** - Logs, records, and categorizes incoming calls.
- **Seamless Integration** - Built with Node.js, Express, TypeScript, and MongoDB.
- **Modular Design** - Separate frontend and backend for scalability.

---

## 🛠️ Project Setup
This project consists of **two main parts**:
1. **Frontend** (React-based UI)
2. **Backend** (Node.js with Express and MongoDB)

Ensure you have **Node.js** and **MongoDB** installed on your system before proceeding.

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/CallSmart.git
cd CallSmart
```

### **2️⃣ Backend Setup**
Navigate to the `backend` folder and install dependencies.

```sh
cd backend
npm install
```

#### **Required Dependencies**
Install the necessary TypeScript-related dependencies:
```sh
npm install typescript ts-node @types/node @types/express @types/mongoose
```

Install required backend dependencies:
```sh
npm install express mongoose cors dotenv
```

#### **Environment Variables**
Create a `.env` file inside the `backend` directory and configure your MongoDB connection:
```
PORT=5000
MONGO_URI=your_mongodb_connection_string
```

### **3️⃣ Running the Backend Server**
Start the backend server using **TypeScript**:
```sh
npx ts-node src/server.ts
```
The server will be running on **http://localhost:5000**.

---

### **4️⃣ Frontend Setup**
Navigate to the `frontend` folder and install dependencies.
```sh
cd ../frontend
npm install
```
Run the frontend application:
```sh
npm start
```
The frontend will be running on **http://localhost:3000**.

---

## 📌 Development Workflow
To maintain a clean and structured development process, follow these steps:

1. **Do NOT commit directly to `main`**.
2. Always create a new branch for each specific task:
   ```sh
   git checkout -b feature-task-name
   ```
3. Work on your branch, make commits, and push changes:
   ```sh
   git add .
   git commit -m "Added feature X"
   git push origin feature-task-name
   ```
4. Before merging, discuss the changes with the team.
5. Open a pull request (PR) and get approval before merging to `main`.

---

## 📜 License
This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

---

## 🔍 Insights on the Call Handler Project
CallSmart is designed to **enhance user security and call management efficiency** by integrating:
- **Machine Learning for Fraud Detection** (future enhancement)
- **Real-Time Call Analysis and Logging**
- **Intelligent Automated Responses** to manage spam calls
- **Scalability for Future Enhancements** (e.g., API integrations, VoIP support)

This project is still in development, and contributions from the team are essential to refining its features. Feel free to propose improvements or report issues.

---

### 💡 Need Help?
For any queries, contact the team before proceeding with major changes.

Happy coding! 🚀

