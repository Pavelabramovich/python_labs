def operation(x: float, y: float, opr: str):
    match opr:
        case "add":
            return x + y
        case "sub":
            return x - y
        case "mult":
            return x * y
        case "div":
            if y == 0:
                raise ZeroDivisionError
            return x / y
        case _:
            raise NotImplementedError





