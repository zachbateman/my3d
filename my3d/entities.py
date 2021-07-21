'''
Module containing various base 3D entities.  Any of these entities could be combined to form a composite entity.
'''
import math



class Entity():

    def __init__(self) -> None:
        ...

    def assign_click_trigger(self) -> None:
        ...

    def assign_proximity_effect(self) -> None:
        ...




class Point(Entity):
    def __init__(self, point, color='blue', alpha: float=1.0) -> None:
        self.point = point
        self.color = color
        self.alpha = alpha


class Line(Entity):
    def __init__(self, point1, point2, color='red') -> None:
        self.point1 = point1
        self.point2 = point2
        self.color = color


class TextPane(Entity):
    def __init__(self, text: str='TextPane', center_point=(0, 0, 0), width: int=3, height: int=5, rotation: float=0):
        self.text = text
        words = text.split(' ')
        lines = []
        while words:
            new_line = ''
            while len(new_line) < (10 * width) and words:
                new_line += f' {words[0]}'
                words = words[1:]
            lines.append(new_line)
        self.text_lines = lines

        self.center_point = center_point
        self.width = width
        self.height = height
        self.rotation = rotation * math.pi / 180  # given in angles; convert to radians for THREE.js


class Sphere(Entity):
    def __init__(self, location, radius: float=1.0) -> None:
        self.location = location
        self.radius = radius


class Pipe(Entity):
    def __init__(self, points: list, radius: float=1.0) -> None:
        self.points = points
        self.radius = radius

    @property
    def end_to_end_length(self):
        return math.dist(self.points[0], self.points[-1])

    @property
    def segments(self):
        return int(5 + self.end_to_end_length / 5)


class Cuboid(Entity):
    def __init__(self, width: float=1.0, height: float=1.0) -> None:
        ...




