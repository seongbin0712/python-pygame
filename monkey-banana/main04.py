import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("Monkey Bananas")

fps = pygame.time.Clock()

x_pos = background.get_size()[0] // 2
y_pos = background.get_size()[1] // 2

to_x = 0
to_y = 0

play = True
while play:

  # 1초 동안에 while문을 몇 번 실행할 것인지를 설정함...
  daltaTime = fps.tick(60)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        to_y = -1
        print("UP")
      elif event.key == pygame.K_DOWN:
        to_y = 1
        print("DOWN")
      elif event.key == pygame.K_LEFT:
        to_x = -1
        print("LEFT")
      elif event.key == pygame.K_RIGHT:
        to_x = 1
        print("RIGHT")

    if event.type == pygame.KEYUP:
      # 키보드를 때는 순간에 증가량이 0이 된다.
      to_x = 0
      to_y = 0

  x_pos += to_x
  y_pos += to_y

  background.fill((255, 0, 0))

  pygame.draw.circle(background, (0, 0, 255), (x_pos, y_pos), 5)

  pygame.display.update()

pygame.quit()