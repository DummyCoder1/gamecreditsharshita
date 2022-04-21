import pygame, sys

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((400,600))
font1=pygame.font.Font('freesansbold.ttf',26)
name=font1.render("SPACE INVADERS",False,(225,225,225))
text=font1.render("created by Harshita",False,(225,225,225))
y=100






while True:    
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
      
    screen.blit(name,[95,y])
    screen.blit(text,[110,y+50])       
   
    
    pygame.display.update()
    clock.tick(30)
