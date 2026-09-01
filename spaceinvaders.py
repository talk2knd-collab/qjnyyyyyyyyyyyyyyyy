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
max_bullet=3
bullet_VEL=7
YELLOW_HIT=pygame.USEREVENT+1
RED_HIT=pygame.USEREVENT+2


space=pygame.transform.scale(pygame.image.load("space1.png"),(WIDTH, HEIGHT))

yellowspaceshipimage=pygame.image.load("yellowspaceship.png")
yellow_spaceship=pygame.transform.rotate(pygame.transform.scale(yellowspaceshipimage,(spaceship_width,spaceship_height)),90)

redspaceshipimage=pygame.image.load("redspaceship.png")
red_spaceship=pygame.transform.rotate(pygame.transform.scale(redspaceshipimage,(spaceship_width,spaceship_height)),270)

BORDER=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)

def draw_window(red,yellow,red_bullets,yellow_bullets):
    screen.blit(space,(0,0))
    screen.blit(red_spaceship,(red.x,red.y))
    screen.blit(yellow_spaceship,(yellow.x,yellow.y))
    pygame.draw.rect(screen,"white",BORDER)

    for i in red_bullets:
        pygame.draw.rect(screen,"red",i)
    for i in red_bullets:
        pygame.draw.rect(screen,"yellow",i)

    pygame.display.update()

def yellow_handle_movement(key_pressed,yellow):
    if key_pressed[pygame.K_a] and yellow.x-VEL>0:
        yellow.x-=VEL

    if key_pressed[pygame.K_d] and yellow.x+yellow.width<BORDER.x:
        yellow.x+=VEL
    if key_pressed[pygame.K_w] and yellow.y-VEL>0:
        yellow.y-=VEL
    if key_pressed[pygame.K_s] and yellow.y+VEL+yellow.height<HEIGHT-15:
        yellow.y+=VEL
    

def red_handle_movement(key_pressed,red):
    if key_pressed[pygame.K_LEFT] and red.x-VEL>BORDER.x:
        red.x-=VEL
    if key_pressed[pygame.K_RIGHT] and red.x+VEL+red.width<WIDTH:
        red.x+=VEL
    if key_pressed[pygame.K_UP] and red.y-VEL>0:
        red.y-=VEL
    if key_pressed[pygame.K_DOWN] and red.y+VEL+red.height<HEIGHT-15:
        red.y+=VEL

def handle_bullets(red_bullets,yellow_bullets,red,yellow):
    for i in yellow_bullets:
        i.x+=bullet_VEL
        if red.collide_rect == pygame.event.post(pygame.event.Event(RED_HIT)):
            yellow_bullets.remove(i)
        elif i.x>WIDTH:
            yellow_bullets.remove(i)
    for i in red_bullets:
        i.x+=bullet_VEL
        if yellow.collide_rect == pygame.event.post(pygame.event.Event(YELLOW_HIT)):
            red_bullets.remove(i)
        elif i.x>WIDTH:
            red_bullets.remove(i)

        

def main():    
    red=pygame.Rect(660,210,spaceship_width,spaceship_height)
    yellow=pygame.Rect(190,210,spaceship_width,spaceship_height)

    red_bullets=[]
    yellow_bullets=[]

    red_health=10
    yellow_health=10

    clock=pygame.time.Clock()
                                                        
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.K_DOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets)<max_bullet:
                    bullet=pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2-2,10,5)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(red_bullets)<max_bullet:
                    bullet=pygame.Rect(red.x+red.width,red.y+red.height//2-2,10,5)
                    red_bullets.append(bullet)
        
        key_pressed=pygame.key.get_pressed()
                
        yellow_handle_movement(key_pressed,yellow)
        red_handle_movement(key_pressed,red)
        draw_window(red,yellow,red_bullets,yellow_bullets) 
        handle_bullets(red_bullets,yellow_bullets,red,yellow)    

        pygame.display.update()
main()
