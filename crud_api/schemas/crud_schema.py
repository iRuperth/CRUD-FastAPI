from pydantic import BaseModel

class ItemSchema(BaseModel):
    title: str
    description: str

class ItemCreate(ItemSchema):
    pass

class ItemResponse(ItemSchema):
    id: int

    class Config:
        from_attributes = True
