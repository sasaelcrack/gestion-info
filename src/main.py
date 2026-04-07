# main.py
# Punto de entrada — Módulo 3: CRUD completo con persistencia JSON

from service import new_register, list_records, search_record, update_record, delete_record

def mostrar_venta(venta: dict) -> None:
    print(f"""
  ID       : {venta['id']}
  Cliente  : {venta['cliente']}
  Producto : {venta['producto']}
  Cantidad : {venta['cantidad']}
  Precio   : ${venta['precio']:.2f}
  Estado   : {venta['estado']}
  {'─' * 30}""")


def demo_create() -> None:
    ventas_prueba = [
        ("V001", "Ana Torres",  "Laptop",    2, 1500.0, "ok"),
        ("V002", "Luis Gómez",  "Monitor",   1,  350.0, "ok"),
        ("V003", "María López", "Teclado",   5,   45.0, "ok"),
        ("V001", "Duplicado",   "Mouse",     1,   20.0, "ok"),  
        ("V004", "",            "Mouse",     1,   20.0, "ok"),  
        ("V005", "Carlos Ruiz", "Audífonos", 3,   80.0, "ok"),
    ]
    print("\n CREATE — Creando ventas...\n")
    for datos in ventas_prueba:
        exito, mensaje = new_register(*datos)
        print(f"  {'✅' if exito else '❌'} {mensaje}")

def demo_list() -> None:
    ventas = list_records(orden="cliente")
    print(f"\n LIST — Ventas ordenadas por cliente ({len(ventas)} registros):")
    print("  " + "─" * 30)
    if not ventas:
        print("  (sin registros)")
        return
    for venta in ventas:
        mostrar_venta(venta)

def demo_search() -> None:
    print("\n SEARCH — Buscando V002...")
    venta = search_record("V002")
    if venta:
        mostrar_venta(venta)
    else:
        print("  ❌ No encontrado.")

    print("\n SEARCH — Buscando V999 (no existe)...")
    venta = search_record("V999")
    if venta:
        mostrar_venta(venta)
    else:
        print("  ❌ No encontrado.")

def demo_update() -> None:
    print("\n  UPDATE — Actualizando V003...")
    exito, mensaje = update_record("V003", cliente="María Pérez", precio=50.0)
    print(f"  {'✅' if exito else '❌'} {mensaje}")

    print("\n  UPDATE — Actualizando V999 (no existe)...")
    exito, mensaje = update_record("V999", cliente="Fantasma")
    print(f"  {'✅' if exito else '❌'} {mensaje}")

def demo_delete() -> None:
    print("\n  DELETE — Eliminando V005...")
    exito, mensaje = delete_record("V005")
    print(f"  {'✅' if exito else '❌'} {mensaje}")

    print("\n  DELETE — Eliminando V999 (no existe)...")
    exito, mensaje = delete_record("V999")
    print(f"  {'✅' if exito else '❌'} {mensaje}")

if __name__ == "__main__":
    print("=" * 40)
    print("   Sistema de Gestión de Ventas")
    print("   Módulo 3 — CRUD completo")
    print("=" * 40)

    demo_create()
    demo_list()
    demo_search()
    demo_update()
    demo_delete()

    print("\n Estado final:")
    demo_list()

    print("\n✔ Sistema listo.\n")