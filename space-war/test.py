import pygame
import random

pygame.init()
background = pygame.display.set_mode((480, 360))
image_pico = pygame.image.load("images/pico-1.png")
image_rocket = pygame.image.load("images/rocket-1.png")

rect_pico = image_pico.get_rect()
rect_rocket = image_rocket.get_rect()

x_pos_pico = 100
y_pos_pico = 100

x_pos_rocket = 200
y_pos_rocket = 200

rect_pico.topleft = (x_pos_pico, y_pos_pico)
rect_rocket.topleft = (x_pos_rocket, y_pos_rocket)

play = True
while play:
  for event in pygame.event.get():
    if  event.type == pygame.QUIT:
      play = False

  if rect_rocket.colliderect(rect_pico):
    print("충돌")

  background.blit(image_pico, (x_pos_pico, y_pos_pico))
  background.blit(image_rocket, (x_pos_rocket, y_pos_rocket))

  pygame.display.update()

pygame.quit()