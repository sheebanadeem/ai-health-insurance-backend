from dotenv import load_dotenv
load_dotenv()

import os
from pydantic_ai.models.openai import OpenAIModel

# Groq uses OpenAI-compatible API
# pydantic-ai reads these from env vars
os.environ["OPENAI_API_KEY"] = os.getenv("GROQ_API_KEY", "")
os.environ["OPENAI_BASE_URL"] = "https://api.groq.com/openai/v1"

if not os.environ["OPENAI_API_KEY"]:
    raise RuntimeError("GROQ_API_KEY is not set")

model = OpenAIModel(
    model_name="llama3-70b-8192"
)
