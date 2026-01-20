from pydantic_ai import Agent
from config import model

policy_parser_agent = Agent(
    model=model,
    system_prompt="""
    You are a health insurance policy analysis assistant.
    Answer user questions clearly and concisely.
    """
)
