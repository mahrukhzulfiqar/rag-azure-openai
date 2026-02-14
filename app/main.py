from fastapi import FastAPI
from app.services.azure_openai_service import AzureOpenAIService

app = FastAPI()

# Initialize service
azure_service = AzureOpenAIService()


@app.get("/")
def read_root():
    return {"message": "RAG Azure OpenAI is running 🚀"}


@app.post("/chat")
def chat_with_model(message: str):
    """
    Simple chat endpoint that sends a message
    to Azure OpenAI and returns the response.
    """
    response = azure_service.chat(message)
    return {"response": response}
