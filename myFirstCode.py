import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Colors
WHITE = (255, 255, 255)

# Ball settings
ball_radius = 15
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))

# Paddle settings
paddle_width, paddle_height = 8, 100
paddle_speed = 7

# Player paddles
player_paddle = pygame.Rect(WIDTH - 20, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
opponent_paddle = pygame.Rect(10, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and player_paddle.bottom < HEIGHT:
        player_paddle.y += paddle_speed

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Collisions
    if ball_y - ball_radius < 0 or ball_y + ball_radius > HEIGHT:
        ball_speed_y *= -1
    if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:
        ball_speed_x *= -1

    # Paddle collisions
    if ball_x + ball_radius > player_paddle.left and ball_y > player_paddle.top and ball_y < player_paddle.bottom:
        ball_speed_x *= -1
    if ball_x - ball_radius < opponent_paddle.right and ball_y > opponent_paddle.top and ball_y < opponent_paddle.bottom:
        ball_speed_x *= -1

    # Drawing
    screen.fill(WHITE)
    pygame.draw.ellipse(screen, (0, 0, 0), (ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius))
    pygame.draw.rect(screen, (0, 0, 0), player_paddle)
    pygame.draw.rect(screen, (0, 0, 0), opponent_paddle)
    pygame.display.flip()

    clock.tick(60)

# Clean up
pygame.quit()
