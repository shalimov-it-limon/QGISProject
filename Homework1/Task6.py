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
