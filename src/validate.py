# Módulo de validaciones de campos para registros de ventas

ESTADOS_VALIDOS = {"ok", "error"}


def validar_id(id_venta: str) -> bool:

    return isinstance(id_venta, str) and id_venta.strip() != ""


def validar_cliente(cliente: str) -> bool:

    return isinstance(cliente, str) and len(cliente.strip()) >= 2


def validar_producto(producto: str) -> bool:

    return isinstance(producto, str) and producto.strip() != ""


def validar_cantidad(cantidad) -> bool:
    
    try:
        return int(cantidad) > 0
    except (ValueError, TypeError):
        return False


def validar_precio(precio) -> bool:
    try:
        return float(precio) > 0
    except (ValueError, TypeError):
        return False


def validar_estado(estado: str) -> bool:
    """El estado debe ser 'ok' o 'error'."""
    return estado in ESTADOS_VALIDOS


def validar_registro(registro: dict) -> tuple[bool, list]:
    
    errores = []

    if not validar_id(registro.get("id", "")):
        errores.append("ID inválido: no puede estar vacío.")

    if not validar_cliente(registro.get("cliente", "")):
        errores.append("Cliente inválido: debe tener al menos 2 caracteres.")

    if not validar_producto(registro.get("producto", "")):
        errores.append("Producto inválido: no puede estar vacío.")

    if not validar_cantidad(registro.get("cantidad")):
        errores.append("Cantidad inválida: debe ser un número entero mayor a 0.")

    if not validar_precio(registro.get("precio")):
        errores.append("Precio inválido: debe ser un número mayor a 0.")

    if not validar_estado(registro.get("estado", "")):
        errores.append(f"Estado inválido: debe ser uno de {ESTADOS_VALIDOS}.")

    return (len(errores) == 0, errores)