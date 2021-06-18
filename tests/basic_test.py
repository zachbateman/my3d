import unittest
import sys
sys.path.insert(1, '..')
import my3d


class Test3D(unittest.TestCase):

    def setUp(self):
        self.world = my3d.World()

    def add_spheres(self):
        spheres = [my3d.Sphere(radius=1), my3d.Sphere(radius=2), my3d.Sphere(radius=0.8), my3d.Sphere(radius=5)
        for sphere in spheres:
            self.world.add_entity(sphere)





if __name__ == '__main__':
    unittest.main(buffer=True)
