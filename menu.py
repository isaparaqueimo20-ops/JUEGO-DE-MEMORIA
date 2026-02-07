import pygame
from constantes import NIVEL

class Menu:
    def manejar_eventos(self, eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    return NIVEL

    def dibujar(self, ventana):
        ventana.fill((40, 40, 40))
        