from pydantic import BaseModel, ConfigDict, Field
from typing import Literal, Optional
from enum import Enum

class Finding(BaseModel):
    agent: str = Field(min_length=1) 
    severity: Literal["critical","high","medium","low","info"]
    category: Literal["security","bug","quality"]
    title: str = Field(min_length=1)
    description: str = Field(min_length=1)
    line_range: str | None = None
    suggestion: str = Field(min_length=1)
    confidence: float = Field(ge=0.0 , le=1.0)


class ReviewRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    code: str = Field(min_length=1, max_length=20000)
    language: str = Field(min_length=1)


class ReviewResponse(BaseModel):
    run_id: str
    findings: list[Finding]
    summary: dict