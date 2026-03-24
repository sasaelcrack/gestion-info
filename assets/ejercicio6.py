#🧩 Ejercicio 6: Refactorizar procesamiento de ventas (separar lógica/I-O + eficiencia + pruebas)

import unittest

def _calculate_discount(sale: dict) -> float:
    discount = 0.0
    if sale["qty"] >= 10:
        discount += 0.10
    if sale["customer"] == "vip":
        discount += 0.05
    return discount

def calculate_sale_total(sale: dict) -> float:
    if sale["status"] != "ok":
        raise ValueError(f"Venta inválida: {sale}")
    discount = _calculate_discount(sale)
    subtotal = sale["price"] * sale["qty"]
    return subtotal - (subtotal * discount)


def calculate_total(sales: list) -> float:
    total = 0.0
    for sale in sales:
        try:
            total += calculate_sale_total(sale)
        except ValueError:
            pass
    return total

def report_invalid_sales(sales: list) -> None:
    for sale in sales:
        if sale["status"] != "ok":
            print("bad sale:", sale)
            
class TestCalculateSaleTotal(unittest.TestCase):

    def test_venta_sin_descuento(self):
        sale = {"status": "ok", "price": 100.0, "qty": 1, "customer": "regular"}
        self.assertEqual(calculate_sale_total(sale), 100.0)

    def test_descuento_por_cantidad(self):
        sale = {"status": "ok", "price": 100.0, "qty": 10, "customer": "regular"}
        self.assertEqual(calculate_sale_total(sale), 900.0)

    def test_descuento_por_vip(self):
        sale = {"status": "ok", "price": 100.0, "qty": 1, "customer": "vip"}
        self.assertEqual(calculate_sale_total(sale), 95.0)

    def test_descuento_cantidad_y_vip(self):
        sale = {"status": "ok", "price": 100.0, "qty": 10, "customer": "vip"}
        self.assertEqual(calculate_sale_total(sale), 850.0)

    def test_venta_invalida_lanza_excepcion(self):
        sale = {"status": "error", "price": 100.0, "qty": 5, "customer": "regular"}
        with self.assertRaises(ValueError):
            calculate_sale_total(sale)


class TestCalculateTotal(unittest.TestCase):

    def test_suma_ventas_validas(self):
        sales = [
            {"status": "ok",    "price": 100.0, "qty": 1,  "customer": "regular"},
            {"status": "ok",    "price": 200.0, "qty": 1,  "customer": "regular"},
            {"status": "error", "price": 999.0, "qty": 99, "customer": "vip"},
        ]
        self.assertEqual(calculate_total(sales), 300.0)

    def test_lista_vacia(self):
        self.assertEqual(calculate_total([]), 0.0)

    def test_todas_invalidas(self):
        sales = [
            {"status": "error", "price": 100.0, "qty": 5, "customer": "regular"},
            {"status": "error", "price": 200.0, "qty": 3, "customer": "vip"},
        ]
        self.assertEqual(calculate_total(sales), 0.0)