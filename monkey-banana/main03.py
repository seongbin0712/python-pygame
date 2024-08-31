import pygame

pygame.init()


sample_surface = pygame.display.set_mode((400, 300))
# sample_surface.fill((255, 0, 0))
image = pygame.image.load("./images/bananas.png")
sample_surface.blit(image, (35, 37))
sample_surface.blit(image, (150, 150))

color = (255, 255, 0)
pygame.draw.rect(sample_surface, color, pygame.Rect(30, 30, 90, 90), 5)

pygame.display.update()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

pygame.quit()