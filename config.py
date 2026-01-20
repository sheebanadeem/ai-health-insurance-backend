from dotenv import load_dotenv
load_dotenv()

import os
from pydantic_ai.models.groq import GroqModel

if not os.getenv("GROQ_API_KEY"):
    raise RuntimeError("GROQ_API_KEY is not set")

model = GroqModel(
    model_name="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
)
