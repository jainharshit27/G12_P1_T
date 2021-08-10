import pygame

#initialising pygame and its functions 
pygame.init()

# creating game window and title
screen = pygame.display.set_mode((300,300))

SAFRON=(255, 153, 51)
safron_rect=pygame.Rect(50,100,200,30)

WHITE=(255,255,255)
# Create White Rectangle

Green=(34, 139, 34)
# Create Greeen Rectangle


while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.draw.rect(screen,SAFRON,safron_rect)
    # Draw White Rectangle
    # Draw Green Rectangle
    
    pygame.display.update()