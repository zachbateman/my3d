'''
High-level module for handling the entire 3 dimensional world/space and all created entities.
'''
import os
import webbrowser
from . import entities
from .entities import Entity, Point, Line, TextPane, Pipe, Sphere, Plane
from typing import List

from flask import Flask, render_template, json, request

template_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'templates')
print(template_folder)

site = Flask(__name__, template_folder=template_folder)


WORLD = None
@site.route('/')
def visualize(pipes=None):
    return render_template('base_space.html', world=WORLD)


class World():
    def __init__(self,
        title: str='My3D',
        scale: float=1.0,
        xyz_helper: bool=False,
        background_particles: bool=False,
        controls: str='orbit',
        total_animation_frames: int=100,
        animation_frame_duration: float=0.1,
        frame_labels: list=[],
        floor_size: int=300,
        floor_opacity: float=0.25,
        camera_position: tuple=(0, -30, 12)) -> None:
        '''
        TODO: controls kwarg can be one of 'orbit', 'first_person', or 'fly'
        '''
        self.title = title
        self.entities = []
        self.xyz_helper = xyz_helper
        if xyz_helper:
            panes = [
                TextPane('X', center_point=(1, 0, 0.3), width=0.5, height=0.5),
                TextPane('Y', center_point=(0, 1, 0.3), width=0.5, height=0.5),
                TextPane('Z', center_point=(0, 0, 1.3), width=0.5, height=0.5),
                ]
            for pane in panes:
                pane.add_click_effect('spin')
                self.add_entity(pane)

        self.background_particles = background_particles
        self.controls = controls
        self.total_animation_frames = total_animation_frames
        self.animation_frame_duration = animation_frame_duration
        self.frame_labels = frame_labels  # display in top right corner; index of list = frame number
        self.floor_size = floor_size
        self.floor_opacity = floor_opacity
        self.camera_x, self.camera_y, self.camera_z = camera_position


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

    @property
    def planes(self):
        return [e for e in self.entities if isinstance(e, Plane)]

    def add_entity(self, *entities):  # : entities.Entity | Iterable[entities.Entity]) -> None:
        for entity in entities:
            if isinstance(entity, Entity):
                self.entities.append(entity)
            else:
                for inner_entity in entity:  # if "entity" is say a list
                    self.entities.append(inner_entity)

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
        global WORLD
        WORLD = self
        webbrowser.open('http://127.0.0.1:5000/')
        site.run(debug=True)
