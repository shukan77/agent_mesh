from pydantic import BaseModel, Field
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