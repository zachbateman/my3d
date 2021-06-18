'''
High-level module for handling the entire 3 dimensional world/space and all created entities.
'''



class World()

    def __int__(self, scale: float=1.0) -> None:
        ...

    def add_entity(self, entity) -> None:
        ...

    def remove_entity(self, entity) -> None:
        ...

    def __add__(self, other_world) -> World:
        '''
        Combine self World with other_world to get composite world with all entities together.
        '''
        ...

    def generate_as_webpage(self) -> str:
        ...

    def save_as_webpage(self, filename: str='my3D Visualization.html'):
        with open(filename, 'w') as f:
            f.write(self.generate_as_webpage())
        print(Visualization saved to file!')

    def serve_local(self) -> None:
        '''
        Serve the 3D visualization locally on localhost:5000 using Flask
        '''
        ...
