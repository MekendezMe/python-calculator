import core
from core import Operation


def calculator() -> float:
    a = 0
    b = 0
    try:
        a = float(input("Введите первое число\n"))
        b = float(input("Введите второе число\n"))
    except ValueError:
        print("Введено некорректное число")
        raise

    symbol = input("Введите одну из доступных операций: + - * / ^\n")

    operation = core.parse_operation(symbol=symbol)

    return core.calculate(a, b, operation)

while True:
    print(calculator())
