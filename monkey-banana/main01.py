import pygame

(numpass, numfail) = pygame.init()

print("성공적으로 초기화된 모듈 수 : ", numpass)

is_inititalized = pygame.get_init()

print("pygame이 성공적으로 초기화 되었나요? : ", is_inititalized)