import pygame

class HangMan:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.state = 1
        self.image = pygame.image.load("./assets/hangman pics/hangman_1.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self,canvas):
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.image = pygame.image.load("./assets/hangman pics/hangman_"+str(self.state)+".png")
        self.image = pygame.transform.rotozoom(self.image,0,0.6)
        render_pos = ((self.x - self.width//2),(self.y - self.height//2))
        canvas.blit(self.image,render_pos)