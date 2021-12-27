import pygame
import random

WIDTH = 400
HEIGHT = 600
FPS = 120
BULLETS = 5


BLACK=(0,0,0)
WHITE=(255,255,255)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Spaceships by Jakub Kochański')

SPACESHIP = pygame.transform.scale(pygame.image.load('assets/spaceship.png'),(30,30))
ALIEN = pygame.transform.scale(pygame.image.load('assets/alien.png'),(30,30))
BACKGROUND = pygame.transform.scale(pygame.image.load('assets/background.png'),(400,600))

def lose_game():
    pygame.font.init()
    text = pygame.font.SysFont('comicsans', 20)
    text = text.render(f'wynik {score}',1,WHITE)
    WIN.blit(text,(WIDTH/2 - text.get_width() /2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()
    return False

def spaceship_movement(keys_pressed):
    if keys_pressed[pygame.K_LEFT] and spaceship.x>0:
        spaceship.x-=3
    if keys_pressed[pygame.K_RIGHT] and spaceship.x+spaceship.width<WIDTH:
        spaceship.x+=3
    if keys_pressed[pygame.K_UP] and spaceship.y>0:
        spaceship.y-=3
    if keys_pressed[pygame.K_DOWN] and spaceship.y+spaceship.height<HEIGHT:
        spaceship.y+=3

def time_handling():
    global time
    global score
    global counter
    pygame.time.Clock().tick(FPS)
    if time % 2 == 0:
        for alien in aliens:
            alien.y += 1
        for bullet in bullets:
            for alien in aliens:
                if bullet.colliderect(alien):
                    print('trafiony')
                    bullets.remove(bullet)
                    aliens.remove(alien)
                    score+=1
                    if counter>30:
                        counter-=2
            if bullet.y<=0:
                bullets.remove(bullet)


            bullet.y-=10
    if time % counter == 0:
        aliens.append(pygame.Rect(random.randrange(0, 370), 0, 30, 30))
    time += 1
def draw_window():
    WIN.blit(BACKGROUND, (0, 0))
    for alien in aliens:
        WIN.blit(ALIEN, (alien.x, alien.y))
    for bullet in bullets:
        pygame.draw.rect(WIN,WHITE,bullet)
    keys_pressed = pygame.key.get_pressed()
    spaceship_movement(keys_pressed)
    WIN.blit(SPACESHIP, (spaceship.x, spaceship.y))
    pygame.display.update()

spaceship = pygame.Rect(185,550,30,30)
aliens = []
bullets = []
score = 0
time  = 0
counter = 80

def main():
    run = True
    while run:
        time_handling()
        draw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = lose_game()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(bullets)<=BULLETS:
                    bullet = pygame.Rect(spaceship.x+spaceship.width//2,spaceship.y,2,10)
                    bullets.append(bullet)
        if run:
            for alien in aliens:
                if alien.y+spaceship.height>=HEIGHT:
                    run = lose_game()
                elif spaceship.colliderect(alien):
                    run = lose_game()



main()