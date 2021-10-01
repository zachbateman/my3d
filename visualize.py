
from flask import Flask, render_template, json, request
site = Flask(__name__)
import my3d


@site.route('/')
def visualize():
    world = my3d.World(controls='orbit',
                               animation_frame_duration=0.1,
                               floor_size=150,
                               floor_opacity=0.15)

    pipe1 = my3d.Pipe(points=[[0, 0, 5], [5, 20, 20]])
    pipe2 = my3d.Pipe(points=[[-30, -5, -50], [-20, -2, -20], [-5, 10, -10]], radius=3)
    pipe3 = my3d.Pipe(points=[[-20, -3, -132], [-8, 32, 21]], radius=10)

    pipe3.change_visibility(8, False)
    pipe3.change_visibility(20, True)
    pipe3.change_color(30, 'orange')
    pipe3.change_color(50, 'white')
    pipe3.change_visibility(55, False)
    pipe3.change_visibility(70, True)

    pipe4 = my3d.Pipe(points=[(10, 3, 7), (18, 2, 10)], radius=0.3)

    world.add_entity([pipe1, pipe2, pipe3, pipe4])
    world.add_entity(my3d.Line([0, 0, 0], [10, 8, 6]))
    world.add_entity(my3d.Sphere([5, -5, 10], radius=1))
    world.add_entity(my3d.Sphere([5, -5, 10], radius=3))
    pane = my3d.TextPane('Text goes... HERE!  And here is additional following text...', center_point=[-8, -16, 10])
    pane.add_mouseover_effect('blue')
    pane.add_click_effect('spin')
    world.add_entity(pane)

    world.add_entity(my3d.Point([7, 7, 7]))

    for x in range(-20, 20, 2):
        for y in range(-20, 20, 2):
            for z in range(0, 6, 2):
                world.add_entity(my3d.Point((x, y, z), radius=0.1, opacity=0.2, fast=True))


    plane = my3d.Plane(points=[(), (), ()], length=30, width=10)
    world.add_entity(plane)

    return render_template('base_space.html', world=world)


if __name__ == '__main__':
    site.run(debug=True)
