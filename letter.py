import pygame

class Letter():
    def __init__(self,content,x,y):
        self.x = x
        self.y = y
        self.content = content
        self.image = pygame.image.load("./assets/letters/"+content+".png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def __str__(self):
        return self.content
    
    def is_clicked(self,mouse):
        if self.x < mouse[0] < self.x + self.width:
            if self.y < mouse[1] < self.y + self.height:
                return True

    def is_matched(self,key_word):
        return self.content in key_word


    def update(self,canvas):
        render_pos = (self.x, self.y)
        canvas.blit(self.image,render_pos)