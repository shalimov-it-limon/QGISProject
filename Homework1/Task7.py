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
