import os
from pydantic_ai import Agent

model = f"openrouter:{os.getenv('OPENROUTER_MODEL')}"

policy_parser_agent = Agent(
    model=model,
    system_prompt="""
You are an expert health insurance policy analyst.

Rules:
- Answer ONLY based on the policy text
- If information is missing, say "Not mentioned in the policy"
- Be concise and structured
"""
)
