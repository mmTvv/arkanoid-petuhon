import pygame
import random

# Инициализация pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
BALL_RADIUS = 10
BLOCK_WIDTH, BLOCK_HEIGHT = 60, 20
BLOCK_ROWS, BLOCK_COLS = 5, 10

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Arkanoid')

# Создание каретки (платформы)
def draw_paddle(paddle_rect):
    pygame.draw.rect(screen, WHITE, paddle_rect)

# Создание шарика
def draw_ball(ball_pos):
    pygame.draw.circle(screen, WHITE, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS)

# Создание блоков
def draw_blocks(blocks):
    for block in blocks:
        pygame.draw.rect(screen, RED, block)

# Основная функция игры
def main():
    # Начальные настройки
    paddle_rect = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball_pos = [WIDTH // 2, HEIGHT // 2]
    ball_vel = [random.choice([-4, 4]), -4]

    blocks = [pygame.Rect(i * (BLOCK_WIDTH + 5) + 20, j * (BLOCK_HEIGHT + 5) + 20, BLOCK_WIDTH, BLOCK_HEIGHT)
              for j in range(BLOCK_ROWS) for i in range(BLOCK_COLS)]

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Получаем позицию мыши и обновляем каретку
        mouse_x, _ = pygame.mouse.get_pos()
        paddle_rect.x = mouse_x - PADDLE_WIDTH // 2

        # Ограничиваем движение каретки по краям экрана
        if paddle_rect.left < 0:
            paddle_rect.left = 0
        if paddle_rect.right > WIDTH:
            paddle_rect.right = WIDTH

        # Двигаем шарик
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]

        if ball_pos[0] <= BALL_RADIUS or ball_pos[0] >= WIDTH - BALL_RADIUS:
            ball_vel[0] = -ball_vel[0]
        if ball_pos[1] <= BALL_RADIUS:
            ball_vel[1] = -ball_vel[1]
        elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
            print("Game Over!")
            running = False

        # Отскок от каретки
        if paddle_rect.collidepoint(ball_pos[0], ball_pos[1] + BALL_RADIUS):
            ball_vel[1] = -ball_vel[1]

        # Отскок от блоков
        for block in blocks[:]:
            if block.collidepoint(ball_pos[0], ball_pos[1]):
                ball_vel[1] = -ball_vel[1]
                blocks.remove(block)

        # Отображение
        screen.fill(BLACK)
        draw_paddle(paddle_rect)
        draw_ball(ball_pos)
        draw_blocks(blocks)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
