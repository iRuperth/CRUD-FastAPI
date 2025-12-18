from sqlalchemy.orm import Session
from schemas import crud_schema
from models.curd_model import Item

class CrudControllers:

'''
Si no usaramos @static methos tendriamos que escribir:

def __init__(self, db: Session): # El trabajador ya tiene su caja de herramientas (self.db) y no necesita traer nada externo cada vez.
        self.db = db

y el controlador se vería así:

 def create_item(self, item: crud_schema.ItemCreate): # No hace falta pasar db:session cada vez
        db_item = Item(**item.dict())
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item
'''

    @staticmethod
    async def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()

    @staticmethod # Cada función es como un trabajador independiente que llega con su propio conjunto de herramientas (db) y hace su tarea.
    async def get_item(db: Session, item_id: int):
        return db.query(Item).filter(Item.id == item_id).first()

    @staticmethod
    async def create_item(db: Session, item: crud_schema.ItemCreate):
        db_item = Item(**item.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

   @staticmethod
   async def update_item(db: Session, item_id: int, item: crud_schema.ItemCreate):
       db_item = db.query(Item).filter(Item.id == item_id).first()
       if db_item:
           db_item.title = item.title
           db_item.description = item.description
           db.commit()
           db.refresh(db_item)
       return db_item
   
   @staticmethod
   async def delete_item(db: Session, item_id: int):
       db_item = db.query(Item).filter(Item.id == item_id).first()
       if db_item:
           db.delete(db_item)
           db.commit()
       return db_item