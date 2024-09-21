import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("Monkey Bananas")

# image를 로딩...
image_bg = pygame.image.load("images/Blue-sky.png")
image_banana = pygame.image.load("images/bananas.png")
image_monkey = pygame.image.load("images/monkey.png")

# 화면의 크기를 가져온다...

# size_bg_width = background.get_size()[0]
# size_bg_height = background.get_size()[1]

size_bg_width, size_bg_height = background.get_size()

# banana, monkey 이미지 사이즈 얻기

size_banana_width = image_banana.get_rect().size[0]
size_banana_height = image_banana.get_rect().size[1]

size_monkey_width = image_monkey.get_rect().size[0]
size_monkey_height = image_monkey.get_rect().size[1]

# banana, monkey의 초기 위치를 설정 (좌표값)
x_pos_banana = size_bg_width / 2 - size_banana_width / 2
y_pos_banana = 0

x_pos_monkey = size_bg_width / 2 - size_monkey_width / 2
y_pos_monkey = size_bg_height - size_monkey_height

x_speed_banana = 1
y_speed_banana = 1

to_x = 0
to_y = 0

# 점수 표시를 위한 변수 선언, font 생성
point = 0
font_point = pygame.font.SysFont(None, 30)

font_gameover = pygame.font.SysFont(None, 30)
text_gameover = font_gameover.render("GAME OVER", True, (255, 0, 0))

size_text_width = text_gameover.get_rect().size[0]
size_text_height = text_gameover.get_rect().size[1]

x_pos_text = size_bg_width / 2 - size_text_width / 2
y_pos_text = size_bg_height / 2 - size_text_height / 2

play = True
while play:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        to_x = -2
      elif event.key == pygame.K_RIGHT:
        to_x = 2

    if event.type == pygame.KEYUP:
      to_x = 0

  # 원숭이가 왼쪽 벽, 오른쪽 벽을 벗어나지 않게 하는 것...
  if x_pos_monkey < 0:
    x_pos_monkey = 0
  elif x_pos_monkey > size_bg_width - size_monkey_width:
    x_pos_monkey = size_bg_width - size_monkey_width

  # 바나나의 위치 (좌표값)
  x_pos_banana += x_speed_banana
  y_pos_banana += y_speed_banana

  # 바나나가 왼쪽, 오른쪽 벽을 벗어나지 않게 함...
  if x_pos_banana <= 0:
    x_speed_banana = -x_speed_banana
    x_pos_banana = 0
  elif x_pos_banana >= size_bg_width - size_banana_width:
    x_speed_banana = -x_speed_banana
    x_pos_banana = size_bg_width - size_banana_width

  # 바나나가 윗면, 아랫면을 벗어나지 않게 함...
  if y_pos_banana <= 0:
    y_speed_banana = -y_speed_banana
    y_pos_banana = 0
  elif y_pos_banana >= size_bg_height - size_banana_height:
    y_speed_banana = -y_speed_banana
    y_pos_banana = size_bg_height - size_banana_height

    # 밑면에 바나나가 부딪히면... -> 게임오버...
    background.blit(text_gameover, (x_pos_text, y_pos_text))
    pygame.display.update()
    pygame.time.delay(2000)
    play = False

  # 앞에서 계산한 바나나, 원숭이 좌표값으로 이미지의 왼쪽 위 모서리를 이동시킨다...
  rect_banana = image_banana.get_rect()
  rect_banana.left = x_pos_banana
  rect_banana.top = y_pos_banana

  rect_monkey = image_monkey.get_rect()
  rect_monkey.left = x_pos_monkey
  rect_monkey.top = y_pos_monkey

  # 바나나가 원숭이와 충돌되는지를 판단한다...
  if rect_monkey.colliderect(rect_banana):
    x_speed_banana = -x_speed_banana
    y_speed_banana = -y_speed_banana
    point += 1

  background.blit(image_bg, (0, 0))
  background.blit(image_banana, (x_pos_banana, y_pos_banana))
  background.blit(image_monkey, (x_pos_monkey, y_pos_monkey))

  text_point = font_point.render(str(point), True, (0, 0, 0))
  background.blit(text_point, (10, 10))

  pygame.display.update()

pygame.quit()