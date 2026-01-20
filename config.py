import os
from pydantic_ai.models.openai import OpenAIModel

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

model = OpenAIModel(
    model_name="llama3-70b-8192",
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
)
