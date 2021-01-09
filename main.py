import pygame
from letter import Letter
from hangman import HangMan
from letter_holder import LetterHolder


word_list = [
    {
        "key_word": "APPLE",
        "hint": "An __________ a day keep the doctor away!"
    }
]

key_word = "APPLE"


pygame.init()
pygame.display.set_caption("Pong game")
loop = True
clock = pygame.time.Clock()
BG_COLOR = (47,62,63)

# Set up game window
SIZE = (1200,700)
canvas = pygame.display.set_mode(SIZE)

letters = []
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

starting_point = [100,350]


for i,l in enumerate(alphabet):
    letters.append(Letter(l,starting_point[0],starting_point[1]))

    starting_point[0] += letters[-1].width + 20
    if starting_point[0] > 1000:
        starting_point[0] = 100
        starting_point[1] += letters[-1].height + 20


starting_point = [450,200]
letter_holders = []

for l in key_word:
    print(l)
    letter_holders.append(LetterHolder(l,starting_point[0],starting_point[1]))

    starting_point[0] += letter_holders[-1].width + 20


hangman = HangMan(200,180)    

while loop:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            clicked = [l for l in letters if l.is_clicked(pos)]
            for l in clicked:
                if l.is_matched(key_word):
                    for h in letter_holders:
                        if h.content == l.content:
                            h.hidden = False
                else:
                    if hangman.state < 7:
                        hangman.state += 1
                    else:
                        loop = False


    canvas.fill(BG_COLOR)
    for l in letters:
        l.update(canvas)
    for l in letter_holders:
        l.update(canvas)
    hangman.update(canvas)
    
    font = pygame.font.SysFont("monospace",15)

    clock.tick(60)
    pygame.display.flip()
