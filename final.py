import pygame
from constantes import MENU

class Final:
    def manejar_eventos(self, eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    return MENU

    def dibujar(self, ventana):
        ventana.fill((20, 150, 80))