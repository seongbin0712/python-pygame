import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))

pygame.display.set_caption("test")

# None의 의미는 기본폰트를 사용한다는 의미...
font_test = pygame.font.SysFont(None, 30)

total = 123

play = True
while play:
  for event in pygame.event.get():
    if event.type ==pygame.QUIT:
      play = False

  # True는 글자를 조금 더 부드럽게 보이게 하기 위한 것임...
  text = font_test.render(str(total), True, (255, 255, 255))
  background.blit(text, (210, 180))
  pygame.display.update()

pygame.quit()