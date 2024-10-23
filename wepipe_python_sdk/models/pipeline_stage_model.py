from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class PipelineStageModel(BaseModel):
    stage: str = Field(default=None, alias='stage')
    stage_index: int = Field(default=None, alias='stage_index')
    total: Optional[int] = Field(default=None, alias='total')
    moved_at: Optional[datetime] = Field(default=None, alias='moved_at')
