import pygame
import sys
import dataStructures
import entityManager
import renderer
import spriteRenderer
import transform

pygame.init()

window = pygame.display.set_mode((720, 480))
pygame.display.set_caption("Game")

running = True

entityTree = entityManager.EntityTree()
entityTree.addEntity("player", None)
entityTree.root.children[0].addComponent(transform.Transform(50, 1, 100, 100))
entityTree.root.children[0].addComponent(spriteRenderer.SpriteRenderer(entityTree.root.children[0],"C:/Users/sinai/Documents/PythonPrograms/TheGameEngine/player.jpg"))
player = entityTree.root.children[0]

renderer = renderer.RenderEngine(entityTree.root.children)

def EventHandler(): 
    global running
    global player

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.components[0].x += -10
            if event.key == pygame.K_RIGHT:
                player.components[0].x += 10
            if event.key == pygame.K_UP:
                player.components[0].y += -10
            if event.key == pygame.K_DOWN:
                player.components[0].y += 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.components[0].x += -10
            if event.key == pygame.K_RIGHT:
                player.components[0].x += 10
            if event.key == pygame.K_UP:
                player.components[0].y += -1
            if event.key == pygame.K_DOWN:
                player.components[0].y += 10

def UpdateAllUpates(entityTree):
    for entity in entityTree.root.children:
        for component in entity.components:
            component.update()
    
        
while running :
    window.fill((0, 0, 0))
    EventHandler()
    UpdateAllUpates(entityTree)
    renderer.render(window)
    pygame.display.update()