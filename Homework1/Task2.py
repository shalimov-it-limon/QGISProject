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
