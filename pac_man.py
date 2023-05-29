import pygame
import random

# 游戏窗口大小
WIDTH = 800
HEIGHT = 600

# 颜色定义
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# 初始化Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# 定义吃豆人的类
class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

        self.rect.clamp_ip(screen.get_rect())  # 限制吃豆人在屏幕范围内移动

# 定义豆子的类
class Dot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

# 创建吃豆人对象
pacman = Pacman(WIDTH // 2, HEIGHT // 2)

# 创建豆子对象
dots = pygame.sprite.Group()
for _ in range(50):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    dot = Dot(x, y)
    dots.add(dot)

# 初始化得分
score = 0

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pacman.update()

    # 判断吃豆人是否吃到豆子
    eaten_dots = pygame.sprite.spritecollide(pacman, dots, True)
    score += len(eaten_dots)  # 增加得分

    screen.fill(BLACK)

    dots.draw(screen)
    screen.blit(pacman.image, pacman.rect)

    # 绘制得分文本
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, YELLOW)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
