from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from typing import Optional
import json
import httpx

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Environment configuration
ENVIRONMENT = os.getenv("ENVIRONMENT", "local")  # 'local' or 'production'

if ENVIRONMENT == "production":
    # Azure OpenAI Configuration
    openai.api_type = "azure"
    openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
    openai.api_version = "2024-02-15-preview"
    openai.api_key = os.getenv("AZURE_OPENAI_KEY")
    AZURE_DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME")

class Message(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    error: Optional[str] = None

async def get_ollama_response(message: str) -> str:
    """Get response from local Ollama instance"""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",  # or any other model you've pulled
                "prompt": message,
                "stream": False
            }
        )
        if response.status_code == 200:
            return response.json()["response"]
        else:
            raise Exception("Failed to get response from Ollama")

async def get_azure_response(message: str) -> str:
    """Get response from Azure OpenAI"""
    response = await openai.ChatCompletion.create(
        engine=AZURE_DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ],
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].message.content

@app.post("/chat")
async def chat(message: Message) -> ChatResponse:
    try:
        if ENVIRONMENT == "local":
            response_text = await get_ollama_response(message.message)
        else:
            response_text = await get_azure_response(message.message)
            
        return ChatResponse(response=response_text)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "environment": ENVIRONMENT}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)