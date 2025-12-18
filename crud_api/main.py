from fastapi import FastAPI
from crud_api.database.database import engine, Base
from crud_api.routes.crud_routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)
