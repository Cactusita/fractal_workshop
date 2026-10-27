"""Роль 1: базовые рекурсивные фракталы — двоичное дерево и «Ветка».

Правила модуля:
* draw_* только рисуют: черепашка всегда возвращается в исходную точку
  и направление. Параметры сюда передаёт меню (main.py), input() здесь нет.
* run_* — обёртки для меню: рисуют и возвращают управление.
"""
import turtle

START_POS = (0, -250)  # начальная позиция (внизу экрана)
t = turtle.Turtle()
t.left(90)
t.speed(0)


def draw_binary_tree(depth: int, size: float, angle: float) -> None:
    """Двоичное дерево.

    depth — глубина рекурсии, size — длина ствола, angle — угол в градусах.
    """

    if depth == 0:
        t.forward(size)
        t.backward(size)
        return

    t.forward(size)  # ствол
    t.right(angle)
    draw_binary_tree(depth - 1, size / 2, angle)  # правая ветвь
    t.left(2 * angle)
    draw_binary_tree(depth - 1, size / 2, angle)  # левая ветвь
    t.right(angle)  # исходное направление
    t.backward(size)  # назад к началу


def _branch(l: float, n: int) -> None:
    """Рекурсивная часть «Ветки» (из второго кода).

    После вызова черепашка стоит в начальной точке, но смотрит
    в противоположную сторону (на этом построена сама рекурсия).
    """
    if n == 0:
        t.left(180)
        return

    x = l / (n + 1)  # длина одного участка ствола

    for i in range(n):
        t.forward(x)
        t.left(45)
        _branch(0.5 * x * (n - i - 1), n - i - 1)  # левая веточка
        t.left(90)
        _branch(0.5 * x * (n - i - 1), n - i - 1)  # правая веточка
        t.right(135)

    t.forward(x)
    t.left(180)
    t.forward(l)  # вернулись в начало


def draw_branch(n: int, size: float) -> None:
    """Фрактал «Ветка»: n — глубина, size — длина ствола.

    В конце разворачиваем черепашку обратно, чтобы она смотрела
    в исходном направлении, как у draw_binary_tree.
    """
    _branch(size, n)
    t.left(180)


def run_binary_tree():
    draw_binary_tree(depth=8, size=100.0, angle=30)


def run_branch():
    draw_branch(n=5, size=200.0)


# Что рисовать при запуске: оставьте одну строку
run_branch()
# run_binary_tree()

turtle.done()