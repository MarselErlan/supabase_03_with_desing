from sqlmodel import SQLModel, Field

class InventoryItem(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  name: str
  price: float
  is_offer: bool = False