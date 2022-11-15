import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from scipy.signal import savgol_filter


"""numpy"""
# 1. создайте массив случайных чисел с плавающей точкой от 0 до 1 размером 10х10 и
# найдите минимальное и максимальное
print('###########################################1###################################################')
random_array = np.random.uniform(low=0.0, high=1.0, size=[10, 10])
print('массив случайных чисел с плавающей точкой')
print(random_array)

maximum = random_array.max()
minimum = random_array.min()

print('Максимальное число: ' + str(maximum))
print('минимальное число: ' + str(minimum))

print('###########################################2###################################################')

# 2. выполните сортировку всех значений массива от большего к меньшему и выведите их в
# консоль в виде простой последовательности

sorted_array = np.sort(random_array, kind='quicksort')
print(sorted_array)
print('###########################################3###################################################')
# 3. вычтите из значений массива средние значения по столбцам (np.mean).
sorted_array = sorted_array - np.mean(sorted_array)

print(sorted_array)
print('###########################################4###################################################')
"""numpy & matplotlib"""

# 4. постройте график функции y = tanh(x)
ordinate = []
abscis = np.arange(start=0, stop=10, step=0.1)
for x in abscis:
    ordinate.append(np.tanh(x))

def plot_signal(time, values, xlim=10, ylim=2, xlog=False, ylog=False):
    # метод возвращает ссылку на единственный график (объект `Axes`),
    # который будет содержаться в области отрисовки (объект `Figure`).
    # с помощью метода `subplots` можно получить ссылки на несколько
    # объектов `Axes`, если нужно разместить на рисунке несколько графиков.
    axes = plt.subplot()
    plt.title("График функции y = tanh(x)")  # заголовок
    plt.xlabel("x")  # ось абсцисс
    plt.ylabel("y")  # ось ординат
    # `Axes` обладает множеством методов для настройки шрифтов, подписей
    # осей, выбора цены деления и прочего.
    axes.tick_params(labelsize=10)
    axes.grid(True, which='both')

    if xlim:
        axes.set_xlim(xlim)
    if ylim:
        axes.set_ylim(ylim)
    if xlog:
        axes.set_xscale('log')
    if ylog:
        axes.set_yscale('log')

    # метод `plot` строит график в виде линии.  другие методы (такие
    # как `scatter`, `loglog`, `hist` и др.) позволяют строить другие
    # всевозможные типы диаграмм, растровых и контурных
    # карт (не географических).
    axes.plot(time, values)
    # для вывода на экран в отдельном окне.  этого не требуется
    # при работе в Jupyter Notebooks.
    plt.show()


plot_signal(abscis, ordinate, ylim=1)  # , xlog=True, ylog=True)

print('###########################################5###################################################')
# создайте объект типа Figure и разместите на нем два объекта типа Axes (друг под
# другом), которые будут содержать 1) простую гистограмму распределения значений
# массива случайных чисел из предыдущего примера (matplotlib.pyplot.hist) и
# 2) растровое 2D изображение этого массива (matplotlib.pyplot.inshow)
fig, axes = plt.subplots(2,1,figsize = (8,8))
ax = axes[0]
ax.hist(random_array, bins = 30, density = True, histtype = 'step', label = 'C1')
ax = axes[1]
_ = np.linspace(-1,1,100)
x =random_array[0,:]
y =random_array[:,1]
x,y =np.meshgrid(x,y)
z = 1
ax.plot.contourf(x,y,z)
plt.show()
