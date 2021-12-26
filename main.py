import pygame
import random

WIDTH = 400
HEIGHT = 600

FPS = 120

BLACK=(0,0,0)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Spaceships by Jakub Kochański')

SPACESHIP = pygame.transform.scale(pygame.image.load('assets/spaceship.png'),(30,30))
ALIEN = pygame.transform.scale(pygame.image.load('assets/alien.png'),(30,30))
BACKGROUND = pygame.transform.scale(pygame.image.load('assets/background.png'),(400,600))

spaceship = pygame.Rect(185,550,30,30)
aliens = []

def spaceship_movement(keys_pressed):
    if keys_pressed[pygame.K_LEFT] and spaceship.x>0:
        spaceship.x-=3
    if keys_pressed[pygame.K_RIGHT] and spaceship.x+spaceship.width<WIDTH:
        spaceship.x+=3
    if keys_pressed[pygame.K_UP] and spaceship.y>0:
        spaceship.y-=3
    if keys_pressed[pygame.K_DOWN] and spaceship.y+spaceship.height<HEIGHT:
        spaceship.y+=3
score = 0
time  = 0
counter = 80

def main():
    global time
    run = True
    while run:
        if time%2==0:
            for alien in aliens:
                alien.y+=1
        if time%counter == 0:
            aliens.append(pygame.Rect(random.randrange(0,370),0,30,30))
        time+=1
        pygame.time.Clock().tick(FPS)
        WIN.blit(BACKGROUND,(0,0))
        for alien in aliens:
            WIN.blit(ALIEN,(alien.x,alien.y))
        keys_pressed = pygame.key.get_pressed()
        spaceship_movement(keys_pressed)
        WIN.blit(SPACESHIP,(spaceship.x,spaceship.y))
        pygame.display.update()

        for alien in aliens:
            if alien.y>=HEIGHT:
                pygame.quit()
                run = False
            elif spaceship.colliderect(alien):
                pygame.quit()
                run = False
        if run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False

main()