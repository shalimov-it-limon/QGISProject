# для создания иерархии классов плоаских геометрических фигур
# с базовым абстрактным классом, воспользуемся модулем, позволяющим
# воплощать абстрактные методы с помощью декоратора `abstractmethod`.
# ABC - Abstract Base Class.
from abc import ABC, abstractmethod

# Число Пи
Pi: float = 3.1415


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
        self.area = 0

    def get_area(self, *args, **kwargs):
        return self.get_area()

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
        global Pi
        super().__init__('circle', pos)
        # это свойство будет только у экземпляров `Circle`.
        self.radius = radius
        self.area = self.get_area(self.radius)

    @staticmethod
    def about() -> str:
        return 'Circle has no angles.'

    def get_area(self, radius) -> float:
        global Pi
        # Pi = super().Pi
        s: float = radius ** 2 * Pi
        return s

    def equal_area(self, _shape: Shape) -> bool:
        return self.area == _shape.area

    def interrsect(self, _shape: Shape)->bool:
        if _shape.shape == Circle:
            delta_pos = (abs(self.position.x-_shape.position.x)**2+abs(self.position.y-_shape.position.y)**2)**(0.5)
            return ((self.radius+_shape.radius)>delta_pos) and (delta_pos>(self.radius-_shape.radius))
        if _shape.shape == Rectangle:
            up_right_center_rast = (abs(self.position.x + (_shape.position.x+_shape.width/2))**2)+abs(abs(self.position.y-(_shape.position.y+_shape.height/2))**2)**(0.5)
            up_left_center_rast = (abs(self.position.x - (_shape.position.x + _shape.width / 2)) ** 2) + abs(
                abs(self.position.y + (_shape.position.y + _shape.height / 2)) ** 2) ** (0.5)
            down_right_center_rast = (abs(self.position.x + (_shape.position.x + _shape.width / 2)) ** 2) + abs(
                abs(self.position.y - (_shape.position.y + _shape.height / 2)) ** 2) ** (0.5)
            down_left_center_rast = (abs(self.position.x - (_shape.position.x + _shape.width / 2)) ** 2) + abs(
                abs(self.position.y - (_shape.position.y + _shape.height / 2)) ** 2) ** (0.5)
            return  (self.radius >up_right_center_rast)and(self.radius>up_left_center_rast)and(self.radius>down_right_center_rast)and(self.radius>down_left_center_rast)
# еще конкретный класс, унаследованный от `Shape`.
class Rectangle(Shape):
    def __init__(self, pos: Point2D, lo_left: Point2D, up_right: Point2D):
        super().__init__('rectangle', pos)
        self.lower_left = lo_left
        self.upper_right = up_right
        self.area = self.get_area(up_right.x, lo_left.y)

    @staticmethod
    def about() -> str:
        return 'Rectangle has four angles.'


    def get_area(self, height: float, width: float, *args, **kwargs) -> float:
        width = abs(self.lower_left.x - self.upper_right.x)
        height = abs(self.lower_left.y - self.upper_right.y)
        s: float = height * width
        return s

    def equal_area_rectangle(self, _shape: Shape) -> bool:
        return self.area == _shape.area



# класс, унаследованный от `Rectangle`.
class Cross(Rectangle):
    def __init__(self, pos: Point2D, lo_left_vertical: Point2D, up_right_vertical: Point2D, lo_left_horizontal: Point2D,
                 up_right_horizontal: Point2D):
        super().__init__(pos, lo_left_vertical, up_right_vertical)
        self.lower_left_vertical = lo_left_vertical
        self.upper_right_vertical = up_right_vertical
        self.lower_left_horizontal = lo_left_horizontal
        self.upper_right_horizontal = up_right_horizontal
        self.area = self.get_cross_area(abs(up_right_vertical.y - lo_left_vertical.y),
                                        abs(up_right_horizontal.y - lo_left_horizontal.y),
                                        abs(lo_left_vertical.x - up_right_vertical.x),
                                        abs(up_right_horizontal.x - lo_left_horizontal.x))

    @staticmethod
    def about() -> str:
        return 'Cross has eight angles.'


    def get_cross_area(self, height_vert: float, height_hor: float, width_vert: float, width_hor: float) -> float:
        area_vert = super().get_area(height_vert, width_vert)
        area_hor = super().get_area(height_hor, width_hor)
        area_center = super().get_area(height_vert - height_hor, width_hor - width_vert)
        s = area_hor + area_vert - area_center
        return s

    def equal_area_cross(self,_shape: Shape)->bool:
        return self.area == _shape.area


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
        self.area = self.get_tumbler_area(self.pos_body, self.radius_body, self.pos_head, self.radius_head,
                                          self.pos_left_arm, self.radius_left_arm, self.pos_right_arm,
                                          self.radius_right_arm)

    @staticmethod
    def about() -> str:
        return 'Tumbler has no angles.'

    def get_tumbler_area(self, pos_body, radius_body: float, pos_head, radius_head: float, pos_left_arm,
                         radius_left_arm: float, pos_right_arm, radius_right_arm: float):
        body = Circle(pos_body, radius_body)
        area_body = body.get_area(radius_body)
        head = Circle(pos_head, radius_head)
        area_head = head.get_area(radius_head)
        left_arm = Circle(pos_left_arm, radius_left_arm)
        area_left_arm = left_arm.get_area(radius_left_arm)
        right_arm = Circle(pos_right_arm, radius_right_arm)
        area_right_arm = right_arm.get_area(radius_right_arm)
        s = area_body + area_head + area_left_arm + area_right_arm
        return s

    def equal_area_tubler(self,_shape: Shape)-> bool:
        return  self.area == _shape.area




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
# shape = Shape('shape', Point2D(0, 0))


shapes.append(Cross(pos=Point2D(0, 0), lo_left_vertical=Point2D(-2, -10), up_right_vertical=Point2D(2, 10),
                    lo_left_horizontal=Point2D(-10, -2), up_right_horizontal=Point2D(10, 2)))
# cross
print(shapes[-1])

shapes.append(Tumbler(pos_body=Point2D(0, -10), radius_body=10, pos_head=Point2D(0, 5), radius_head=5,
                      pos_left_arm=Point2D(-(24 ** (0.5)), 0), radius_left_arm=2,
                      pos_right_arm=Point2D((24 ** (0.5)), 0), radius_right_arm=2))
# tubler
print(shapes[-1])
# общий интерфейс базового абстрактного класса `Shape` позволяет
# обращаться к атрибутам сущностей конкретных классов однаково.
for shape in shapes:
    print(shape.shape)
