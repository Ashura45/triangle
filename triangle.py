def triangle(sides):
    """Определяет тип треугольника по сторонам."""
    sides = sorted([int(side) for side in sides])  # Сортируем стороны по возрастанию

    if sides[0] + sides[1] <= sides[2]:  # Проверка существования треугольника
        return 'Такой треугольник не существует'

    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        return 'Прямоугольный'
    elif sides[0] == sides[1] == sides[2]:
        return 'Равносторонний'
    elif sides[0] != sides[1] != sides[2]:
        return 'Разносторонний'
    else:
        return 'Равнобедренный'

while True:
    # Пользовательский ввод
    user_input = input('Введите три положительных числа через пробел (или "N" для выхода): ')

    if user_input.upper() == 'N':  # Выход из программы
        print('Программа завершена.')
        break

    try:
        sides = user_input.split()
        if len(sides) != 3 or not all(side.isdigit() for side in sides):
            raise ValueError("Нужно ввести ровно три положительных числа!")

        # Вывод результата
        print(triangle(sides))
    except ValueError as e:
        print(f'Ошибка: {e}')