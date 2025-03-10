import express from "express";
import dotenv from "dotenv";
import cors from "cors";
import connectDB from "./config/db";

dotenv.config();
const app = express();
const PORT = process.env.PORT || 5000; // Default to 5000 if PORT is not set in .env, when running locally

//Middleware
app.use(cors());
app.use(express.json());


// Connect to DB and then start the server
connectDB().then(() => {
  console.log("✅ MongoDB connected, starting server...");
  app.listen(PORT, () => console.log(`🚀 Server running on port ${PORT}`));
}).catch((err) => {
  console.error("❌ Failed to connect to MongoDB:", err);
  process.exit(1);
});