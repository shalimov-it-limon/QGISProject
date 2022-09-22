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
