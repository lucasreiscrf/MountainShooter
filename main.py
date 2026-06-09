import pygame

pygame.init()
print('Setup start')
window = pygame.display.set_mode(size=(600, 480))
print('Setup end')

print('Loop start')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Quitting...')
            pygame.quit() # Close window
            quit() # end pygame

