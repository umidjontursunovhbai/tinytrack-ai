import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("TinyTrack AI")

running = True

car_x = 430
car_y = 290
car_width = 40
car_height = 20
car_speed = 3

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    # car_x += 1  # Move the car to the right for demonstration
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        car_x += car_speed
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_UP]:
        car_y -= car_speed
    if keys[pygame.K_DOWN]:
        car_y += car_speed

    if car_x < 0:
        car_x = 0
    if car_x > 900 - car_width:
        car_x = 900 - car_width
    if car_y < 0:
        car_y = 0
    if car_y > 600 - car_height:
        car_y = 600 - car_height

    screen.fill((25, 25, 25))

    pygame.draw.rect(screen, (220, 220, 220), (100, 100, 700, 400))
    pygame.draw.rect(screen, (25, 25, 25), (250, 200, 400, 200))

    pygame.draw.rect(screen, (40, 180, 255), (car_x, car_y, car_width, car_height))
    pygame.display.flip()

pygame.quit()
