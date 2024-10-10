import pygame
from pygame.locals import *
import random


pygame.init()

# create the window
width = 500
height = 500

screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Car Game")

# colors 설정
gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 232, 0)

# road & mark 그리기
road_width = 300
marker_width = 10
marker_height = 30

# road & edge & marks
road = (100, 0, road_width, height)
left_edge_marker = (95, 0, marker_width, height)
right_edge_marker = (395, 0, marker_width, height)

# game settings
gameover = False
speed = 2
score = 0

# lane 좌표값
left_lane = 150
center_lane = 250
right_lane = 350
lanes = [left_lane, center_lane, right_lane]

# lane marker가 움직이도록 animation 
lane_marker_move_y = 0

# 자동차 Class
class Vehicle(pygame.sprite.Sprite):
  def __init__(self, image, x, y):
    pygame.sprite.Sprite.__init__(self)

    # 본래 자동차 이미지가 도록 폭 보다 크기 때문에, 이미지를 축소해준다.
    image_scale = 45 / image.get_rect().width
    new_width = image.get_rect().width * image_scale
    new_height = image.get_rect().height * image_scale
    self.image = pygame.transform.scale(image, (new_width, new_height))

    self.rect = self.image.get_rect()
    self.rect.center = [x, y]


# Player Class
class PlayerVehicle(Vehicle):
  def __init__(self, x, y):
    image = pygame.image.load('images/car.png')
    super().__init__(image, x, y)

# player 출발 좌표
player_x = 250
player_y = 400

# player의 자동차 생성
player_group = pygame.sprite.Group()
player = PlayerVehicle(player_x, player_y)
player_group.add(player)


# vechicle 이미지 로딩
image_filenames = ['pickup_truck.png', 'semi_trailer.png', 'taxi.png', 'van.png']
vehicle_images = []
for image_filename in image_filenames:
    image = pygame.image.load('images/' + image_filename)
    vehicle_images.append(image)

vehicle_group = pygame.sprite.Group()

# 충돌 이미지 로딩

crash = pygame.image.load('images/crash.png')
crash_rect = crash.get_rect()

# game loop
clock = pygame.time.Clock()
fps = 120
running = True


while running:
  clock.tick(fps)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
    # 자동차 움직이기
    if event.type == KEYDOWN:
      if event.key == K_LEFT and player.rect.center[0] > left_lane:
        player.rect.x -= 100
      elif event.key == K_RIGHT and player.rect.center[0] < right_lane:
        player.rect.x += 100
    
      for vehicle in vehicle_group:
        if pygame.sprite.collide_rect(player, vehicle):
          gameover = True

          if event.key == K_LEFT:
            player.rect.left = vehicle.rect.right
            crash_rect.center = [player.rect.left, (player.rect.center[1] + vehicle.rect.center[1]) / 2]
          elif event.key == K_RIGHT:
            player.rect.right = vehicle.rect.left
            crash_rect.center = [player.rect.right, (player.rect.center[1] + vehicle.rect.center[1]) / 2]
          

  # draw th grass
  screen.fill(green)

  # 도로 그리기
  pygame.draw.rect(screen, gray, road)

  # 도로 Edge & marks 그리기
  pygame.draw.rect(screen, yellow, left_edge_marker)
  pygame.draw.rect(screen, yellow, right_edge_marker)

  # lane marker의 y방향으로 움직이기
  lane_marker_move_y += speed * 2
  if lane_marker_move_y >= marker_height * 2:
    lane_marker_move_y = 0

  # lane markers 그리기
  for y in range(marker_height * -2, height, marker_height * 2):
    pygame.draw.rect(screen, white, (left_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
    pygame.draw.rect(screen, white, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))


  # player 자동차 그리기
  player_group.draw(screen)

  # vehicle 그리기
  if len(vehicle_group) < 2:
    add_vehicle = True
    for vehicle in vehicle_group:
      if vehicle.rect.top < vehicle.rect.height * 1.3:
        add_vehicle = False

    if add_vehicle:
      lane = random.choice(lanes)
      image = random.choice(vehicle_images)
      vehicle = Vehicle(image, lane, height / -2)
      vehicle_group.add(vehicle)

  # vehicle 움직이기
  for vehicle in vehicle_group:
    vehicle.rect.y += speed

    # 만약 자동차가 화면을 지나가면, group에서 석재
    if vehicle.rect.top >= height:
      vehicle.kill()

      # score 증가
      score += 1

      # 5대가 지나갈 때 마다 speed를 더 빠르게
      if score > 0 and score % 5 == 0:
        speed += 1

  # vehicle을 화면에 그리기
  vehicle_group.draw(screen)

  # 점수 나타내기
  font = pygame.font.Font(pygame.font.get_default_font(), 16)
  text = font.render('Score : ' + str(score), True, white)
  text_rect = text.get_rect()
  text_rect.center = (50, 400)
  screen.blit(text, text_rect)

  # 정면 충돌할 경우
  if pygame.sprite.spritecollide(player, vehicle_group, True):
    gameover = True
    crash_rect.center = [player.rect.center[0], player.rect.top]

  # 충돌 시, game over 표시
  
  if gameover:
    screen.blit(crash, crash_rect)

    pygame.draw.rect(screen, red, (0, 50, width, 100))

    font = pygame.font.Font(pygame.font.get_default_font(), 15)
    text = font.render('Game Over, Play again? (Enter Y or N)', True, white)
    text_rect = text.get_rect()
    text_rect.center = (width / 2, 100)
    screen.blit(text, text_rect)

  pygame.display.update()

  while gameover:
    clock.tick(fps)

    for event in pygame.event.get():
      if event.type == QUIT:
        gameover = False
        running = False

      if event.type == KEYDOWN:
        if event.key == K_y:
          gameover = False
          speed = 2
          score = 0
          vehicle_group.empty()
          player.rect.center = [player_x, player_y]
        elif event.key == K_n:
          gameover = False
          running = False

pygame.quit()