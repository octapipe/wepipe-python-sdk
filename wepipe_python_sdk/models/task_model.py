from __future__ import annotations
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from .task_type_model import TaskTypeModel
from .user_model import UserModel


class TaskModel(BaseModel):
    id: int = Field(default=None, alias='id')
    code: int = Field(default=None, alias='code')
    customer_id: int = Field(default=None, alias='customer_id')
    deal_id: int = Field(default=None, alias='card_id')
    task_type_id: int = Field(default=None, alias='task_type_id')
    creator_user_id: int = Field(default=None, alias='creator_user_id')
    responsible_user_id: int = Field(default=None, alias='responsible_user_id')
    source: str = Field(default=None, alias='source')
    name: str = Field(default=None, alias='name')
    note: Optional[str] = Field(default=None, alias='note')
    start: str = Field(default=None, alias='start')
    end: str = Field(default=None, alias='end')
    status: Optional[str] = Field(default=None, alias='status')
    is_finished: bool = Field(default=None, alias='is_finished')
    finished_at: Optional[str] = Field(default=None, alias='finished_at')
    created_at: str = Field(default=None, alias='created_at')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
    deleted_at: Optional[str] = Field(default=None, alias='deleted_at')
    deal: Optional['CardModel'] = Field(default=None, alias='deal')
    task_type: Optional[TaskTypeModel] = Field(default=None, alias='task_type')
    creator_user: Optional[UserModel] = Field(default=None, alias='creator_user')
    responsible_user: Optional[UserModel] = Field(default=None, alias='responsible_user')


from .card_model import CardModel

TaskModel.model_rebuild()
