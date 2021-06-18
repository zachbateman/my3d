'''
Module containing various base 3D entities.  Any of these entities could be combined to form a composite entity.
'''



class Entity():

    def __init__(self) -> None:
        ...

    def assign_click_trigger(self) -> None:
        ...

    def assign_proximity_effect(self) -> None:
        ...

    





class Sphere(Entity):
    def __init__(self, radius: float=1.0) -> None:
        ...



class Pipe(Entity):
    def __init__(self, radius: float=1.0, points: list) -> None:
        ...


class Cuboid(Entity):
    def __init__(self, width: float=1.0, width: float=1.0, height: float=1.0) -> None:
        ...




