"""Pequeña calculadora usada como cambio de ejemplo para el laboratorio."""


def sumar(a: float, b: float) -> float:
    """Devuelve la suma de dos números."""
    return a + b


def restar(a: float, b: float) -> float:
    """Devuelve la diferencia entre dos números."""
    return a - b


if __name__ == "__main__":
    print(f"2 + 3 = {sumar(2, 3)}")
    print(f"5 - 1 = {restar(5, 1)}")
