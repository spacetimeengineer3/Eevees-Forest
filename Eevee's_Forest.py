import pygame
from pygame.locals import *
from random import randint
from pygame import mixer 
pygame.init()

white = (255, 255, 255)
black = (  0,   0,   0)
red = (180, 0, 0)
green = (0, 255, 0)
turquoise = (0, 255, 255)
yellow = (255, 255, 0)
purple = (180,   0, 180)
magenta = (255, 0, 255)
lblue = (154, 167, 229)
lteal = (70, 216, 200)

def intro():
    intro = True
    info.draw(screen)
    keys = pygame.key.get_pressed()
    if keys [K_RETURN]:
        intro = False
        enter_sound.play()
    if intro == True:
        info.draw(screen)
    if intro == False:
        info.remove(instructions)

class Instructions(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/instructions3.png")
        self.rect = self.image.get_rect()
instructions = Instructions()
instructions.rect.x = 0
instructions.rect.y = 0

class BlueApple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/blueapple40.png")
        self.rect = self.image.get_rect()
blueapple = BlueApple()

class PinkBanana(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/pinkbanana40.png")
        self.rect = self.image.get_rect()
pinkbanana = PinkBanana()

class Pizza(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/pizza40.png")
        self.rect = self.image.get_rect()
pizza = Pizza()

class Cake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/cake40.png")
        self.rect = self.image.get_rect()
cake = Cake()

class BlueAppleScore(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/blue_apple.png")
        self.rect = self.image.get_rect()
blueapple2 = BlueAppleScore()
blueapple2.rect.x = 10
blueapple2.rect.y = 10

class ShinyEevee(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.eevee_right = [pygame.image.load('Images/eevee_r1.png'), pygame.image.load('Images/eevee_r2.png'), pygame.image.load('Images/eevee_r3.png'), pygame.image.load('Images/eevee_r4.png')]
        self.eevee_left = [pygame.image.load('Images/eevee_l1.png'), pygame.image.load('Images/eevee_l2.png'), pygame.image.load('Images/eevee_l3.png'), pygame.image.load('Images/eevee_l4.png')]
        self.eevee_lr = [pygame.image.load('Images/eevee_r1.png'), pygame.image.load('Images/eevee_r2.png'), pygame.image.load('Images/eevee_r3.png'), pygame.image.load('Images/eevee_r4.png'), pygame.image.load('Images/eevee_l1.png'), pygame.image.load('Images/eevee_l2.png'), pygame.image.load('Images/eevee_l3.png'), pygame.image.load('Images/eevee_l4.png')]
        
        self.image = self.eevee_lr[2]
        self.rect = self.image.get_rect()
        
shiny_eevee = ShinyEevee()
shiny_eevee.rect.x = 20
shiny_eevee.rect.y = 400

x = shiny_eevee.rect.x
y = shiny_eevee.rect.y
def check_keys():
    global shiny_eevee
    self = shiny_eevee
    keys = pygame.key.get_pressed()
    if keys[K_RIGHT]and shiny_eevee.rect.x <600:
        shiny_eevee.rect.x += 30
        if self.image == self.eevee_lr[0]:
            pygame.time.wait(50)
            self.image = self.eevee_lr[1]
        elif self.image == self.eevee_lr[1]:
            pygame.time.wait(50)
            self.image = self.eevee_lr[2]
        elif self.image == self.eevee_lr[2]:
            pygame.time.wait(50)
            self.image = self.eevee_lr[3]
        elif self.image == self.eevee_lr[3]:
            pygame.time.wait(50)
            self.image = self.eevee_lr[0]
        elif self.image == self.eevee_lr[4]:
            pygame.time.wait(50)
            self.image = self.eevee_lr[0]
        elif self.image == self.eevee_lr[5]:
            pygame.time.wait(50)
            self.image = self.eevee_lr[1]
        elif self.image == self.eevee_lr[6]:
            pygame.time.wait(50)
            self.image = self.eevee_lr[2]
        elif self.image == self.eevee_lr[7]:
            pygame.time.wait(50)
            self.image = self.eevee_lr[3]
       
    if keys[K_LEFT] and shiny_eevee.rect.x > 5:
        shiny_eevee.rect.x -= 30
        if self.image == self.eevee_lr[0]:
            pygame.time.wait(50)
            self.image = self.eevee_lr[4]
        elif self.image == self.eevee_lr[1]:
            pygame.time.wait(50)
            self.image = self.eevee_lr[5]
        elif self.image == self.eevee_lr[2]:
            pygame.time.wait(50)
            self.image = self.eevee_lr[6]
        elif self.image == self.eevee_lr[3]:
            pygame.time.wait(50)
            self.image = self.eevee_lr[7]
        elif self.image == self.eevee_lr[4]:
            pygame.time.wait(50)
            self.image = self.eevee_lr[5]
        elif self.image == self.eevee_lr[5]:
            pygame.time.wait(50)
            self.image = self.eevee_lr[6]
        elif self.image == self.eevee_lr[6]:
            pygame.time.wait(50)
            self.image = self.eevee_lr[7]
        elif self.image == self.eevee_lr[7]:
            pygame.time.wait(50)
            self.image = self.eevee_lr[4]

    
    if keys[K_SPACE] and shiny_eevee.rect.y >10:
        shiny_eevee.rect.y -= 50
    if keys[K_SPACE] and end == True:
        shiny_eevee.rect.y =500
    if keys[K_SPACE]== False and shiny_eevee.rect.y <400:
        shiny_eevee.rect.y += 30
    if keys[K_ESCAPE]:
        runaway_sound.play(1)
        pygame.time.wait(1800)
        pygame.quit()
        quit()

allsprites = pygame.sprite.Group()
info = pygame.sprite.Group()
info.add(instructions)
allsprites.add(shiny_eevee)
allsprites.add(blueapple2)
blueapples = pygame.sprite.Group()
pinkbananas = pygame.sprite.Group()
pizzas = pygame.sprite.Group()
cakes = pygame.sprite.Group()
screenWidth = 800
screenHeight = 600
screenSize = [screenWidth, screenHeight]
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Eevee's Forest")
eat_sound = pygame.mixer.Sound("Audio/food_crunch1.wav")
eat_sound.set_volume(0.4)
pizza_sound = pygame.mixer.Sound("Audio/pizza.wav")
pizza_sound.set_volume(0.9)
banana_sound = pygame.mixer.Sound("Audio/ew.wav")
banana_sound.set_volume(0.9)
lose_sound = pygame.mixer.Sound("Audio/lose.wav")
lose_sound.set_volume(0.4)
win_sound = pygame.mixer.Sound("Audio/win.mp3")
win_sound.set_volume(0.3)
cake_sound = pygame.mixer.Sound("Audio/Wish.mp3")
enter_sound = pygame.mixer.Sound("Audio/enter.mp3")
runaway_sound = pygame.mixer.Sound("Audio/runaway.mp3")
runaway_sound.set_volume(0.5)
mixer.init()
mixer.music.load("Audio/LavenderTownPiano.mp3")
mixer.music.set_volume(0.9)
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()

done = False
score = 0

end = False
win = False
lose = False

while not done:
    # 1. Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    check_keys()
    
    # 2. Program logic, change variables, etc.
    collidelist1 = pygame.sprite.spritecollide(shiny_eevee, blueapples, True)
    for blueapple in collidelist1:
        allsprites.remove(blueapple)
        blueapples.remove(blueapple)
        eat_sound.play()
        score = score + 1
        if score >=50:
            pygame.mixer.music.stop()
            win_sound.play(-1)
             
    chance1 = randint(1, 50)
    if chance1 <= 2:
        # Make a new blueapple.
        blueapple = BlueApple()
        # Put it on a random location on the screen.
        blueapple.rect.x = randint(790, 800)
        blueapple.rect.y = randint(0, screenHeight/2)

        blueapples.add(blueapple)

        allsprites.add(blueapple)
        
    # Move all the blueapples to the left.
    for blueapple in blueapples:
        blueapple.rect.x -= 5
        
    collidelist2 = pygame.sprite.spritecollide(shiny_eevee, pinkbananas, True)
    for pinkbanana in collidelist2:
        allsprites.remove(pinkbanana)
        blueapples.remove(pinkbanana)
        banana_sound.play()
        score = score - 5
        if  score <0:
            pygame.mixer.music.stop()
            lose_sound.play()
             
    chance2 = randint(1, 50)
    if chance2 <= 2:
        # Make a new pinkbanana.
        pinkbanana = PinkBanana()
        # Put it on a random location on the screen.
        pinkbanana.rect.x = randint(0, 10)
        pinkbanana.rect.y = randint(0, screenHeight/2)

        pinkbananas.add(pinkbanana)

        allsprites.add(pinkbanana)
        
    # Move all the pinkbananas to the right.
    for pinkbanana in pinkbananas:
        pinkbanana.rect.x += 7
        
    collidelist3 = pygame.sprite.spritecollide(shiny_eevee, cakes, True)
    for cake in collidelist3:
        allsprites.remove(cake)
        cakes.remove(cake)
        cake_sound.play()
        score = score + 20
        if score >=50:
            pygame.mixer.music.stop()
            win_sound.play(-1)
             
    chance3 = randint(1, 800)
    if chance3 <= 2:
        # Make a new cake.
        cake = Cake()
        # Put it on a random location on the screen.
        cake.rect.x = randint(0, 10)
        cake.rect.y = randint(0, screenHeight/2)
        
        cakes.add(cake)

        allsprites.add(cake)
        
    # Move all the cake to the right.
    for cake in cakes:
        cake.rect.x += 5
        
        
    collidelist4 = pygame.sprite.spritecollide(shiny_eevee, pizzas, True)
    for pizza in collidelist4:
        allsprites.remove(pizza)
        pizzas.remove(pizza)
        pizza_sound.play()
        score = score + 10
        if score >=50:
            pygame.mixer.music.stop()
            win_sound.play(-1)     
    chance4 = randint(1, 300)
    if chance4 <= 2:
        # Make a new pizza.
        pizza = Pizza()
        # Put it on a random location on the screen.
        pizza.rect.x = randint(790, 800)
        pizza.rect.y = randint(0, screenHeight/2)

        pizzas.add(pizza)

        allsprites.add(pizza)
        
    # Move all the pizza to the left.
    for pizza in pizzas:
        pizza.rect.x -= 5
   
    # 3. Draw stuff
    background = pygame.image.load("Images/green_forest2.png")
    background2 = pygame.image.load("Images/dark_forest.png")
    background3 = pygame.image.load("Images/pink_forest.png")
    screen.blit(background, [0, 0])

    allsprites.draw(screen)
    
    font = pygame.font.Font(None, 55)
    font2 = pygame.font.Font(None, 100)
    text = font.render("%d" % score, True, lblue)
    screen.blit(text, [70, 25])
    gameover = font2.render("Game Over",True, red)
    win = font2.render("You Win!", True, lteal)
    
    if score <0:
        screen.blit(background2, [0, 0])
        screen.blit(gameover, [200, 270])
        end = True
        lose = True
        
    elif score >=50:
        screen.blit(background3, [0, 0])
        screen.blit(win, [240, 270])
        end = True
        win = True
        pygame.mixer.music.stop
        
    info.draw(screen)
    pygame.display.flip()
    clock.tick(20)
    intro()
    
pygame.quit()
