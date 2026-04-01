# 🤖 AI Chatbot API (FastAPI + Groq)

## 🚀 Overview
This project is a backend API built using FastAPI that integrates with a Large Language Model (Groq) to generate chatbot responses.

## 🛠️ Tech Stack
- Python
- FastAPI
- Groq API (LLM)
- HTML (Frontend)
- Uvicorn

## ⚙️ Features
- REST API for chatbot interaction
- Secure API key using environment variables
- Error handling and input validation
- Interactive Swagger UI
- Simple frontend interface

## ▶️ Run Locally
```bash
pip install fastapi uvicorn groq python-dotenv
uvicorn main:app --reload


📌 API Endpoint

POST /chat

{
  "query": "What is AI?"
}
📷 Demo

Open: http://127.0.0.1:8000/docs

👨‍💻 Author

Aruni Shajith
