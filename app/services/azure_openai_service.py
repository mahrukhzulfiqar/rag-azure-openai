from openai import AzureOpenAI
from app.config import settings


class AzureOpenAIService:
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=settings.azure_openai_key,
            api_version="2024-02-01",
            azure_endpoint=settings.azure_openai_endpoint,
        )

        self.chat_deployment = settings.azure_openai_chat_deployment
        self.embedding_deployment = settings.azure_openai_embedding_deployment

    def chat(self, message: str) -> str:
        response = self.client.chat.completions.create(
            model=self.chat_deployment,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message},
            ],
        )

        return response.choices[0].message.content

    def embed(self, text: str) -> list[float]:
        response = self.client.embeddings.create(
            model=self.embedding_deployment,
            input=text,
        )

        return response.data[0].embedding
