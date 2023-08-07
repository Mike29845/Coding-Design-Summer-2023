#Project 9(Space Invaders)
import pygame
import random
import math

S_WIDTH = 800
S_HEIGHT = 800

#initialize pygame
pygame.init()

#title and icon of window
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)

#create screen and background
screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
background = pygame.image.load("img/background.jpg")

#Classes
class Player():
    img = pygame.image.load("img/player.png")
    WIDTH = img.get_width()
    HEIGHT = img.get_height()

    def __init__(self):#constructor
        self.x = S_WIDTH / 2 - self.WIDTH /2
        self.y = S_HEIGHT - self.HEIGHT *1.5
        self.x_movement = 0

    def move_right(self):
        self.x_movement = 2

    def move_left(self):
        self.x_movement = -2

    def stop_moving(self):
        self.x_movement = 0

    def update(self):#make any neccessary movements and show new player
        self.x += self.x_movement
        self.boundary_check()
        self.show()

    def boundary_check(self):#player stays within screen
        if self.x <= 0:
            self.x = 0
        elif self.x >= S_WIDTH -self.WIDTH:
            self.x = S_WIDTH -self.WIDTH

    def show(self):
        screen.blit(self.img, (self.x, self.y))

class Invader():
    img = pygame.image.load("img/invader.png")
    WIDTH = img.get_width()
    HEIGHT = img.get_height()
    y_shift = S_HEIGHT * .05

    def __init__(self):
        self.reset()
        
    def reset(self):#randomize x and y to respawn within range
        self.x = random.randint(0, S_WIDTH -self.WIDTH)
        self.y = random.randint(int(S_HEIGHT * 0.0625), int(S_HEIGHT * 0.25))
        self.x_movement = 1
    
    def update(self):#moves invader in given direction and updates position
        self.x += self.x_movement
        self.boundary_check()
        self.show()

    def boundary_check(self):
        if self.x <= 0:
            self.x_movement = 1
            self.y += self.y_shift
        elif self.x >= S_WIDTH -self.WIDTH:
            self.x_movement = -1
            self.y += self.y_shift
    
    def show(self):#displays invader at its current position
        screen.blit(self.img, (self.x, self.y))

    def game_over_check(self):#checks if invader reaches too close to bottom
        if self.y > 660:
            return True
        else:
            return False

class Bullet():
    img = pygame.image.load("img/bullet.png")
    WIDTH = img.get_width()
    HEIGHT = img.get_height()
    y_shift = S_HEIGHT * .005

    def __init__(self):
        self.x = 0
        self.reset()
    
    def reset(self):
        self.y = 0
        self.state = "loaded"
    
    def fire(self, player):
        if self.state is "loaded":
            self.x = player.x
            self.y = player.y
            self.state = "fired"

    def did_hit(self, invader):
        distance = math.sqrt(((invader.x-self.x)**2) + ((invader.y-self.y)**2))
        if distance < invader.WIDTH * 0.4:
            return True
        else:
            return False
        
    def update(self):
        if self.state is "fired":
            if self.y <= 0:
                self.reset()
            else:
                self.show()
                self.y -= self.y_shift
    
    def show(self):
        screen.blit(self.img, (self.x + self.WIDTH/2, self.y + self.HEIGHT/3))


player = Player()
bullet = Bullet()
num_invaders = 10
invaders = [Invader() for i in range(num_invaders)]


#game loop
loop = True
while loop:
    screen.fill((0, 0, 0))#reset screen
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #exit
            loop == False
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()
            if event.key == pygame.K_SPACE:
                bullet.fire(player)
        if event.type == pygame.KEYUP:
            if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.stop_moving()
        
    for invader in invaders:
        was_hit = bullet.did_hit(invader)
        if was_hit:
            invader.reset()
            bullet.reset()
        invader.update()
    
    player.update()
    bullet.update()
    pygame.display.update() #update/refresh
pygame.quit()

