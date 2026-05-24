import pygame

WIDTH = 900
HEIGHT = 600
FPS = 60

BACKGROUND_COLOR = (25, 25, 25)
TRACK_COLOR = (220, 220, 220)
CAR_COLOR = (40, 180, 255)
CRASH_COLOR = (255, 60, 60)

TRACK_OUTER = (100, 100, 700, 400)
TRACK_INNER = (250, 200, 400, 200)

START_X = 120
START_Y = 280
CAR_WIDTH = 40
CAR_HEIGHT = 20
CAR_SPEED = 3

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TinyTrack AI")

running = True

car_x = START_X
car_y = START_Y
car_width = CAR_WIDTH
car_height = CAR_HEIGHT
car_speed = CAR_SPEED
crashed = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                car_x = START_X
                car_y = START_Y
                crashed = False

    clock.tick(FPS)
    # car_x += 1  # Move the car to the right for demonstration
    keys = pygame.key.get_pressed()
    if not crashed:
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
    if car_x > WIDTH - car_width:
        car_x = WIDTH - car_width
    if car_y < 0:
        car_y = 0
    if car_y > HEIGHT - car_height:
        car_y = HEIGHT - car_height

    car_center_x = car_x + car_width / 2
    car_center_y = car_y + car_height / 2

    outer_x, outer_y, outer_width, outer_height = TRACK_OUTER
    inner_x, inner_y, inner_width, inner_height = TRACK_INNER

    inside_outer = (
        outer_x < car_center_x < outer_x + outer_width
        and outer_y < car_center_y < outer_y + outer_height
    )
    inside_inner = (
        inner_x < car_center_x < inner_x + inner_width
        and inner_y < car_center_y < inner_y + inner_height
    )
    on_track = inside_outer and not inside_inner

    if not on_track:
        crashed = True

    if crashed:
        car_color = CRASH_COLOR
    else:
        car_color = CAR_COLOR

    screen.fill(BACKGROUND_COLOR)

    pygame.draw.rect(screen, TRACK_COLOR, TRACK_OUTER)
    pygame.draw.rect(screen, BACKGROUND_COLOR, TRACK_INNER)

    pygame.draw.rect(screen, car_color, (car_x, car_y, car_width, car_height))
    pygame.display.flip()

pygame.quit()
