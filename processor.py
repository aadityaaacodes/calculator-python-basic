import operator as op
import json


def calculate(datum):
    opr = datum['operator']
    result = datum["result"]
    inp = datum["input_value"]

    try:
        if opr == '+':
            result = float(result) + float(inp)
        elif opr == '-':
            result = float(result) - float(inp)
        elif opr == '*':
            result = float(result) * float(inp)
        elif opr == '/':
            result = float(result) / float(inp)
        else:
            raise ValueError("Invalid operator")

        return result
    except ValueError as e:
        return str(0)
