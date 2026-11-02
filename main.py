import turtle

from fractals.basic import draw_binary_tree, draw_branch
from fractals.koch import koch, koch_snowflake, minkowski
from fractals.complex import ice_fractal_1, ice_fractal_2, levy, dragon


def show_menu() -> None:
    print("\n=== ФРАКТАЛЬНАЯ МАСТЕРСКАЯ ===")
    print("1. Двоичное дерево")
    print("2. Фрактал 'Ветка'")
    print("3. Кривая Коха")
    print("4. Снежинка Коха")
    print("5. Кривая Минковского")
    print("6. Ледяной фрактал №1")
    print("7. Ледяной фрактал №2")
    print("8. Кривая Леви")
    print("9. Дракон Хартера-Хейтуэя")
    print("10. Выход")


def ask_number(text, kind=float, min_v=None, max_v=None):
    """Спрашивает число, пока не введут корректное значение."""
    while True:
        try:
            value = kind(input(text))
        except ValueError:
            print("Нужно ввести число.")
            continue
        if min_v is not None and value < min_v:
            print(f"Значение не меньше {min_v}.")
        elif max_v is not None and value > max_v:
            print(f"Значение не больше {max_v}.")
        else:
            return value


def prepare(x=0, y=0, heading=0) -> None:
    """Очищает экран и ставит черепашку в начальную точку."""
    turtle.reset()
    turtle.speed(0)
    turtle.hideturtle()
    turtle.up()
    turtle.goto(x, y)
    turtle.setheading(heading)
    turtle.down()


def run_tree() -> None:
    depth = ask_number("Глубина (1-10): ", int, 1, 10)
    angle = ask_number("Угол (0-90): ", float, 0, 90)
    size = ask_number("Начальный размер: ", float, 1)
    prepare(0, -250, 90)
    draw_binary_tree(depth, size, angle)


def run_branch() -> None:
    n = ask_number("Глубина (1-8): ", int, 1, 8)
    size = ask_number("Размер: ", float, 1)
    prepare(0, -250, 90)
    draw_branch(n, size)


def run_curve(func, name: str, max_order: int = 6) -> None:
    """Общий запуск для кривых вида func(order, size), которые идут вправо."""
    order = ask_number(f"Глубина (0-{max_order}): ", int, 0, max_order)
    size = ask_number("Длина стороны: ", float, 1)
    prepare(-size / 2, 0, 0)
    func(order, size)


def run_snowflake() -> None:
    order = ask_number("Глубина (0-6): ", int, 0, 6)
    size = ask_number("Длина стороны: ", float, 1)
    prepare(-size / 2, size * 3 ** 0.5 / 6, 0)
    koch_snowflake(order, size)


def main() -> None:
    actions = {
        "1": run_tree,
        "2": run_branch,
        "3": lambda: run_curve(koch, "Кривая Коха"),
        "4": run_snowflake,
        "5": lambda: run_curve(minkowski, "Кривая Минковского", 4),
        "6": lambda: run_curve(ice_fractal_1, "Ледяной фрактал №1"),
        "7": lambda: run_curve(ice_fractal_2, "Ледяной фрактал №2"),
        "8": lambda: run_curve(levy, "Кривая Леви", 12),
        "9": lambda: run_curve(dragon, "Дракон", 12),
    }
    while True:
        show_menu()
        choice = input("Выберите пункт меню: ").strip()
        if choice == "10":
            break
        action = actions.get(choice)
        if action is None:
            print("Нет такого пункта.")
        else:
            action()
    turtle.bye()


if __name__ == "__main__":
    main()