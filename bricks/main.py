import pygame
import random


pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("Brick Breaking")

size_width_bg = background.get_size()[0]
size_height_bg = background.get_size()[1]

# pedal 사이즈, 좌표, rect
size_width_pedal = 100
size_height_pedal = 15

x_pos_pedal = size_width_bg // 2 - size_width_pedal // 2
y_pos_pedal = size_height_bg // 2 - size_height_pedal

rect_pedal = pygame.Rect(x_pos_pedal, y_pos_pedal, size_height_pedal, size_height_pedal)

# ball의 사이즈, 좌표. rect
size_radius_ball = 20

x_pos_ball = size_width_bg // 2
y_pos_ball = size_height_bg - size_height_pedal - size_radius_ball

rect_ball = pygame.Rect(x_pos_ball, y_pos_ball, size_radius_ball * 2, size_radius_ball * 2)
rect_ball_center = (x_pos_ball, y_pos_ball)

# 공의 방향과 스피드를 설정하는 변수 (처음에는 둘 다 +)
x_speed_ball = 0.1
y_speed_ball = 0.1

# 블록 사이즈, 좌표, Rect
size_width_block = size_width_bg // 10
size_height_block = 30

x_pos_block = 0
y_pos_block = 0

rect_block = [[] for _ in range(10)] # == [[], [], [], [], [], [], [], [], []. []]

color_block = [[] for _ in range(10)]

for i in range(10):
  for j in range(3):
    rect_block[i].append(pygame.Rect(i * size_width_block, j * size_height_block, size_width_block, size_height_block))
    color_block[i].append((random.randrange(255), random.randrange(132, 233), random.randrange(150, 255)))

# 마우스 좌표 (마우스로 페달을 움직임)

x_pos_mouse, y_pos_mouse = 0, 0

# gameover 판정변수

gameover = False
play = True

while play:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False
  
    if event.type == pygame.MOUSEMOTION:
      x_pos_mouse, y_pos_mouse = pygame.mouse.get_pos()

      # 마우스가 왼쪽, 오른쪽 벽을 벗어나지 않게
      if x_pos_mouse - size_width_pedal // 2 >= 0 and x_pos_mouse + size_width_pedal // 2 <= size_width_bg:
        x_pos_pedal = x_pos_mouse - size_width_pedal // 2
        rect_pedal.left = x_pos_mouse - size_width_pedal // 2

  background.fill((255, 255, 255))

  # pedal 그리기
  pygame.draw.rect(background, (244, 255, 0), rect_pedal)

  # ball 좌표 계산
  if x_pos_ball - size_radius_ball <= 0:
    x_speed_ball = -x_speed_ball
  elif x_pos_ball >= size_width_bg - size_radius_ball:
    x_speed_ball = -x_speed_ball

  if y_pos_ball - size_radius_ball <= 0:
    y_speed_ball = -y_speed_ball
  elif y_pos_ball >= size_height_bg - size_radius_ball:
    y_speed_ball = -y_speed_ball

  # 공 좌표에 스피드 값을 누적
  x_pos_ball += x_speed_ball
  y_pos_ball += y_speed_ball

  # ball 그리기
  rect_ball_center = (x_pos_ball, y_pos_ball)
  pygame.draw.circle(background, (255, 0, 255), (x_pos_ball, y_pos_ball), size_radius_ball)

  # 공이 pedal에 닿을 때
  if rect_ball.colliderect(rect_pedal):
    y_speed_ball = -y_speed_ball

  # block 그리기
  for i in range(10):
    for j in range(3):
      if rect_block[i][j]:  
        pygame.draw.rect(background,  color_block[i][j], rect_block[i][j])
        rect_block[i][j].topleft = (i * size_width_block, j * size_height_block)

        # 공 - 벽돌 닿았을 때
        if rect_ball.colliderect(rect_block[i][j]):
          x_speed_ball = -x_speed_ball
          y_speed_ball = -y_speed_ball
          rect_block

  pygame.display.update()

pygame.quit()