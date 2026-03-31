# Módulo de persistencia — lectura y escritura en archivo JSON

import json
import os

RUTA_ARCHIVO = os.path.join(os.path.dirname(__file__), "..", "data", "records.json")


def load_data() -> list:

    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
            contenido = f.read().strip()
            if not contenido:
                return []
            return json.loads(contenido)
    except FileNotFoundError:
        print("  Archivo de datos no encontrado. Iniciando con lista vacía.")
        return []
    except json.JSONDecodeError:
        print("  Archivo de datos dañado. Iniciando con lista vacía.")
        return []
    except Exception as e:
        print(f"  Error inesperado al leer datos: {e}")
        return []


def save_data(data: list) -> bool:
    try:
        os.makedirs(os.path.dirname(RUTA_ARCHIVO), exist_ok=True)
        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except PermissionError:
        print("  Sin permisos para escribir en el archivo de datos.")
        return False
    except Exception as e:
        print(f"  Error inesperado al guardar datos: {e}")
        return False