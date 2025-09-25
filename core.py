import math
from enum import Enum

class Operation(str, Enum):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"
    POW = "^"

def calculate(a: float, b: float, operation: Operation) -> float:
        if operation == Operation.ADD:
            return a + b
        elif operation == Operation.SUB:
            return a - b
        elif operation == Operation.MUL:
            return a * b
        elif operation == Operation.DIV:
            if b == 0:
                raise ZeroDivisionError("На ноль делить нельзя")
            return a / b
        else:
            return math.pow(a, b)

def parse_operation(symbol: str) -> Operation:
    operation = None
    try:
        operation = Operation(symbol)
        return operation
    except ValueError:
        print("Введена недоступная операция")
        raise