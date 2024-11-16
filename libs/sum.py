
def add_integers(x: int, y: int) -> int:

    if not type(x) is int or not type(y) is int:
        raise TypeError("Arguments must be integers.")

    return x + y
