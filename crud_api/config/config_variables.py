import os
from pathlib import Path
from dotenv import load_dotenv

# 1. Obtenemos la ruta absoluta de la carpeta raíz del proyecto
# (Subimos dos niveles desde crud_api/config hasta la raíz CRUD-FastAPI)
BASE_DIR = Path(__file__).resolve().parent.parent.parent
env_path = os.path.join(BASE_DIR, '.env')

# 2. Cargamos el archivo especificando la ruta exacta
load_dotenv(dotenv_path=env_path)

class Settings:
    # Usamos 'root' como valor por defecto si falla el .env
    DB_USER: str = os.getenv("DB_USER", "root")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "") 
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_NAME: str = os.getenv("DB_NAME", "test_db")

settings = Settings()

# 3. (Opcional) Debug para verificar si cargó bien
print(f"--- Conectando con usuario: {settings.DB_USER} ---")
