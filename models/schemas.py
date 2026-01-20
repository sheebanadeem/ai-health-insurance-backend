from pydantic import BaseModel
from typing import List, Optional


class PolicyData(BaseModel):
    coverage: List[str]
    exclusions: List[str]
    waiting_periods: List[str]


class CoverageDecision(BaseModel):
    is_covered: bool
    reason: str
    referenced_clauses: List[str]


class SimpleExplanation(BaseModel):
    summary: str
    next_steps: List[str]
