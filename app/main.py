from fastapi import FastAPI
from openai import AzureOpenAI

from app.config import settings

app = FastAPI()

client = AzureOpenAI(
    api_key=settings.AZURE_OPENAI_KEY,
    api_version="2024-02-01",
    azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
)

deployment_name = settings.AZURE_OPENAI_CHAT_DEPLOYMENT


@app.get("/")
def read_root():
    return {"message": "RAG Azure OpenAI is running 🚀"}


@app.post("/chat")
def chat_with_model(message: str):
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ],
    )

    return {"response": response.choices[0].message.content}
