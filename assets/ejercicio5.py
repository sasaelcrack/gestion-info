# 🧩 Ejercicio 5: 
#Refactorizar validador de contraseñas (legibilidad + mantenibilidad + pruebas)
#Código inicial (mejorable)

import unittest

def _has_minimum_length(password: str) -> bool:
    return len(password) >= 8

def _has_at_least_one_digit(password: str) -> bool:
    return any(char.isdigit() for char in password)

def _has_at_least_one_uppercase(password: str) -> bool:
    return any(char.isupper() for char in password)

def _has_no_spaces(password: str) -> bool:
    return " " not in password

def is_valid_password(password: str) -> bool:
    if not _has_minimum_length(password):
        return False
    if not _has_at_least_one_digit(password):
        return False
    if not _has_at_least_one_uppercase(password):
        return False
    if not _has_no_spaces(password):
        return False
    return True

class TestIsValidPassword(unittest.TestCase):

    def test_password_valida(self):
        self.assertTrue(is_valid_password("Abcdefg1"))

    def test_falla_sin_mayuscula(self):
        self.assertFalse(is_valid_password("abcdefg1"))

    def test_falla_sin_digito(self):
        self.assertFalse(is_valid_password("ABCDEFGH"))

    def test_falla_con_espacio(self):
        self.assertFalse(is_valid_password("Abcdef 1"))

    def test_falla_muy_corta(self):
        self.assertFalse(is_valid_password("Ab1"))

    def test_falla_7_caracteres(self):
        self.assertFalse(is_valid_password("Abcdef1"))

    def test_falla_cadena_vacia(self):
        self.assertFalse(is_valid_password(""))

    def test_password_exactamente_8_caracteres(self):
        self.assertTrue(is_valid_password("Aa000000"))