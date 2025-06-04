from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.endpoints import inventory_item
from app.db.session import engine
from sqlmodel import SQLModel



@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(
    title="Inventory Management API",
    description="A structured API to manage inventory items in a Supabase PostgreSQL database.",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(inventory_item.router)