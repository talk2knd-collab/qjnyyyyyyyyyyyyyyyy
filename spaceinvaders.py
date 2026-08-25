import pygame
pygame.init()

WIDTH=900
HEIGHT=500

screen=pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Space Invaders")

spaceship_width=55
spaceship_height=40
VEL=5
FPS=60

space=pygame.transform.scale(pygame.image.load("space1.png"),(WIDTH, HEIGHT))

yellowspaceshipimage=pygame.image.load("yellowspaceship.png")
yellow_spaceship=pygame.transform.rotate(pygame.transform.scale(yellowspaceshipimage,(spaceship_width,spaceship_height)),90)

redspaceshipimage=pygame.image.load("redspaceship.png")
red_spaceship=pygame.transform.rotate(pygame.transform.scale(redspaceshipimage,(spaceship_width,spaceship_height)),270)

BORDER=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)

def draw_window(red,yellow):
    screen.blit(space,(0,0))
    screen.blit(red_spaceship,(red.x,red.y))
    screen.blit(yellow_spaceship,(yellow.x,yellow.y))
    pygame.draw.rect(screen,"white",BORDER)

def yellow_handle_movement(key_pressed,yellow):
    if key_pressed[pygame.K_a]:
        yellow.x-=VEL
    if key_pressed[pygame.K_d]:
        yellow.x+=VEL
    if key_pressed[pygame.K_w]:
        yellow.y-=VEL
    if key_pressed[pygame.K_s]:
        yellow.y+=VEL

def red_handle_movement(key_pressed,red):
    if key_pressed[pygame.K_LEFT]:
        red.x-=VEL
    if key_pressed[pygame.K_RIGHT]:
        red.x+=VEL
    if key_pressed[pygame.K_UP]:
        red.y-=VEL
    if key_pressed[pygame.K_DOWN]:
        red.y+=VEL
pygame.display.update()


def main():    
    red=pygame.Rect(660,210,spaceship_width,spaceship_height)
    yellow=pygame.Rect(190,210,spaceship_width,spaceship_height)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        key_pressed=pygame.key.get_pressed()
        
        draw_window(red,yellow)
        yellow_handle_movement(key_pressed,yellow)
        red_handle_movement(key_pressed,red)
main()    
