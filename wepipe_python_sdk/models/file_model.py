from pydantic import BaseModel, Field
from typing import Dict, Any, Optional


class FileModel(BaseModel):
    id: int = Field(default=None, alias='id')
    customer_id: int = Field(default=None, alias='customer_id')
    user_id: int = Field(default=None, alias='user_id')
    record_id: int = Field(default=None, alias='record_id')
    entity: str = Field(default=None, alias='entity')
    name: str = Field(default=None, alias='name')
    url: str = Field(default=None, alias='url')
    mime: str = Field(default=None, alias='mime')
    size: int = Field(default=None, alias='size')
    created_at: str = Field(default=None, alias='created_at')
    updated_at: str = Field(default=None, alias='updated_at')
    deleted_at: Optional[str] = Field(default=None, alias='deleted_at')
    user: Dict[str, Any] = Field(default=None, alias='user')
