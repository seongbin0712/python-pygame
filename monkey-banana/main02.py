import pygame

# pygame 초기화
pygame.init()

# pygame 창 크기를 설정
surface = pygame.display.set_mode((400, 400)) # 가로, 세로 크기는 Tuple로 지정한다.

# 창의 이름을 설정
pygame.display.set_caption("My Game")

# 창의 icon 바꾸기(설정)
icon = pygame.image.load('./images/bananas.png')
pygame.display.set_icon(icon)

# RGB color 설정
color = (255, 0, 0)

#surface 색상 지정
surface.fill(color)

running = True

pygame.display.flip() # surface 내용을 update 하는데 사용한다.
# pygame.display.update()

while running:

  # Event 처리 for문...
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

pygame.quit()