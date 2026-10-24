import turtle as t


def koch(order: int, size: float) -> None:
    if order == 0:
        t.forward(size)
        return
    if order == 1:
        koch(order - 1, size/3)
        t.left(60)
        koch(order - 1, size/3)
        t.right(120)
        koch(order - 1, size/3)
        t.left(60)
        koch(order - 1, size/3)
        return
    koch(order - 1, size/3)
    t.left(60)
    koch(order - 1, size/3)
    t.right(120)
    koch(order - 1, size/3)
    t.left(60)
    koch(order - 1, size/3)


def koch_snowflake(order: int, size: float) -> None:
    for _ in range(3):
        koch(order, size)
        t.right(120)
def minkowski(order, size):
    if order == 0:
        t.forward(size)
        return
    s = size / 4
    minkowski(order - 1, s)
    t.left(90)
    minkowski(order - 1, s)
    t.right(90)
    minkowski(order - 1, s)
    t.right(90)
    minkowski(order - 1, s)
    minkowski(order - 1, s)
    t.left(90)
    minkowski(order - 1, s)
    t.left(90)
    minkowski(order - 1, s)
    t.right(90)
    minkowski(order - 1, s)
minkowski(3, 500)
t.done()