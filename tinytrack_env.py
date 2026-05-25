import pygame
import math

WIDTH = 900
HEIGHT = 600
CAR_HEIGHT = 20
CAR_WIDTH = 40
CRASHED_COLOR = (255, 60, 60)
NOT_CRASHED_COLOR = (40, 180, 255)
FPS = 60
ACCELERATION = 0.4
FRICTION = 0.9
MAX_SPEED = 5
SENSOR_LENGTH = 100

def is_on_track(x, y):
    inside_outer = 100 < x < WIDTH - 100 and 100 < y < HEIGHT - 100
    inside_inner = 250 < x < WIDTH - 250 and 200 < y < HEIGHT - 200
    return inside_outer and not inside_inner

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TinyTrack AI")

running = True

car_x = 120 # Starting position of the car in x direction
car_y = 280 # Starting position of the car in y direction
car_width = CAR_WIDTH
car_height = CAR_HEIGHT
crashed = False
car_angle = 0
car_velocity = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                car_x = 120
                car_y = 280
                crashed = False
                car_angle = 0
                car_velocity = 0

    clock.tick(FPS)
    # car_x += 1  # Move the car to the right for demonstration
    keys = pygame.key.get_pressed()
    if not crashed:
        if keys[pygame.K_a]:
            car_angle += 3
        if keys[pygame.K_d]:
            car_angle -= 3

        angle_rad = math.radians(car_angle)
        if keys[pygame.K_w]:
            car_velocity += ACCELERATION
        if keys[pygame.K_s]:
            car_velocity -= ACCELERATION

        if car_velocity > MAX_SPEED:
            car_velocity = MAX_SPEED
        if car_velocity < -MAX_SPEED:
            car_velocity = -MAX_SPEED

        car_velocity *= FRICTION

        car_x += car_velocity * math.cos(angle_rad)
        car_y -= car_velocity * math.sin(angle_rad)

    if car_x < 0:
        car_x = 0
    if car_x > WIDTH - car_width:
        car_x = WIDTH - car_width
    if car_y < 0:
        car_y = 0
    if car_y > HEIGHT - car_height:
        car_y = HEIGHT - car_height

    car_center_x = car_x + CAR_WIDTH / 2
    car_center_y = car_y + CAR_HEIGHT / 2

    on_track = is_on_track(car_center_x, car_center_y)

    if not on_track:
        crashed = True
        car_velocity = 0

    if not crashed:
        car_color = NOT_CRASHED_COLOR
    else:
        car_color = CRASHED_COLOR
        
    screen.fill((25, 25, 25))

    pygame.draw.rect(screen, (220, 220, 220), (100, 100, WIDTH - 200, HEIGHT - 200))
    pygame.draw.rect(screen, (25, 25, 25), (250, 200, WIDTH - 500, HEIGHT - 400))

    angle_rad = math.radians(car_angle)
    sensor_end_x = car_center_x + SENSOR_LENGTH * math.cos(angle_rad)
    sensor_end_y = car_center_y - SENSOR_LENGTH * math.sin(angle_rad)
    pygame.draw.line(screen, (255, 255, 0), (car_center_x, car_center_y), (sensor_end_x, sensor_end_y), 2)

    # pygame.draw.rect(screen, car_color, (car_x, car_y, CAR_WIDTH, CAR_HEIGHT))
    car_surface = pygame.Surface((CAR_WIDTH, CAR_HEIGHT), pygame.SRCALPHA)
    pygame.draw.rect(car_surface, car_color, (0, 0, CAR_WIDTH, CAR_HEIGHT))

    rotated_car = pygame.transform.rotate(car_surface, car_angle)

    car_rect = pygame.Rect(car_x, car_y, CAR_WIDTH, CAR_HEIGHT)
    rotated_rect = rotated_car.get_rect(center=car_rect.center)

    screen.blit(rotated_car, rotated_rect)
    pygame.display.flip()

pygame.quit()
