from component import Component
from pygame import image as pygameImage
from pygame import transform as pygameTransform

class SpriteRenderer(Component):
    def __init__(self, gameObject, spritePath):
        self.gameObject = gameObject
        self.transform = self.gameObject.getComponent("Transform")
        self.sprite = pygameImage.load(spritePath)
        self.scaleImage(self.transform.width, self.transform.height)
        self.enabled = True
    
    def scaleImage(self, width, height):
        self.sprite = pygameTransform.scale(self.sprite, (width, height))

    def update(self):
        pass

        
    