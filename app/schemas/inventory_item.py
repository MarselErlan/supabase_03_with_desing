from pydantic import BaseModel
from typing import List

class InventoryItemBase(BaseModel):
    name: str
    price: float
    is_offer: bool = False

class InventoryItemCreate(InventoryItemBase):
    pass

class InventoryItem(InventoryItemBase):
    id: int

    class Config:
        from_attributes = True