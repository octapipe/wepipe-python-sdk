from __future__ import annotations
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional, Union
from .user_model import UserModel
from .contact_model import ContactModel
from .company_model import CompanyModel
from .product_model import ProductModel
from .pipeline_stage_model import PipelineStageModel


class CardModel(BaseModel):
    id: int = Field(default=None, alias='id')
    code: int = Field(default=None, alias='code')
    name: str = Field(default=None, alias='name')
    pipeline_id: int = Field(default=None, alias='pipeline_id')
    pipeline_stage_id: int = Field(default=None, alias='pipeline_stage_id')
    customer_id: int = Field(default=None, alias='customer_id')
    user_id: int = Field(default=None, alias='user_id')
    lost_reason: Optional[str] = Field(default=None, alias='lost_reason')
    currency: str = Field(default=None, alias='currency')
    amount: str = Field(default=None, alias='amount')
    custom_fields: Optional[List[Dict[str, Any]]] = Field(default=None, alias='custom_fields')
    last_stage_updated_at: str = Field(default=None, alias='last_stage_updated_at')
    created_at: str = Field(default=None, alias='created_at')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
    deleted_at: Optional[str] = Field(default=None, alias='deleted_at')
    pipeline: Optional[str] = Field(default=None, alias='pipeline')
    pipeline_stage: Optional[str] = Field(default=None, alias='pipeline_stage')
    tags: List[str] = Field(default=None, alias='tags')
    user: Optional[UserModel] = Field(default=None, alias='user')
    tasks: Optional[List['TaskModel']] = Field(default=None, alias='tasks')
    contacts: Optional[Union[List[ContactModel], list[int]]] = Field(default=None, alias='contacts')
    companies: Optional[List[CompanyModel]] = Field(default=None, alias='companies')
    products: Optional[List[ProductModel]] = Field(default=None, alias='products')
    deals: Optional[List[CardModel]] = Field(default=None, alias='deals')
    pipeline_stages: Optional[List[PipelineStageModel]] = Field(default=None, alias='pipeline_stages')


from .task_model import TaskModel

CardModel.model_rebuild()
