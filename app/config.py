import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    AZURE_OPENAI_ENDPOINT: str = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_KEY: str = os.getenv("AZURE_OPENAI_KEY")
    AZURE_OPENAI_CHAT_DEPLOYMENT: str = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")
    AZURE_OPENAI_EMBEDDING_DEPLOYMENT: str = os.getenv(
        "AZURE_OPENAI_EMBEDDING_DEPLOYMENT"
    )


settings = Settings()
