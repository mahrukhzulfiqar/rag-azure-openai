from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    azure_openai_endpoint: str
    azure_openai_key: str
    azure_openai_chat_deployment: str
    azure_openai_embedding_deployment: str

    class Config:
        env_file = ".env"


settings = Settings()
