from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://postgres:1234321@localhost:5432/tododb"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    
    autoflush=False,
    autocommit=False,
    bind=engine
)

Base = declarative_base()

Base.metadata.create_all(bind=engine)

def get_db():
    
    db = SessionLocal()
    
    try:
        
        yield db
        
    finally:
        
        db.close()
        
