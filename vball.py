
from flask import Flask, render_template, json, request
site = Flask(__name__)
import my3d


ball_spot = (-30, 6, 4)
gravity = 0.05
ball_frame = 5

def move_ball(ball, velocity, frames, ground=False):
    global ball_spot, ball_frame, gravity
    for _ in range(frames):
        ball_spot = (ball_spot[0] + velocity[0], ball_spot[1] + velocity[1], ball_spot[2] + velocity[2])
        velocity = (velocity[0], velocity[1], velocity[2] - gravity)
        ball.change_position(ball_frame, ball_spot)
        ball_frame += 1
        if not ground:
            if ball_spot[2] < 3.5:
                break
        else:
            if ball_spot[2] < 0.8:
                break

@site.route('/')
def visualize():
    world = my3d.World(
        title='Volleyball',
        xyz_helper=False,
        controls='orbit',
        animation_frame_duration=0.05,
        frame_labels = [f'Frame: {x}' for x in range(251)],
        floor_size=90,
        floor_opacity=0.1,
        camera_position=(20, -20, 10))

    # court
    world.add_entity(my3d.Plane(points=[], length=60, width=30, color='0x777744'))

    world.add_entity(my3d.Pipe(points=[(30, -15, 0), (30, 15, 0)], radius=0.1))
    world.add_entity(my3d.Pipe(points=[(-30, 15, 0), (-30, -15, 0)], radius=0.1))
    world.add_entity(my3d.Pipe(points=[(30, -15, 0), (-30, -15, 0)], radius=0.1))
    world.add_entity(my3d.Pipe(points=[(30, 15, 0), (-30, 15, 0)], radius=0.1))

    # net
    world.add_entity(my3d.Pipe(points=[(0, -15, 0),(0, -15, 7.5)], radius=0.3))
    world.add_entity(my3d.Pipe(points=[(0, 15, 0),(0, 15, 7.5)], radius=0.3))

    net1 = my3d.Plane(points=[], length=1.5, width=30, color='0xdddddd')
    net1.change_rotationY(3, 90)
    net1.change_position(0, (0, 0, 6.75))
    world.add_entity(net1)

    net2 = my3d.Plane(points=[], length=1.5, width=30, color='0xdddddd')
    net2.change_rotationY(3, 90)
    net2.change_position(0, (0, 0, 5.25))
    world.add_entity(net2)



    ball = my3d.Sphere(ball_spot, radius=0.7)

    move_ball(ball, (0, 0, 0.8), 30)
    move_ball(ball, (1.3, -0.3, 0.7), 50)
    move_ball(ball, (-0.2, -0.1, 1.1), 80)
    move_ball(ball, (-0.05, 0.5, 1.0), 33)
    move_ball(ball, (-2.0, -1.2, -0.4), 50, ground=True)

    world.add_entity(ball)

    # test TextPane
    pane = my3d.TextPane('VICTORY!', center_point=(0, 0, 10), width=11, height=2, rotation=90, font_size=100)
    pane.change_visibility(0, False)
    pane.change_visibility(160, True)
    for i in range(161, 209):
        pane.change_rotationY(i, 3)
    world.add_entity(pane)


    return render_template('base_space.html', world=world)


if __name__ == '__main__':
    site.run(debug=True)
