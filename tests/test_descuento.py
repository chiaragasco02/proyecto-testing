import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.descuento import calcular_descuento
import pytest


# Caso exitoso
def test_descuento_correcto():
    assert calcular_descuento(1000, 20) == 800


# Caso error
def test_precio_negativo():
    with pytest.raises(ValueError):
        calcular_descuento(-100, 10)


# Caso borde
def test_descuento_total():
    assert calcular_descuento(500, 100) == 0