'''
Module containing various base 3D entities.  Any of these entities could be combined to form a composite entity.
'''
import math



class Entity():

    def __init__(self) -> None:
        self.mouseover_effects = []
        self.click_effects = []
        self.proximity_effects = []
        self.changes = []  # [(frame, change), (frame, change), ...]

    def add_mouseover_effect(self, effect) -> None:
        self.mouseover_effects.append(effect)

    def add_click_effect(self, effect) -> None:
        self.click_effects.append(effect)

    def add_proximity_effect(self) -> None:
        ...

    def change_color(self, change_frame: int, new_color: str):
        self.changes.append((change_frame, ('color', new_color)))

    def change_visibility(self, change_frame: int, visible: bool):
        self.changes.append((change_frame, ('visibility', visible)))

    def change_position(self, change_frame: int, new_position):
        self.changes.append((change_frame, ('position', new_position)))

    def change_rotationX(self, change_frame: int, degrees: float):
        self.changes.append((change_frame, ('rotateX', math.radians(degrees))))

    def change_rotationY(self, change_frame: int, degrees: float):
        self.changes.append((change_frame, ('rotateY', math.radians(degrees))))

    def change_rotationZ(self, change_frame: int, degrees: float):
        self.changes.append((change_frame, ('rotateZ', math.radians(degrees))))





class Point(Entity):
    def __init__(self, point, color='green', opacity: float=0.7, radius=0.5, fast=False) -> None:
        super().__init__()
        self.point = point
        self.color = color
        self.opacity = opacity
        self.radius = radius
        self.fast = 1 if fast else 0


class Line(Entity):
    def __init__(self, point1, point2, color='red') -> None:
        super().__init__()
        self.point1 = point1
        self.point2 = point2
        self.color = color


class TextPane(Entity):
    def __init__(self, text: str='TextPane', center_point=(0, 0, 0), width: float=3, height: float=5, rotation: float=0):
        super().__init__()
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
        super().__init__()
        self.location = location
        self.radius = radius


class Pipe(Entity):
    def __init__(self, points: list, radius: float=1.0) -> None:
        super().__init__()
        self.points = points
        self.radius = radius
        self.segments = int(5 + self.end_to_end_length / 5)

    @property
    def end_to_end_length(self):
        # return math.dist(self.points[0], self.points[-1])  # Python 3.8+...
        p1, p2 = self.points[0], self.points[-1]
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)**0.5

    # @property
    # def segments(self):
        # return int(5 + self.end_to_end_length / 5)


class Plane(Entity):
    # need 3 points to define a plane in 3D...
    # need to specify length and width...
    def __init__(self, points, length=20, width=10, color='blue'):
        super().__init__()
        # points is to be a sequence of 3 separate (x, y, z) points
        # these three points define a plane
        self.points = points
        self.length = length
        self.width = width
        self.color = color


class Cuboid(Entity):
    def __init__(self, width: float=1.0, height: float=1.0) -> None:
        super().__init__()
        ...




