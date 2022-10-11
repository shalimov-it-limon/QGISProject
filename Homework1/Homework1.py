def Task1():
    """
    Создайте скрипт, печатающий все нечетные числа из списка и
    прекращающий это делать, если встретится число, большее или
    равное 237.
    """

    def is_odd(number):
        """
        Определение нечётности числа
        :param number: исходное число
        :return: True, если число нечётное, False, если число чётное
        """
        if number % 2 == 0:
            return False
        else:
            return True

    numbers = [
        386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328,
        615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248,
        866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894,
        767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 743, 527
    ]

    def task_1(numbers):
        """
        Печать всех нечетных чисел из списка, прекращающий это делать, если встретится число, большее или равное 237.
        :param numbers: исходный список чисел
        """
        for num in numbers:
            if is_odd(num):
                if num < 237:
                    print(str(num) + ' ')
                else:
                    return

    task_1(numbers)


def Task2():
    """
    Создайте скрипт, который объединит элементы списка в строку
    """

    letters = ['Q', 'G', 'I', 'S', ' ', 'i', 's', ' ', 'a', 'w', 'e', 's',
               'o', 'm', 'e', '!']
    phrase = ""

    def phrase_from_letters(letters, phrase):
        """
        Объединение элементов списка в строку
        :param letters: список символов
        :param phrase: итоговая строка
        :return: строка, собранная из элементов списка
        """
        for letter in letters:
            phrase = phrase + letter
        return phrase

    print(phrase_from_letters(letters, phrase))


def Task3():
    """
    Создайте скрипт, печатающий из списка названия плоских
    геометрических фигур, имеющих углы.
    """

    shapes = ['circle', 'hexagon', 'pentagon', 'ellipse', 'triangle', 'rectangle', 'line']

    def print_shapes_with_angles(shapes):
        """
        Печать названий фигур из списка , имеющих углы.
        :param shapes: список плоских геометрических фигур
        """
        for shape in shapes:
            if (shape.find('angle') > 0) or (shape.find('agon') > 0):
                print(shape + ' ')

    print_shapes_with_angles(shapes)


def Task4():
    """
    Измените скрипт из предыдущего задания так, чтобы он печатал
    фигуры, не имеющие углы.
    """

    shapes = ['circle', 'hexagon', 'pentagon', 'ellipse', 'triangle', 'rectangle', 'line']

    def print_shapes_with_angles(shapes):
        """
        Печать названий фигур из списка , не имеющих углы.
        :param shapes: список плоских геометрических фигур
        """
        for shape in shapes:
            if not ((shape.find('angle') > 0) or (shape.find('agon') > 0)):
                print(shape + ' ')

    print_shapes_with_angles(shapes)


def Task5():
    """
    Создайте скрипт, подсчитывающий количество строк в списке,
    длиннее 5 символов.
    """

    cities = ['Wien', 'Perm', 'Oxford', 'Paris', 'Novosibirsk', 'Bern', 'Rio', 'Washington']
    amount = 0

    def count_number_of_words(list, amount):
        """
        Подсчет количество строк, длиннее 5 символов в списке
        :param list: исходный список
        :param amount: переменная для хранения количества слов
        :return: количество строк ,длиннее 5 символов в списке.
        """
        for word in list:
            if len(word) > 5:
                amount += 1
        return amount

    print(count_number_of_words(cities, amount))


def Task6():
    """
    Измените скрипт из предыдущего задания так, чтобы он добавлял
    новый элементы в словарь, содержащий название города в качестве
    ключа и длину его названия в качестве значения.
    """

    cities = ['Wien', 'Perm', 'Oxford', 'Paris', 'Novosibirsk', 'Bern',
              'Rio', 'Washington']
    amount = 0
    dictionary = dict.fromkeys(cities)
    for city in cities:
        dictionary[city] = len(city)

    def add_city_in_dict(city, dict):
        """
        Добавление наименования города в соловарь
        :param city: наименование города
        :param dict: словарь, содержащий название города в качестве ключа и длину его названия в качестве значения.
        """
        new_dict = {city: len(city)}
        dict.update(new_dict)

    add_city_in_dict('Krasnokamsk', dictionary)

    print(dictionary)


def Task7():
    """
    Создайте скрипт, подсчитывающий, сколько раз каждый символ
    встречается в строке. Результат должен быть сохранен в словарь,
    где ключи — символы, значения — встречаемость.
    """

    dictionary = {}

    def count_letter_amount(string, dict):
        """
        Подсчёт того, сколько раз каждый символ встречается в строке
        :param string: исходная строка
        :param dict: итоговый словарь
        :return: словарь,где ключи — символы, значения — встречаемость.
        """
        for symbol in string:
            if symbol in dict.keys():
                amount = dict[symbol]
                amount += 1
                dict[symbol] = amount
            else:
                new_dict = {symbol: 1}
                dict.update(new_dict)
        print(dict)

    str = "съешь ещё этих мягких французских булок, да выпей чаю"
    count_letter_amount(str, dictionary)


def Task8():
    """
    Создайте с помощью скрипта список из 5 списков по 5 элементов
    с числом 10 (двумерный массив 5х5), значения в котором
    умножаются на сумму его индексов. Выведите список в виде
    таблицы
    """

    def generate_list(dim):
        """
        Формирования списка из списков
        :param dim: размерность списка
        :return: двумерный массив (max)х(max)
        """
        result_list = [[]]
        for i in range(dim):
            list = [num * 10 + i * 10 for num in range(dim)]
            result_list.insert(i, list)
        return result_list

    def print_list(dim):
        """
        Печать списка из списков
        :param dim: размерность списка
        :return: печать двумерного массива (max)х(max)
        """
        for i in range(dim):
            string = ""
            for j in range(dim + 1):
                if j < dim:
                    string = string + " " + str(generate_list(dim)[i][j])
                else:
                    print(string)

    print_list(5)
