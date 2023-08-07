#Project 8(Stacks)
import pygame
import random

def generate_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

#constants
S_WIDTH = 800
S_HEIGHT = 800
COLS = 10
ROWS = 20
B_HEIGHT = S_HEIGHT/ROWS
B_WIDTH = S_WIDTH/COLS

#Variables
speed = 100
y = S_HEIGHT - B_HEIGHT #y keeps track of the top of our  current rectangle 
left = 0
right = S_WIDTH
width = right - left
prev_left = left
prev_right = right
prev_width = width
color = (213, 62, 79)
direction = "l"
score = 0
high_score = 0

#initialize pygame
pygame.init()

#Set up the screen
screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption("Stacks")

font = pygame.font.SysFont(None, 40)

#game Loop
loop = True
while loop:
    pygame.time.delay(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if right <= prev_left or left >= prev_right:
            pygame.time.delay(1000)
            screen.fill((0, 0, 0))
            left = 0
            width = S_WIDTH
            right = S_WIDTH
            prev_left = left
            prev_right = right
            prev_width = width
            y = S_HEIGHT - B_HEIGHT
            direction = "l"
            if score > high_score:
                high_score = score
            score = 0
        else:
            if left != prev_left:
                left = max(left, prev_left)
                right = min(right, prev_right)
                width = right - left
            prev_left = left
            prev_right = right
            prev_width = width
            screen.fill((0, 0, 0), (0, y, S_WIDTH, B_HEIGHT))
            color = generate_random_color()
            pygame.draw.rect(screen, color, (left, y, width, B_HEIGHT))
            y -= B_HEIGHT
            score += 1

    screen.fill((0, 0, 0), (0, y, S_WIDTH, B_HEIGHT))
    if left < 0-width+2*B_WIDTH:
        direction = "r"
    elif left > S_WIDTH-2*B_WIDTH:
        direction = "l"
    if direction == "r":
        left += B_WIDTH
        right += B_WIDTH
    elif direction == "l":
        left -= B_WIDTH
        right -= B_WIDTH
    pygame.draw.rect(screen, color, (left, y, width, B_HEIGHT))

    # Display scores on the screen
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    high_score_text = font.render("High Score: " + str(high_score), True, (255, 255, 255))

    # Clear previous texts by filling the area with black color
    screen.fill((0, 0, 0), (10, 10, 200, 40))
    screen.fill((0, 0, 0), (10, 50, 250, 40))

    # Blit the updated score and high score texts
    screen.blit(score_text, (10, 10))
    screen.blit(high_score_text, (10, 50))
    
    pygame.display.update()

pygame.quit()
