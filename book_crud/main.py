from fastapi import FastAPI
from book_crud.database.database import engine, Base
from book_crud.routes.crud_routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)
