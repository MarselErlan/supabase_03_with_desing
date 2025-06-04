from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db.session import get_session
from app.models.inventory_item import InventoryItem as InventoryItemModel
from app.schemas.inventory_item import InventoryItemCreate, InventoryItem
from typing import List

router = APIRouter()

@router.post("/inventory-items", response_model=InventoryItem)
def create_inventory_item(item: InventoryItemCreate, session: Session = Depends(get_session)):
    db_item = InventoryItemModel(**item.dict())
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item

@router.get("/inventory-items", response_model=List[InventoryItem])
def get_inventory_items(session: Session = Depends(get_session)):
    items = session.exec(select(InventoryItemModel)).all()
    return items