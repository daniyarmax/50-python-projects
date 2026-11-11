"""Command-line calculator.

Evaluates arithmetic expressions such as:
    2 + 3 * (4 - 1)
    2 ** 8
    sqrt(16) + log10(1000)
    pi * 2

Expressions are parsed with the `ast` module and evaluated node by node,
so arbitrary Python code cannot be executed (unlike plain `eval`).

CODE EXPLAINED: https://chatgpt.com/c/6af1903e-6a6c-83eb-affc-d1d3907346e8
"""

import ast
import math
import operator as op


BINARY_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.FloorDiv: op.floordiv,
    ast.Mod: op.mod,
    ast.Pow: op.pow,
}

UNARY_OPERATORS = {
    ast.UAdd: op.pos,
    ast.USub: op.neg,
}

FUNCTIONS = {
    "sqrt": math.sqrt,
    "abs": abs,
    "round": round,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log,
    "log10": math.log10,
}

CONSTANTS = {
    "pi": math.pi,
    "e": math.e,
}

MAX_EXPONENT = 1000  # guards against huge powers such as 9 ** 9 ** 9


class CalculatorError(Exception):
    """Raised for any input the calculator cannot evaluate."""


def _eval_node(node):
    if isinstance(node, ast.Expression):
        return _eval_node(node.body)

    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.Name):
        if node.id in CONSTANTS:
            return CONSTANTS[node.id]
        raise CalculatorError(f"unknown name '{node.id}'")

    if isinstance(node, ast.BinOp) and type(node.op) in BINARY_OPERATORS:
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        if isinstance(node.op, ast.Pow) and abs(right) > MAX_EXPONENT:
            raise CalculatorError("exponent is too large")
        try:
            return BINARY_OPERATORS[type(node.op)](left, right)
        except ZeroDivisionError:
            raise CalculatorError("division by zero")

    if isinstance(node, ast.UnaryOp) and type(node.op) in UNARY_OPERATORS:
        return UNARY_OPERATORS[type(node.op)](_eval_node(node.operand))

    if (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in FUNCTIONS
    ):
        args = [_eval_node(arg) for arg in node.args]
        try:
            return FUNCTIONS[node.func.id](*args)
        except (ValueError, TypeError, OverflowError) as exc:
            raise CalculatorError(str(exc))

    raise CalculatorError("unsupported expression")


def evaluate(expression):
    """Safely evaluate a math expression string and return the number."""
    try:
        tree = ast.parse(expression.strip(), mode="eval")
    except SyntaxError:
        raise CalculatorError("invalid syntax")

    result = _eval_node(tree)
    if isinstance(result, complex):
        raise CalculatorError("result is a complex number")
    return result


def format_result(value):
    """Show whole-number floats without the trailing '.0'."""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    if isinstance(value, float):
        return f"{value:.10g}"
    return str(value)


def main():
    print("Simple Calculator")
    print("Examples: 2 + 3 * (4 - 1), 2 ** 8, sqrt(16), log10(1000), pi * 2")
    print("Type 'quit' to exit.\n")

    while True:
        try:
            text = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not text:
            continue
        if text.lower() in {"q", "quit", "exit"}:
            break

        try:
            print("=", format_result(evaluate(text)))
        except CalculatorError as exc:
            print("Error:", exc)


if __name__ == "__main__":
    main()