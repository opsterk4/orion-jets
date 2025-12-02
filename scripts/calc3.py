"""
Script de ejemplo equivalente a calc.py pero usando Cyclopts en lugar de argparse.

Este programa realiza una operación aritmética sencilla entre dos números
proporcionados por el usuario. Las operaciones permitidas son:

- "sumar"  → suma de x y y
- "restar" → resta de x y y

El usuario también puede activar un modo "verbose". Si verbose es True,
el programa imprime solo el resultado numérico. Si verbose es False,
imprime la operación completa.

Ejemplos de uso:

    uv run scripts/calc3.py 3 4
    uv run scripts/calc3.py 10 7 --operacion restar
    uv run scripts/calc3.py 5 6 --verbose
"""

import cyclopts
from typing import Literal


def main(
    x: float,
    y: float,
    precision: int = 1,
    operacion: Literal["sumar", "restar", "multiplicar", "dividir"] = "sumar",
    verbose: bool = False,
) -> None:
    """
    Realiza una operación aritmética simple entre dos números.

    Parámetros:
    - x: Primer número.
    - y: Segundo número.
    - precision: valor entero del numero de decimales a mostrar.
                 Por defecto, muestra un decimal   
    - operacion: "sumar" o "restar".
    - verbose: Si es True, imprime solo el resultado; si es False,
      imprime la operación completa.
    """
    if operacion == "sumar":
        resultado = x + y
        operador = "+"
    elif operacion == "restar":
        resultado = x - y
        operador = "-"
    elif operacion == "multiplicar":
        resultado = x * y
        operador = "*"
    elif operacion == "dividir":
        resultado = x / y
        operador = "/"
    else:
        # Cyclopts mostrará este error de forma adecuada en la CLI
        raise ValueError('La operación debe ser "sumar", "restar", "multiplicar" y "dividir".')

    resultado = round(resultado, ndigits=precision)

    if verbose:
        print(f"{x} {operador} {y} = {resultado}")
    else:
        print(f"{resultado}")


if __name__ == "__main__":
    cyclopts.run(main)
