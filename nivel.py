import pygame
from constantes import FINAL

class Nivel:
    def __init__(self, numero):
        self.numero = numero

    def manejar_eventos(self, eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    return FINAL

    def dibujar(self, ventana):
        ventana.fill((0, 120, 255))