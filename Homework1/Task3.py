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
