
from sqlmodel import Session, create_engine
from app.core.config import settings

engine = create_engine(settings.POSTGRES_URI, echo=True)

def get_session():
    with Session(engine) as session:
        yield session