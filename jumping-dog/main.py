import pygame
import sys

# 초기화
pygame.init()
pygame.display.set_caption('Jumping Dog')
MAX_WIDTH = 800
MAX_HEIGHT = 400

# 창 만들기
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))

fps = pygame.time.Clock()

# dog 이미지 로드
imgdog1 = pygame.image.load('images/dog1.png')
imgdog2 = pygame.image.load('images/dog2.png')

# dog height, bottom 구하기

dog_height = imgdog1.get_size()[1]
dog_bottom = MAX_HEIGHT - dog_height

# 전역변수 설정
dog_x = 50
dog_y = dog_bottom

jump_top = 200
leg_swap = True
is_bottom = True
is_go_up = False

# tree 이미지 로드
imgtree = pygame.image.load('images/tree.png')
tree_height = imgtree.get_size()[1]
tree_x = MAX_WIDTH
tree_x = MAX_HEIGHT - tree_height

while True:
  screen.fill((255, 255, 255))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      if is_bottom:
        is_go_up = True
        is_bottom = False

  if is_go_up:
    dog_y -= 10.0
  elif not is_go_up and not is_bottom:
    dog_y += 10.0

  # dog의 top과 bottom을 check
  if is_go_up and dog_y <= jump_top:
    is_go_up = False

  if not is_bottom and dog_y >= dog_bottom:
    is_bottom = True
    dog_y = dog_bottom

  # tree 움직이기
  tree_x -= 12.0
  if tree_x <= 0:
    tree_x = MAX_WIDTH

  screen.blit(imgtree(tree_x, tree_y))

  if leg_swap:
    screen.blit(imgdog1, (dog_x, dog_y))
    leg_swap = False
  else:
    screen.blit(imgdog1, (dog_x, dog_y))
    leg_swap = True

  pygame.display.update()
  fps.tick(30)