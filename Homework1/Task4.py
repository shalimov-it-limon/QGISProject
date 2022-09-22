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
