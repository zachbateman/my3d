'''
High-level module for handling the entire 3 dimensional world/space and all created entities.
'''
from . import entities
from .entities import Point, Line, TextPane, Pipe, Sphere
from typing import List

from flask import Flask, render_template, json, request
site = Flask(__name__)

@site.route('/')
def visualize(pipes=None):
    return render_template('base_space.html', pipes=pipes)


class World():
    def __init__(self, scale: float=1.0) -> None:
        self.entities = []

    @property
    def points(self):
        return [e for e in self.entities if isinstance(e, Point)]

    @property
    def lines(self):
        return [e for e in self.entities if isinstance(e, Line)]

    @property
    def text_panes(self):
        return [e for e in self.entities if isinstance(e, TextPane)]

    @property
    def pipes(self):
        return [e for e in self.entities if isinstance(e, Pipe)]

    @property
    def spheres(self):
        return [e for e in self.entities if isinstance(e, Sphere)]

    def add_entity(self, entity):  # : entities.Entity | List[entities.Entity]) -> None:
        if isinstance(entity, list):
            self.entities.extend(entity)
        else:
            self.entities.append(entity)

    def remove_entity(self, entity) -> None:
        ...

    def __add__(self, other_world):  # -> World:
        '''
        Combine self World with other_world to get composite world with all entities together.
        '''
        ...

    def generate_as_webpage(self) -> str:
        ...

    def save_as_webpage(self, filename: str='my3D Visualization.html'):
        with open(filename, 'w') as f:
            f.write(self.generate_as_webpage())
        print('Visualization saved to file!')

    def serve_local(self) -> None:
        '''
        Serve the 3D visualization locally on localhost:5000 using Flask
        '''
        site.run(debug=True)

