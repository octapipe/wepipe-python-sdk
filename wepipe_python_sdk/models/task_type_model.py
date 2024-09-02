from pydantic import BaseModel, Field
from typing import Optional


class TaskTypeModel(BaseModel):
    id: int = Field(default=None, alias='id')
    name: Optional[str] = Field(default=None, alias='name')
    color: Optional[str] = Field(default=None, alias='color')
