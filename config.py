from dotenv import load_dotenv
load_dotenv()

import os
from pydantic_ai.models.openai import OpenAIModel

# Use Groq via OpenAI-compatible interface
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")
os.environ["OPENAI_BASE_URL"] = "https://api.groq.com/openai/v1"

if not os.environ["OPENAI_API_KEY"]:
    raise RuntimeError("OPENAI_API_KEY is not set")

model = OpenAIModel(
    model_name="llama-3.1-8b-instant"
)
