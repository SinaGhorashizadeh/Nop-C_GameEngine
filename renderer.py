class RenderEngine:
    def __init__(self, entitys):
        self.entityTreesChildrens = entitys
        self.spriteRenderers = []
        self.transforms = []
        self.sortArrays()

    def updateRender(self, gameObject):
        self.renderlist.append(gameObject)

    def sortArrays(self):
        for gameObject in self.entityTreesChildrens:
            if gameObject.getComponent("SpriteRenderer") != None:
                self.spriteRenderers.append(gameObject.getComponent("SpriteRenderer"))
                if gameObject.getComponent("Transform") != None:
                    self.transforms.append(gameObject.getComponent("Transform"))

    def render(self, window):
        for i in range(len(self.transforms)):
            window.blit(self.spriteRenderers[i].sprite, (self.transforms[i].x, self.transforms[i].y, self.transforms[i].width, self.transforms[i].height))
            
