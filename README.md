# 🗂️ gestion-info

Sistema de gestión de ventas por consola en Python. Permite realizar operaciones CRUD sobre registros de ventas con persistencia en archivo JSON, menú interactivo con colores y generación de datos falsos con Faker.

---

## 📋 Características principales

- ✅ Crear, listar, buscar, actualizar y eliminar ventas
- ✅ Persistencia real en archivo `data/records.json`
- ✅ Menú interactivo en consola con colores (colorama)
- ✅ Validación de entradas con manejo de errores (try-except)
- ✅ No permite IDs duplicados (uso de set)
- ✅ Generación de registros falsos con Faker
- ✅ Código modular separado por responsabilidades

---

## 🏗️ Arquitectura del proyecto

```
gestion-info/
├── assets/              # Ejercicios de práctica
│   ├── ejercicio1.py
│   ├── ejercicio2.py
│   ├── ejercicio3.py
│   ├── ejercicio4.py
│   ├── ejercicio5.py
│   └── ejercicio6.py
├── data/
│   └── records.json     # Almacenamiento de registros
├── src/
│   ├── main.py          # Punto de entrada
│   ├── menu.py          # Interfaz de consola (UI)
│   ├── service.py       # Lógica de negocio (CRUD)
│   ├── file.py          # Persistencia (leer/guardar)
│   ├── validate.py      # Validaciones y helpers
│   └── integration.py   # Integración con Faker
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/sasaelcrack/gestion-info.git
cd gestion-info
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

Las dependencias del proyecto son:

| Librería | Uso |
|---|---|
| `faker` | Generación de registros falsos |
| `colorama` | Colores en la consola |
| `pandas` | Disponible para reportes |
| `requests` | Disponible para integraciones externas |

---

## ▶️ Ejecución

```bash
py src/main.py
```

---

## 🖥️ Interfaz del sistema

Al ejecutar el programa aparece el siguiente menú interactivo:

```
=============================================
   Sistema de Gestión de Ventas
=============================================

┌─ Menú ───────────────────────────────┐
│  1. Crear venta                       │
│  2. Listar ventas                     │
│  3. Buscar venta                      │
│  4. Actualizar venta                  │
│  5. Eliminar venta                    │
│  6. Generar registros falsos (Faker)  │
│  7. Salir                             │
└───────────────────────────────────────┘
```

### Flujo de uso

- **Opción 1** — Ingresa ID, cliente, producto, cantidad y precio
- **Opción 2** — Lista todas las ventas ordenadas por cliente
- **Opción 3** — Busca una venta por su ID
- **Opción 4** — Actualiza campos de una venta existente
- **Opción 5** — Elimina una venta con confirmación previa
- **Opción 6** — Genera N registros falsos y los guarda en el archivo
- **Opción 7** — Sale del programa

---

## 🗃️ Estructura de un registro

```json
{
    "id": "V001",
    "cliente": "Ana Torres",
    "producto": "Laptop",
    "cantidad": 2,
    "precio": 1500.0,
    "estado": "ok"
}
```

---

## 👤 Autor

| Campo | Dato |
|---|---|
| **Nombre** | Samuel Salazar Nanclares |
| **GitHub** | [@sasaelcrack](https://github.com/sasaelcrack) |
| **Proyecto** | Taller de Transferencia — Manejo de archivos y estructuras de datos en Python |