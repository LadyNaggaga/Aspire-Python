from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from typing import Optional
import json
import httpx
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import AzureChatOpenAI
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

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

# Initialize conversation memory
memory = ConversationBufferMemory()

# Initialize the language model and chain based on environment
if ENVIRONMENT == "production":
    # Azure OpenAI Configuration
    openai.api_type = "azure"
    openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
    openai.api_version = "2024-02-15-preview"
    openai.api_key = os.getenv("AZURE_OPENAI_KEY")
    AZURE_DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME")
    
    llm = AzureChatOpenAI(
        deployment_name=AZURE_DEPLOYMENT_NAME,
        openai_api_version="2024-02-15-preview",
        temperature=0.7
    )
else:
    llm = Ollama(model="mistral")

# Create the conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

class Message(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    error: Optional[str] = None

@app.post("/chat")
async def chat(message: Message) -> ChatResponse:
    try:
        # Use LangChain's conversation chain to get response
        response = conversation.predict(input=message.message)
        return ChatResponse(response=response)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "environment": ENVIRONMENT}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)