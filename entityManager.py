import dataStructures
from component import Component
from transform import Transform

class GameObject():
    def __init__(self, name, parent):
        self.name = name
        self.tags = []
        self.components = []
        self.children = []
        self.parent = parent

    def addComponent(self, component):
        self.components.append(component)
        component.gameObject = self

    def addChild(self, child):
        self.children.append(child)
        child.parent = self

    def removeChild(self, child):
        self.children.remove(child)
        child.parent = None
    
    def removeComponent(self, component):
        self.components.remove(component)

    def getComponent(self, component):
        for comp in self.components:
            if comp.__class__.__name__ == component:
                return comp
        return None

    def getComponentByName(self, name):
        for comp in self.components:
            if comp.name == name:
                return comp
        return None

class EntityTree():
    def __init__(self):
        self.root = GameObject("root", None)
        self.root.tags.append("root")

    def addEntity(self, entity, parent):
        if parent == None:
            self.root.children.append(GameObject(entity, self.root))
        else:
            parent.children.append(GameObject(entity, parent))
            entity.parent = parent