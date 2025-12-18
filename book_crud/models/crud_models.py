from sqlalchemy import Column, Integer, String
from book_crud.database.database import Base 

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)        
    description = Column(String(500), index=True)  
