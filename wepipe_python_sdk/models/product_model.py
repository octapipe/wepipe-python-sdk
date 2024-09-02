from __future__ import annotations
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional, Union


class ProductModel(BaseModel):
    id: int = Field(default=None, alias='id')
    customer_id: int = Field(default=None, alias='customer_id')
    sku: Optional[str] = Field(default=None, alias='sku')
    name: str = Field(default=None, alias='name')
    currency: str = Field(default=None, alias='currency')
    price: float = Field(default=None, alias='price')
    color: str = Field(default=None, alias='color')
    picture: Optional[str] = Field(default=None, alias='picture')
    custom_fields: Optional[Union[List[Dict[str, Any]], List[List[Any]]]] = Field(default=None, alias='custom_fields')
    created_at: str = Field(default=None, alias='created_at')
    updated_at: str = Field(default=None, alias='updated_at')
    deleted_at: Optional[str] = Field(default=None, alias='deleted_at')
    products: List[ProductModel] = Field(default=None, alias='products')
