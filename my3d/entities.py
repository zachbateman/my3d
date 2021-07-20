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




