# integration.py
# Módulo de integración con librería externa — Faker
# Módulo 5: generación de registros falsos

from faker import Faker
from service import new_register

fake = Faker("es_ES")  # Faker en español

_PRODUCTOS = [
    "Laptop", "Monitor", "Teclado", "Mouse", "Audífonos",
    "Webcam", "Impresora", "Tablet", "Disco Duro", "Memoria USB"
]


def _generar_id_unico(*args, ids_existentes: set = None, **kwargs) -> str:
    ids_existentes = ids_existentes or set()
    while True:
        nuevo_id = f"F{fake.unique.random_int(min=100, max=999)}"
        if nuevo_id not in ids_existentes:
            return nuevo_id


def generar_registros_falsos(*args, cantidad: int = 10, **kwargs) -> tuple[int, int]:

    from service import obtener_ids

    exitosos = 0
    fallidos = 0

    for _ in range(cantidad):
        id_venta  = _generar_id_unico(ids_existentes=obtener_ids())
        cliente   = fake.name()
        producto  = fake.random_element(_PRODUCTOS)
        cantidad_ = fake.random_int(min=1, max=20)
        precio    = round(fake.random_number(digits=3, fix_len=False) + fake.random.uniform(0, 999), 2)
        precio    = max(10.0, precio)

        exito, _ = new_register(id_venta, cliente, producto, cantidad_, precio)
        if exito:
            exitosos += 1
        else:
            fallidos += 1

    return exitosos, fallidos