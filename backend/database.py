from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url ="postgresql://postgres:12345678@localhost:5432/telusko"
engine = create_engine(url=db_url)
SessionLocal = sessionmaker(autoflush=False)
