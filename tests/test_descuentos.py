import pytest
from src.descuentos import calcular_precio_final

# Caso 1: Aplicación correcta del descuento (monto 15000)
def test_descuento_aplicado():
    assert calcular_precio_final(15000) == 13500

# Caso 2: Manejo de error por monto inválido (monto -100)
def test_monto_negativo():
    with pytest.raises(ValueError):
        calcular_precio_final(-100)

# Caso 3: Monto en el límite (monto 10000)
def test_monto_limite():
    assert calcular_precio_final(10000) == 10000