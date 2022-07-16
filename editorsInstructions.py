import entityManager
import transform
import spriteRenderer

#tell the engine to load the editor
def openLetter():
    entityTree = entityManager.EntityTree()
    entityTree.addEntity("player", None)
    entityTree.root.children[0].addComponent(transform.Transform(1, 1, 100, 100))
    entityTree.root.children[0].addComponent(spriteRenderer.SpriteRenderer(entityTree.root.children[0],"C:/Users/sinai/Documents/PythonPrograms/TheGameEngine/player.jpg"))
    player = entityTree.root.children[0]