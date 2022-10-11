# для создания иерархии классов плоаских геометрических фигур
# с базовым абстрактным классом, воспользуемся модулем, позволяющим
# воплощать абстрактные методы с помощью декоратора `abstractmethod`.
# ABC - Abstract Base Class.
from abc import ABC, abstractmethod


# вспомогательный класс для репрезентации двумерной точки
class Point2D:
    # этот метод - инициализатор, который вызывается при создании
    # экземпляра класса.
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


# абстрактный класс наследуется от ABC и нужен для того, чтобы
# задать общий интерфейс, необходимый всем наследующим его классам.
class Shape(ABC):
    # атрибут класса, который будет одинаковым для всех экземпляров.
    # с помощью аннотации типов, разработчик может указать свои
    # ОЖИДАНИЯ насчет того, какого типа должны быть переменная.
    # аннотация не гарантирует строгого соблюдения типов.
    amount: int = 0

    # именно наличие абстрактных методов запрещает интерпретатору
    # создавать экземпляры абстрактного класса. первый аргумент
    # метода всегда будет являться ссылккой на экземпляр класса.
    @abstractmethod
    def __init__(self, shape, pos: Point2D):
        # эти атрибуты будут уникальными для каждого экземпляра
        # класса, так как добавляются к экземпляру при его создании.
        self.shape = shape
        self.position = pos
        # а к атрибуту класса стоит обращаться по имени класса.
        Shape.amount += 1

    # так же как и атрибут, метод тоже может быть методом класса.
    # метод становится методом класса с помощью декоратора
    # `staticmethod`.  аннотировать тип можно и для значения,
    # возвращающего функцию.
    @staticmethod
    @abstractmethod  # последний (внутренний) в списке декораторов
    def about() -> str:
        return NotImplemented


# конкретному классу, наследуемому от абстрактного, необходимо
# переопределить все абстрактные методы базового класса.
class Circle(Shape):
    def __init__(self, pos: Point2D, radius: float):
        # вызываем инициализатор базового класса, с помощью встроенной
        # функции `super()`, позволяющей получить доступ к методам
        # базового класса.
        super().__init__('circle', pos)
        # это свойство будет только у экземпляров `Circle`.
        self.radius = radius

    @staticmethod
    def about() -> str:
        return 'Circle has no angles.'


# еще конкретный класс, унаследованный от `Shape`.
class Rectangle(Shape):
    def __init__(self, pos: Point2D, lo_left: Point2D, up_right: Point2D):
        super().__init__('rectangle', pos)
        self.lower_left = lo_left
        self.upper_right = up_right

    @staticmethod
    def about() -> str:
        return 'Rectangle has four angles.'


# класс, унаследованный от `Rectangle`.
class Cross(Rectangle):
    def __init__(self, pos: Point2D, lo_left_vertical: Point2D, up_right_vertical: Point2D, lo_left_horizontal: Point2D,
                 up_right_horizontal: Point2D):
        super().__init__(pos, lo_left_vertical, up_right_vertical)
        self.lower_left_vertical = lo_left_vertical
        self.upper_right_vertical = up_right_vertical
        self.lower_left_horizontal = lo_left_horizontal
        self.upper_right_horizontal = up_right_horizontal

    @staticmethod
    def about() -> str:
        return 'Cross has eight angles.'


class Tumbler(Circle):
    def __init__(self, pos_body: Point2D, radius_body: float, pos_head: Point2D, radius_head: float,
                 pos_left_arm: Point2D, radius_left_arm: float, pos_right_arm: Point2D, radius_right_arm: float):
        super().__init__(Point2D(pos_head.x, (pos_head.y - pos_body.y) / 2), radius=2 * radius_body + 2 * radius_head)
        self.radius_body = radius_body
        self.radius_head = radius_head
        self.radius_left_arm = radius_left_arm
        self.radius_right_arm = radius_right_arm
        self.pos_body = pos_body
        self.pos_head = pos_head
        self.pos_left_arm = pos_left_arm
        self.pos_right_arm = pos_right_arm

    @staticmethod
    def about() -> str:
        return 'Tumbler has no angles.'


# создадим список разных фигур - из 3 кругов и
#  3 прямоугольников.
shapes = list()

for n in range(1, 4):
    # для создания экземпляра класса, нужно обратиться
    # к объекту класса как к функции с аргументами, перечисленными
    # в инициализаторе `__init__()`.
    position = Point2D(n * 0.5, n * 1.5)
    shapes.append(Circle(position, n * 0.1))

for n in range(1, 4):
    position = Point2D(-n * 0.5, -n * 1.5)
    shapes.append(
        Rectangle(
            position,
            Point2D(position.x - (n * 0.5), position.y - (n * 0.5)),
            Point2D(position.x + (n * 0.5), position.y + (n * 0.5))
        ))

# статическое свойство теперь имеет значение 6
print(Shape.amount)

# приведет к ошибке, потому что Shape - абстрактный класс
shape = Shape('shape', Point2D(0, 0))

# общий интерфейс базового абстрактного класса `Shape` позволяет
# обращаться к атрибутам сущностей конкретных классов однаково.
for shape in shapes:
    print(shape.shape)
