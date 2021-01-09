import pygame

class LetterHolder:
    def __init__(self,content,x,y):
        self.x = x
        self.y = y
        self.content = content
        self.image = pygame.image.load("./assets/letters/"+ content + ".png")
        self.hidden = True
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self,canvas):
        if self.hidden == False:
            render_pos = self.x, self.y
            canvas.blit(self.image, render_pos)