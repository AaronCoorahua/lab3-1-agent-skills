"""Pequeña calculadora usada como cambio de ejemplo para el laboratorio."""


def sumar(a: float, b: float) -> float:
    """Devuelve la suma de dos números."""
    return a + b


def restar(a: float, b: float) -> float:
    """Devuelve la diferencia entre dos números."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Devuelve el producto de dos números."""
    return a * b


if __name__ == "__main__":
    print(f"2 + 3 = {sumar(2, 3)}")
    print(f"5 - 1 = {restar(5, 1)}")
    print(f"4 * 3 = {multiplicar(4, 3)}")
    print("Hola mundo")
    print("Hola mundo 2")
    print("Hola mundo 3")
    print("Hola mundo 4")
