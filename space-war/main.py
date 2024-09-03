import pygame
import random


# 초기화 및 디스플레이 설정
pygame.init()
background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("Space War")

# 이미지 로딩
image_bg = pygame.image.load("images/Moon.png")
image_pico = pygame.image.load("images/pico-1.png")
image_rocket = pygame.image.load("images/rocket-1.png")
image_star = pygame.image.load("images/star-1.png")
image_ball = pygame.image.load("images/ball-1.png")

# 각 이미지의 가로, 세로 크기 구하기
size_bg_width = background.get_size()[0]
size_bg_height = background.get_size()[1]

size_pico_width = image_pico.get_rect().size[0]
size_pico_height = image_pico.get_rect().size[1]

size_rocket_width = image_rocket.get_rect().size[0]
size_rocket_height = image_rocket.get_rect().size[1]

size_star_width = image_star.get_rect().size[0]
size_star_height = image_star.get_rect().size[1]

size_ball_width = image_ball.get_rect().size[0]
size_ball_height = image_ball.get_rect().size[1]

# 각 이미지를 초기 위치시킬 좌표값(x, y)를 구하기
x_pos_pico = size_bg_width / 2 - size_pico_width / 2
y_pos_pico = size_bg_height - size_pico_height

x_pos_rocket = size_bg_width / 2 - size_rocket_width / 2
y_pos_rocket = 0

x_pos_star = size_bg_width / 2 - size_star_width / 2
y_pos_star = size_bg_height - size_pico_height - size_star_height

x_pos_ball = size_bg_width / 2 - size_ball_width / 2
y_pos_ball = size_rocket_height

# Rocket, Pico를 움직이기 위한 변수
to_x_pico = 0
to_x_rocket = 0
random_rocket = random.randrange(0, size_bg_width - size_rocket_width)

# 별 리스트
stars = []

# Ball 타이밍, 리스트, Ball은 random으로 떨어지게 한다...
ball_time = 0
balls = []
random_time = random.randrange(100, 200)

# pico, rocket의 Life 추가
hp_pico = 10
hp_rocket = 10

# pico, rocket rect 구하기
rect_pico = image_pico.get_rect()
rect_rocket = image_rocket.get_rect()

rect_pico.topleft - (x_pos_pico, y_pos_pico)
rect_rocket.topleft - (x_pos_rocket, y_pos_rocket)

# 별과 공의 rect 리스트
rect_stars = []
rect_balls = []

# 폰트 준비

font_hp = pygame.font.SysFont(None, 30)
font_gameover = pygame.font.SysFont(None, 100)

# Gameover 판정변수
gameover =  False


# 게임 while문
play = True
while play:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False

    # 왼쪽, 오른쪽 키보드로 to_x_pico의 값 조정하기
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        to_x_pico = 1
      if event.key == pygame.K_LEFT:
        to_x_pico -= 1

      # 스페이스바 누르면 별 공격 - 리스트에 저장
      if event.key == pygame.K_SPACE:
        x_pos_star = x_pos_pico + size_star_width / 2
        stars.append([x_pos_star, y_pos_star])
        # rect_stars 계속 추가
        rect_stars.append(image_star.get_rect())

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_RIGHT:
        to_x_pico = 0
      elif event.key == pygame.K_LEFT:
        to_x_pico = 0

  # Pico가 양쪽 벽을 벗어나지 않게 하기
  if x_pos_pico < 0:
    x_pos_pico = 0
  elif x_pos_pico > size_bg_width - size_pico_width:
    x_pos_pico = size_bg_width - size_pico_width
  else:
    x_pos_pico += to_x_pico

  rect_pico.topleft(x_pos_pico, y_pos_pico)

  # Rocket의 x좌표를 랜덤으로 움직이기, Rocket이 random값으로 찾아감...
  if random_rocket > x_pos_rocket:
    x_pos_rocket += 0.5
  elif random_rocket < x_pos_rocket:
    x_pos_rocket -= 0.5
  else: # Rocket과 random값이 같아지면...
    random_rocket = random.randrange(0, size_bg_width - size_rocket_width)

  rect_rocket.topleft = (x_pos_rocket, y_pos_rocket)

  # ball attack : 너무 많은 ball이  떨어지지 않게 시간을 조정해야 한다...
  ball_time += 1
  if ball_time == random_time:
    random_time = random.randrange(100, 200)
    ball_time = 0
    x_pos_ball = x_pos_rocket + size_ball_width / 2
    balls.append([x_pos_ball, y_pos_ball])
    rect_balls.append(image_ball)

  # 이미지 그리기
  background.blit(image_bg, (0, 0))
  background.blit(image_pico, (x_pos_pico, y_pos_pico))
  background.blit(image_rocket, (x_pos_rocket, y_pos_rocket))

  # Star 그리기
  if len(stars):
    for star in stars:
      star[1] -= 1  # y 좌표값
      background.blit(image_star, (star[0], star[1]))

      rect_stars[i].topleft = (star[0], star[1])
      if rect_stars[i].colliderect(rect_rocket):  
        stars.remove(rect_stars[i])
        hp_rocket -= 1
        if hp_rocket == 0:
          gameover = "PICO WIN"

      if star[1] <= 0:
        stars.remove(star)

  # Ball 그리기
  if len(balls):
    for ball in balls:
      ball[1] += 1
      background.blit(image_ball, (ball[0], ball[1]))

      rect_balls[i].topleft = (ball[0], ball[1])

      if rect_balls.collideret(rect_pico):
        balls.remove(ball)

      if ball[1] >= size_bg_height:
        balls.remove(ball)

  text_hp_pico = font_hp.render('pico'+str(hp_pico), True, (255, 255, 0))
  background.blit(text_hp_pico, (10, 10))      
  text_hp_rocket = font_hp.render('rocket'+str(hp_rocket), True, (255, 255, 0))
  background.blit(text_hp_rocket, (380, 10))

  # gameover 표시하기
  if gameover:
    text_gameover = font_gameover.render(gameover, True, (255, 0, 0))

    size_text_width = text_gameover.get_rect().size[0]
    size_text_height = text_gameover.get_rect().size[0]

    x_pos_text = size_bg_width / 2 - size_text_width / 2
    y_pos_text = size_bg_height / 2 - size_text_height / 2

    background.blit(text_gameover, (x_pos_text, y_pos_text))
    pygame.display.update()
    pygame.time.delay(3000)
    play = False

  pygame.display.update()

pygame.quit()