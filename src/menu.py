# menu.py
# Módulo de menú interactivo en consola
# Módulo 5: agregada opción de generar registros falsos con Faker

from colorama import init, Fore, Style
from service import new_register, list_records, search_record, update_record, delete_record
from integration import generar_registros_falsos

init(autoreset=True)

def _encabezado() -> None:
    print(Fore.CYAN + "=" * 45)
    print(Fore.CYAN + "   Sistema de Gestión de Ventas")
    print(Fore.CYAN + "=" * 45)


def _mostrar_venta(venta: dict) -> None:
    print(Fore.WHITE + f"""
  ID       : {Fore.YELLOW}{venta['id']}
  {Fore.WHITE}Cliente  : {venta['cliente']}
  Producto : {venta['producto']}
  Cantidad : {venta['cantidad']}
  Precio   : ${venta['precio']:.2f}
  Estado   : {Fore.GREEN if venta['estado'] == 'ok' else Fore.RED}{venta['estado']}
  {Fore.WHITE}{'─' * 35}""")


def _input_requerido(prompt: str) -> str:
    while True:
        valor = input(Fore.WHITE + prompt).strip()
        if valor:
            return valor
        print(Fore.RED + "  ⚠ Este campo no puede estar vacío.")


def _input_numero(prompt: str, tipo=float):
    while True:
        try:
            return tipo(input(Fore.WHITE + prompt).strip())
        except ValueError:
            print(Fore.RED + "  ⚠ Ingresa un número válido.")

def _crear_venta() -> None:
    print(Fore.CYAN + "\n── Crear nueva venta ──")
    id_venta = _input_requerido("  ID       : ")
    cliente  = _input_requerido("  Cliente  : ")
    producto = _input_requerido("  Producto : ")
    cantidad = _input_numero("  Cantidad : ", int)
    precio   = _input_numero("  Precio   : ")

    exito, mensaje = new_register(id_venta, cliente, producto, cantidad, precio)
    print(Fore.GREEN + f"\n  ✅ {mensaje}" if exito else Fore.RED + f"\n  ❌ {mensaje}")


def _listar_ventas() -> None:
    print(Fore.CYAN + "\n── Listado de ventas ──")
    ventas = list_records(orden="cliente")
    if not ventas:
        print(Fore.YELLOW + "  (sin registros)")
        return
    print(Fore.WHITE + f"  {len(ventas)} registro(s) ordenados por cliente:")
    for venta in ventas:
        _mostrar_venta(venta)


def _buscar_venta() -> None:
    print(Fore.CYAN + "\n── Buscar venta ──")
    id_venta = _input_requerido("  ID a buscar: ")
    venta = search_record(id_venta)
    if venta:
        _mostrar_venta(venta)
    else:
        print(Fore.RED + f"  ❌ No se encontró la venta con ID '{id_venta}'.")


def _actualizar_venta() -> None:
    print(Fore.CYAN + "\n── Actualizar venta ──")
    id_venta = _input_requerido("  ID a actualizar: ")

    venta = search_record(id_venta)
    if not venta:
        print(Fore.RED + f"  ❌ No se encontró la venta con ID '{id_venta}'.")
        return

    print(Fore.YELLOW + "  (deja en blanco para no cambiar el campo)")
    campos = {}

    cliente = input(Fore.WHITE + f"  Cliente [{venta['cliente']}]: ").strip()
    if cliente:
        campos["cliente"] = cliente

    producto = input(Fore.WHITE + f"  Producto [{venta['producto']}]: ").strip()
    if producto:
        campos["producto"] = producto

    cantidad = input(Fore.WHITE + f"  Cantidad [{venta['cantidad']}]: ").strip()
    if cantidad:
        try:
            campos["cantidad"] = int(cantidad)
        except ValueError:
            print(Fore.RED + "  ⚠ Cantidad inválida, se omite.")

    precio = input(Fore.WHITE + f"  Precio [{venta['precio']}]: ").strip()
    if precio:
        try:
            campos["precio"] = float(precio)
        except ValueError:
            print(Fore.RED + "  ⚠ Precio inválido, se omite.")

    if not campos:
        print(Fore.YELLOW + "  ⚠ No se realizaron cambios.")
        return

    exito, mensaje = update_record(id_venta, **campos)
    print(Fore.GREEN + f"\n  ✅ {mensaje}" if exito else Fore.RED + f"\n  ❌ {mensaje}")


def _eliminar_venta() -> None:
    print(Fore.CYAN + "\n── Eliminar venta ──")
    id_venta = _input_requerido("  ID a eliminar: ")

    venta = search_record(id_venta)
    if not venta:
        print(Fore.RED + f"  ❌ No se encontró la venta con ID '{id_venta}'.")
        return

    confirmar = input(Fore.YELLOW + f"  ¿Eliminar '{id_venta}'? (s/n): ").strip().lower()
    if confirmar != "s":
        print(Fore.YELLOW + "  Operación cancelada.")
        return

    exito, mensaje = delete_record(id_venta)
    print(Fore.GREEN + f"\n  ✅ {mensaje}" if exito else Fore.RED + f"\n  ❌ {mensaje}")


def _generar_falsos() -> None:
    print(Fore.CYAN + "\n── Generar registros falsos con Faker ──")
    try:
        cantidad = int(input(Fore.WHITE + "  ¿Cuántos registros generar? (default 10): ").strip() or "10")
    except ValueError:
        cantidad = 10

    print(Fore.YELLOW + f"\n  Generando {cantidad} registros...")
    exitosos, fallidos = generar_registros_falsos(cantidad=cantidad)
    print(Fore.GREEN + f"  ✅ {exitosos} registros creados correctamente.")
    if fallidos:
        print(Fore.RED + f"  ❌ {fallidos} registros fallaron.")

def mostrar_menu() -> None:
    print(Fore.CYAN + "\n┌─ Menú ───────────────────────────────┐")
    print(Fore.WHITE + "│  1. Crear venta                       │")
    print(Fore.WHITE + "│  2. Listar ventas                     │")
    print(Fore.WHITE + "│  3. Buscar venta                      │")
    print(Fore.WHITE + "│  4. Actualizar venta                  │")
    print(Fore.WHITE + "│  5. Eliminar venta                    │")
    print(Fore.MAGENTA+"│  6. Generar registros falsos (Faker)  │")
    print(Fore.RED   + "│  7. Salir                             │")
    print(Fore.CYAN  + "└───────────────────────────────────────┘")


def ejecutar_menu() -> None:
    _encabezado()

    opciones = {
        "1": _crear_venta,
        "2": _listar_ventas,
        "3": _buscar_venta,
        "4": _actualizar_venta,
        "5": _eliminar_venta,
        "6": _generar_falsos,
    }

    while True:
        mostrar_menu()
        try:
            opcion = input(Fore.CYAN + "  Elige una opción: ").strip()

            if opcion == "7":
                print(Fore.YELLOW + "\n  Hasta luego. 👋\n")
                break
            elif opcion in opciones:
                opciones[opcion]()
            else:
                raise ValueError(f"Opción inválida: '{opcion}'")

        except ValueError as e:
            print(Fore.RED + f"  ⚠ {e} — ingresa un número del 1 al 7.")
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n\n  Programa interrumpido. Hasta luego. 👋\n")
            break