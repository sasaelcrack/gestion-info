# crear y listar ventas en memoria

from service import crear_venta, listar_ventas


def mostrar_venta(venta: dict) -> None:
    """Imprime un registro de venta con formato legible."""
    print(f"""
  ID       : {venta['id']}
  Cliente  : {venta['cliente']}
  Producto : {venta['producto']}
  Cantidad : {venta['cantidad']}
  Precio   : ${venta['precio']:.2f}
  Estado   : {venta['estado']}
  {'─' * 30}""")


def demo_crear_ventas() -> None:
    ventas_prueba = [
        ("V001", "Ana Torres",    "Laptop",   2, 1500.0, "ok"),
        ("V002", "Luis Gómez",    "Monitor",  1,  350.0, "ok"),
        ("V003", "María López",   "Teclado",  5,   45.0, "ok"),
        ("V001", "Duplicado",     "Mouse",    1,   20.0, "ok"),   # ID duplicado → debe fallar
        ("V004", "",              "Mouse",    1,   20.0, "ok"),   # Cliente vacío → debe fallar
        ("V005", "Carlos Ruiz",   "Audífonos",3,   80.0, "ok"),
    ]

    print("\n Creando ventas...\n")
    for datos in ventas_prueba:
        exito, mensaje = crear_venta(*datos)
        estado = "✅" if exito else "❌"
        print(f"  {estado} {mensaje}")


def demo_listar_ventas() -> None:
    ventas = listar_ventas()
    print(f"\n Ventas en memoria ({len(ventas)} registros):")
    print("  " + "─" * 30)

    if not ventas:
        print("  (sin registros)")
        return

    for venta in ventas:
        mostrar_venta(venta)


if __name__ == "__main__":
    print("=" * 40)
    print("   Sistema de Gestión de Ventas")
    print("   Módulo 1 — Datos en memoria")
    print("=" * 40)

    demo_crear_ventas()
    demo_listar_ventas()

    print("\n Sistema listo.\n")