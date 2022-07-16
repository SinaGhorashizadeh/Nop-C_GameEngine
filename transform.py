from component import Component

class Transform(Component):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.enabled = True

    def update(self):
        pass
    
    