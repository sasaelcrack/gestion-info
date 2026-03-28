# Módulo de lógica de negocio — CRUD en memoria

from validate import validar_registro


_ventas: list = []           
_ids_registrados: set = set()  


def _construir_venta(id_venta: str, cliente: str, producto: str,
                     cantidad: int, precio: float, estado: str = "ok") -> dict:
    return {
        "id": id_venta.strip(),
        "cliente": cliente.strip(),
        "producto": producto.strip(),
        "cantidad": int(cantidad),
        "precio": float(precio),
        "estado": estado.strip()
    }


def crear_venta(id_venta: str, cliente: str, producto: str,
                cantidad: int, precio: float, estado: str = "ok") -> tuple[bool, str]:

    
    if id_venta.strip() in _ids_registrados:
        return False, f"Error: ya existe una venta con ID '{id_venta}'."

    registro = _construir_venta(id_venta, cliente, producto, cantidad, precio, estado)


    es_valido, errores = validar_registro(registro)
    if not es_valido:
        return False, "Errores de validación:\n" + "\n".join(f"  - {e}" for e in errores)

    _ventas.append(registro)
    _ids_registrados.add(registro["id"])
    return True, f"Venta '{registro['id']}' creada correctamente."


def listar_ventas() -> list:
    return list(_ventas)


def buscar_venta(id_venta: str) -> dict | None:
    coincidencias = [v for v in _ventas if v["id"] == id_venta.strip()]
    return coincidencias[0] if coincidencias else None


def actualizar_venta(id_venta: str, **kwargs) -> tuple[bool, str]:
    campos_permitidos = {"cliente", "producto", "cantidad", "precio", "estado"}

    venta = buscar_venta(id_venta)
    if venta is None:
        return False, f"Error: no se encontró la venta con ID '{id_venta}'."


    for campo, valor in kwargs.items():
        if campo in campos_permitidos:
            venta[campo] = valor

    es_valido, errores = validar_registro(venta)
    if not es_valido:
        return False, "Errores tras actualización:\n" + "\n".join(f"  - {e}" for e in errores)

    return True, f"Venta '{id_venta}' actualizada correctamente."


def eliminar_venta(id_venta: str) -> tuple[bool, str]:
    global _ventas
    venta = buscar_venta(id_venta)
    if venta is None:
        return False, f"Error: no se encontró la venta con ID '{id_venta}'."

    _ventas = [v for v in _ventas if v["id"] != id_venta.strip()]
    _ids_registrados.discard(id_venta.strip())
    return True, f"Venta '{id_venta}' eliminada correctamente."


def obtener_ids() -> set:
    return set(_ids_registrados)