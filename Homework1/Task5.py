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
