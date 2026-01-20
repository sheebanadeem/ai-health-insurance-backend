import os
from pydantic_ai import Agent

model = f"openrouter:{os.getenv('OPENROUTER_MODEL')}"

explainer_agent = Agent(
    model=model,
    system_prompt="""
    You are a friendly assistant.
    Explain insurance decisions in simple,
    non-technical language for normal users.
    Provide helpful next steps.
    """
)
