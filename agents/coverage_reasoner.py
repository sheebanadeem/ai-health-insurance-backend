import os
from pydantic_ai import Agent

model = f"openrouter:{os.getenv('OPENROUTER_MODEL')}"

coverage_reasoner_agent = Agent(
    model=model,
    system_prompt="""
    You are an expert health insurance claim evaluator.
    Determine whether the user's claim is covered
    based on policy data and the user's question.
    Provide clear reasoning and cite relevant clauses.
    """
)
