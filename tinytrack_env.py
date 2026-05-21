import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((900,600))
pygame.display.set_caption("TinyTrack AI")

running = True

car_x = 430
car_y = 290
car_width = 40
car_height = 20

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    # car_x += 1  # Move the car to the right for demonstration
    screen.fill((25, 25, 25))
    pygame.draw.rect(screen, (40, 180, 255), (car_x, car_y, car_width, car_height))
    pygame.display.flip()

pygame.quit()