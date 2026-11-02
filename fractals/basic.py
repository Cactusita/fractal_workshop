import turtle as t


def draw_binary_tree(depth: int, size: float, angle: float) -> None:
    if depth == 0:
        t.forward(size)
        t.backward(size)
        return

    t.forward(size)
    t.right(angle)
    draw_binary_tree(depth - 1, size / 2, angle)
    t.left(2 * angle)
    draw_binary_tree(depth - 1, size / 2, angle)
    t.right(angle)
    t.backward(size)


def draw_branch(n: int, l: float) -> None:
    if n == 0:
        t.left(180)
        return

    x = l / (n + 1)

    for i in range(n):
        t.forward(x)
        t.left(45)
        draw_branch(n - i - 1, 0.5 * x * (n - i - 1))
        t.left(90)
        draw_branch(n - i - 1, 0.5 * x * (n - i - 1))
        t.right(135)

    t.forward(x)
    t.left(180)
    t.forward(l)



