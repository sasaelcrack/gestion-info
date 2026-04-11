# tests.py
# Pruebas unitarias del sistema de gestión de ventas
# Módulo 6: mínimo 4 pruebas con pytest

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from validate import (
    validar_id,
    validar_cliente,
    validar_cantidad,
    validar_precio,
    validar_estado,
    validar_registro,
)

class TestValidarId:
    def test_id_valido(self):
        assert validar_id("V001") is True

    def test_id_vacio_falla(self):
        assert validar_id("") is False

    def test_id_solo_espacios_falla(self):
        assert validar_id("   ") is False


class TestValidarCliente:
    def test_cliente_valido(self):
        assert validar_cliente("Ana Torres") is True

    def test_cliente_un_caracter_falla(self):
        assert validar_cliente("A") is False

    def test_cliente_vacio_falla(self):
        assert validar_cliente("") is False


class TestValidarCantidad:
    def test_cantidad_valida(self):
        assert validar_cantidad(5) is True

    def test_cantidad_cero_falla(self):
        assert validar_cantidad(0) is False

    def test_cantidad_negativa_falla(self):
        assert validar_cantidad(-1) is False

    def test_cantidad_texto_falla(self):
        assert validar_cantidad("abc") is False


class TestValidarPrecio:
    def test_precio_valido(self):
        assert validar_precio(100.0) is True

    def test_precio_cero_falla(self):
        assert validar_precio(0) is False

    def test_precio_negativo_falla(self):
        assert validar_precio(-50.0) is False

    def test_precio_texto_falla(self):
        assert validar_precio("gratis") is False


class TestValidarEstado:
    def test_estado_ok(self):
        assert validar_estado("ok") is True

    def test_estado_error(self):
        assert validar_estado("error") is True

    def test_estado_invalido_falla(self):
        assert validar_estado("pendiente") is False


class TestValidarRegistro:
    def test_registro_completo_valido(self):
        registro = {
            "id": "V001",
            "cliente": "Ana Torres",
            "producto": "Laptop",
            "cantidad": 2,
            "precio": 1500.0,
            "estado": "ok"
        }
        es_valido, errores = validar_registro(registro)
        assert es_valido is True
        assert errores == []

    def test_registro_con_campos_invalidos(self):
        registro = {
            "id": "",
            "cliente": "A",
            "producto": "Laptop",
            "cantidad": 0,
            "precio": -10.0,
            "estado": "ok"
        }
        es_valido, errores = validar_registro(registro)
        assert es_valido is False
        assert len(errores) >= 3

    def test_registro_estado_invalido(self):
        registro = {
            "id": "V002",
            "cliente": "Luis Gómez",
            "producto": "Monitor",
            "cantidad": 1,
            "precio": 350.0,
            "estado": "desconocido"
        }
        es_valido, errores = validar_registro(registro)
        assert es_valido is False
        assert any("Estado" in e for e in errores)