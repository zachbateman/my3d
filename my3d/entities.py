'''
Module containing various base 3D entities.  Any of these entities could be combined to form a composite entity.
'''
import math


def convert_color(color):
    '''Specify specific colors for color names'''
    if color == 'green':
        return 0x22cc77
    elif color == 'blue':
        return 0x2277cc
    elif color == 'red':
        return 0x772211
    else:
        return color


class Entity():

    def __init__(self) -> None:
        self.mouseover_effects = []
        self.click_effects = []
        self.proximity_effects = []
        self.changes = []  # [(frame, change), (frame, change), ...]
        self.note = ''


    def add_mouseover_effect(self, effect) -> None:
        self.mouseover_effects.append(effect)

    def add_click_effect(self, effect) -> None:
        self.click_effects.append(effect)

    def add_proximity_effect(self) -> None:
        ...

    def change_color(self, change_frame: int, new_color: str):
        self.changes.append((change_frame if change_frame > 0 else 1, ('color', convert_color(new_color))))

    def change_visibility(self, change_frame: int, visible: bool):
        self.changes.append((change_frame if change_frame > 0 else 1, ('visibility', visible)))

    def change_position(self, change_frame: int, new_position):
        self.changes.append((change_frame if change_frame > 0 else 1, ('position', new_position)))

    def change_rotationX(self, change_frame: int, degrees: float):
        self.changes.append((change_frame if change_frame > 0 else 1, ('rotateX', math.radians(degrees))))

    def change_rotationY(self, change_frame: int, degrees: float):
        self.changes.append((change_frame if change_frame > 0 else 1, ('rotateY', math.radians(degrees))))

    def change_rotationZ(self, change_frame: int, degrees: float):
        self.changes.append((change_frame if change_frame > 0 else 1, ('rotateZ', math.radians(degrees))))





class Point(Entity):
    def __init__(self, point, color='green', radius=0.5, fast=False) -> None:
        super().__init__()
        self.point = point
        self.color = convert_color(color)
        self.radius = radius
        self.fast = 1 if fast else 0


class Line(Entity):
    def __init__(self, point1, point2, color='red', opacity: float=1.0) -> None:
        super().__init__()
        self.point1 = point1
        self.point2 = point2
        self.color = convert_color(color)
        self.opacity = opacity


class TextPane(Entity):
    def __init__(self, text: str='TextPane', center_point=(0, 0, 0), width: float=3, height: float=5, rotation: float=0, font_size=30):
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
        self.font_size = font_size


class Sphere(Entity):
    def __init__(self, location, radius: float=1.0, color='blue', opacity: float=1.0) -> None:
        super().__init__()
        self.location = location
        self.radius = radius
        self.color = convert_color(color)
        self.opacity = opacity


class Pipe(Entity):
    def __init__(self, points: list, radius: float=1.0, color='blue', opacity: float=1.0) -> None:
        super().__init__()
        self.points = points
        self.radius = radius
        self.color = convert_color(color)
        self.opacity = opacity
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
    # Todo: ability to specify plane from 3 3D points??
    # need 3 points to define a plane in 3D...
    # need to specify length and width...
    def __init__(self, length=20, width=10, color='blue'):
        super().__init__()
        self.length = length
        self.width = width
        self.color = convert_color(color)


class Cuboid(Entity):
    def __init__(self, width: float=1.0, height: float=1.0) -> None:
        super().__init__()
        ...




