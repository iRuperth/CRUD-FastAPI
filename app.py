from fastapi import FastAPI
from routes.routes import router

app = FastAPI()

#IMPORTANT: Aquí referenciamos el archivo "database" no la variable "db"
from database import database

def run():
    pass
if __name__ == '__main__':
    database.Base.metadata.create_all(database.engine)
    run()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(router, prefix="/v1")