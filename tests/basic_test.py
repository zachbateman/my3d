import unittest
import sys
sys.path.insert(1, '..')
import my3d


class Test3D(unittest.TestCase):

    def setUp(self):
        self.world = my3d.World()


    def test_add_pipes(self):
        pipe1 = my3d.Pipe(points=[(0, 0, 5), (5, 20, 20)])
        self.world.add_entity(pipe1)
        pipe2 = my3d.Pipe(points=[(-30, -5, -50), (-20, -2, -20), (-5, 10, -10)], radius=3)
        self.world.add_entity(pipe2)

        self.world.serve_local()

    # def add_spheres(self):
        # spheres = [my3d.Sphere(radius=1), my3d.Sphere(radius=2), my3d.Sphere(radius=0.8), my3d.Sphere(radius=5)
        # for sphere in spheres:
            # self.world.add_entity(sphere)





if __name__ == '__main__':
    unittest.main(buffer=False)
