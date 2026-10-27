def ice_fractal_1(order: int, size: float) -> None:
    colors = ["#000000", "#d62828", "#f77f00", "#2a9d8f", "#1d6fd1", "#7b2cbf", "#e5338b", "#8d6e3f"]
    owner = getattr(ice_fractal_1, "top", None) is None
    if owner:
        ice_fractal_1.top = order

    if order == 0:
        t.forward(size)
        if owner:
            ice_fractal_1.top = None
        return

    ice_fractal_1(order - 1, size / 2)         

    x, y = t.position()
    h = t.heading()
    base = t.pencolor()
    for turn in (90, -90):
        if math.sin(math.radians(h + turn)) < -1e-9:  
            continue
        level = ice_fractal_1.top - order + 1              
        t.pencolor(colors[level % len(colors)])      
        t.setheading(h + turn)
        ice_fractal_1(order - 1, size / 4)         
        t.penup()                                   
        t.goto(x, y)
        t.setheading(h)
        t.pendown()
    t.pencolor(base)

    ice_fractal_1(order - 1, size / 2)            # вторая половина линии
    if owner:
        ice_fractal_1.top = None


def ice_fractal_2(order: int, size: float) -> None:
    colors = ["#000000", "#d62828", "#f77f00", "#2a9d8f", "#1d6fd1", "#7b2cbf", "#e5338b", "#8d6e3f"]
    owner = getattr(ice_fractal_2, "top", None) is None  
    if owner:
        ice_fractal_2.top = order

    if order == 0:
        t.forward(size)
        if owner:
            ice_fractal_2.top = None
        return

    ice_fractal_2(order - 1, size / 2)

    x, y = t.position()
    h = t.heading()
    base = t.pencolor()
    for turn in (60, 120, -60, -120):
        if math.sin(math.radians(h + turn)) < -1e-9:
            continue
        level = ice_fractal_2.top - order + 1
        t.pencolor(colors[level % len(colors)])
        t.setheading(h + turn)
        ice_fractal_2(order - 1, size / 4)
        t.penup()
        t.goto(x, y)
        t.setheading(h)
        t.pendown()
    t.pencolor(base)

    ice_fractal_2(order - 1, size / 2)     
    if owner:
        ice_fractal_2.top = None


def levy(order: int, size: float) -> None:
    rainbow = [
        "#9400D3",  # фиолетовый
        "#4B0082",  # индиго
        "#0000FF",  # синий
        "#00BFFF",  # голубой
        "#00FF00",  # зелёный
        "#FFFF00",  # жёлтый
        "#FF7F00",  # оранжевый
        "#FF0000"   # красный
    ]

    owner = getattr(levy, "top", None) is None
    if owner:
        levy.top = order
        levy.pos = 0
        levy.total = 2 ** order

    if order == 0:
        k = levy.pos * (len(rainbow) - 1) // max(1, levy.total - 1)
        t.pencolor(rainbow[k])
        t.forward(size)

        levy.pos += 1

        if owner:
            levy.top = None
        return

    t.left(45)
    levy(order - 1, size / math.sqrt(2))
    t.right(90)
    levy(order - 1, size / math.sqrt(2))
    t.left(45)

    if owner:
        levy.top = None


def dragon(order: int, size: float) -> None:
    rainbow = [
        "#9400D3",  # фиолетовый
        "#4B0082",  # индиго
        "#0000FF",  # синий
        "#00BFFF",  # голубой
        "#00FF00",  # зелёный
        "#FFFF00",  # жёлтый
        "#FF7F00",  # оранжевый
        "#FF0000"   # красный
    ]

    owner = getattr(dragon, "top", None) is None
    if owner:
        dragon.top = order
        dragon.pos = 0
        dragon.total = 2 ** order

    sign = 1 if size > 0 else -1
    length = abs(size)

    if order == 0:
        k = dragon.pos * (len(rainbow) - 1) // max(1, dragon.total - 1)
        t.pencolor(rainbow[k])
        t.forward(length)

        dragon.pos += 1

        if owner:
            dragon.top = None
        return

    t.left(45 * sign)
    dragon(order - 1, length / math.sqrt(2))
    t.right(90 * sign)
    dragon(order - 1, -length / math.sqrt(2))
    t.left(45 * sign)

    if owner:
        dragon.top = None
