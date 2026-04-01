from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Secure API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class Request(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "AI Chatbot API is running"}

@app.post("/chat")
def chat(request: Request):
    try:
        if not request.query:
            return {"error": "Query cannot be empty"}

        messages = [
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": request.query}
        ]

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            max_tokens=200
        )

        reply = response.choices[0].message.content

        return {"status": "success","response": reply}

    except Exception as e:
        return {"error": "Something went wrong. Please try again."}