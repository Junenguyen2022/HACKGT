import pygame, sys
from pygame.locals import *

screen_h = 600
screen_w = 432

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = ( 0, 255, 0)
RED = (255, 0, 0)
ROSE = (255, 105, 180)

pygame.init()
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Guess Crush!')

start_img = pygame.image.load('funky-pink-heart.png').convert_alpha()
font = pygame.font.SysFont('consolas', 14)
font1 = pygame.font.SysFont('consolas', 20)
font2 = pygame.font.SysFont('consolas', 18)

textSurface = font.render('Thinking about your crush, ', True, BLACK, ROSE)
textSurface1 = font.render('and the question you want to ask. ', True, BLACK, ROSE)
textSurface2 = font2.render('Press here ', True, WHITE, ROSE)


#button class
class Button():
    def __init__(self, x, y, image, scale):
        
        width = image.get_width()
        height = image.get_height()

        self.clicked = False
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self): 
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
        
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action
#create button instances
start_button = Button(115, 100, start_img, 1)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((255,182,193))

    def rungame():
        import random
        random_number = random.randint(1,12)

        if random_number == 1:
            answer = "Yes - definitely."
        elif random_number == 2:
            answer = "It is deciedly no."
        elif random_number == 3:
            answer = "Without a doubt."
        elif random_number == 4:
            answer = "Not now"
        elif random_number == 5:
            answer = "Ask again later."
        elif random_number == 6:
            answer = "Better not tell you now."
        elif random_number == 7:
            answer = "My sources say no." 
        elif random_number == 8:
            answer = "Outlook not so good."
        elif random_number == 9:
            answer = "Very doubtful."
        elif random_number == 10:
            answer = "Go ahead."
        elif random_number == 11:
            answer = "Yes, she love you."
        elif random_number == 12:
            answer = "No, she doesn't love you."
        else:
            answer = "Moving on."

        print("Cupid said: " + answer)

    if start_button.draw():
        print(str(rungame()))
        u = str(rungame)

        textSurface4 = font1.render(u, True, WHITE)
        screen.blit(textSurface4, (100,500))

    
    screen.blit(textSurface, (105,350))
    screen.blit(textSurface1, (75,400))
    screen.blit(textSurface2, (166,450))
    
    
    pygame.display.update()
    

    





    