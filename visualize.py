
from flask import Flask, render_template, json, request
site = Flask(__name__)
import my3d


@site.route('/')
def visualize():
    world = my3d.World()

    # pipe1 = my3d.Pipe(points=[[0, 0, 5], [5, 20, 20]])
    # pipe2 = my3d.Pipe(points=[[-30, -5, -50], [-20, -2, -20], [-5, 10, -10]], radius=3)
    # pipe3 = my3d.Pipe(points=[[-20, -3, -132], [-8, 32, 21]], radius=10)
    # world.add_entity([pipe1, pipe2, pipe3])
    # world.add_entity(my3d.Line([0, 0, 0], [10, 8, 6]))
    # world.add_entity(my3d.Sphere([5, -5, 10], radius=1))
    world.add_entity(my3d.Sphere([5, -5, 10], radius=3))

    world.add_entity(my3d.Point([7, 7, 7]))


    # breakpoint()
    return render_template('base_space.html', world=world)


if __name__ == '__main__':
    site.run(debug=True)
