import turtle as t
import math


ICE_COLORS = ["#000000", "#d62828", "#f77f00", "#2a9d8f",
              "#1d6fd1", "#7b2cbf", "#e5338b", "#8d6e3f"]


RAINBOW = ["#9400D3", "#4B0082", "#0000FF", "#00BFFF",
           "#00FF00", "#FFFF00", "#FF7F00", "#FF0000"]


levy_pos = 0
dragon_pos = 0


def ice_fractal_1(order, size, top=None):
    if top is None:
        top = order

    if order == 0:
        t.forward(size)
        return


    ice_fractal_1(order - 1, size / 2, top)


    x, y = t.position()
    h = t.heading()
    base = t.pencolor()


    for turn in (90, -90):
        if math.sin(math.radians(h + turn)) < -1e-9:
            continue


        level = top - order + 1
        t.pencolor(ICE_COLORS[level % len(ICE_COLORS)])
        t.setheading(h + turn)
        ice_fractal_1(order - 1, size / 4, top)


        t.penup()
        t.goto(x, y)
        t.setheading(h)
        t.pendown()


    t.pencolor(base)


    ice_fractal_1(order - 1, size / 2, top)


def ice_fractal_2(order, size, top=None):
    if top is None:
        top = order

    if order == 0:
        t.forward(size)
        return

    ice_fractal_2(order - 1, size / 2, top)

    x, y = t.position()
    h = t.heading()
    base = t.pencolor()

    for turn in (60, 120, -60, -120):
        if math.sin(math.radians(h + turn)) < -1e-9:
            continue

        level = top - order + 1
        t.pencolor(ICE_COLORS[level % len(ICE_COLORS)])
        t.setheading(h + turn)
        ice_fractal_2(order - 1, size / 4, top)

        t.penup()
        t.goto(x, y)
        t.setheading(h)
        t.pendown()

    t.pencolor(base)

    ice_fractal_2(order - 1, size / 2, top)


def levy(order, size, total=None):
    global levy_pos


    if total is None:
        total = 2 ** order
        levy_pos = 0

    if order == 0:
        k = levy_pos * (len(RAINBOW) - 1) // max(1, total - 1)
        t.pencolor(RAINBOW[k])
        t.forward(size)
        levy_pos += 1
        return

    t.left(45)
    levy(order - 1, size / math.sqrt(2), total)
    t.right(90)
    levy(order - 1, size / math.sqrt(2), total)
    t.left(45)


def dragon(order, size, total=None):
    global dragon_pos

    if total is None:
        total = 2 ** order
        dragon_pos = 0


    if size > 0:
        sign = 1
    else:
        sign = -1
    length = abs(size)

    if order == 0:
        k = dragon_pos * (len(RAINBOW) - 1) // max(1, total - 1)
        t.pencolor(RAINBOW[k])
        t.forward(length)
        dragon_pos += 1
        return

    t.left(45 * sign)
    dragon(order - 1, length / math.sqrt(2), total)
    t.right(90 * sign)
    dragon(order - 1, -length / math.sqrt(2), total)
    t.left(45 * sign)