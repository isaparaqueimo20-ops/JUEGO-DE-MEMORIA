import pygame, sys
import constantes
from constantes import NIVEL, MENU, FINAL
from nivel import Nivel


pygame.init()
ventana = pygame.display.set_mode((constantes.ANCHO, constantes.ALTO))
pygame.display.set_caption("Juego de Memoria")

fondo = pygame.transform.scale(constantes.FONDO, (constantes.ANCHO, constantes.ALTO))
reloj = pygame.time.Clock()

class Menu:
    def manejar_eventos(self, eventos):
        for event in eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return NIVEL

    def actualizar(self):
        pass

    def dibujar(self, ventana):
        pass

pantalla = Menu()
Running = True

while Running:
    reloj.tick(constantes.FPS)
    eventos = pygame.event.get()

    for event in eventos:
        if event.type == pygame.QUIT:
            Running = False

    nuevo_estado = pantalla.manejar_eventos(eventos)

    if nuevo_estado == NIVEL:
        pantalla = Nivel(1)
    elif nuevo_estado == MENU:
        pantalla = Menu()

    ventana.blit(fondo, (0, 0))
    pantalla.actualizar()
    pantalla.dibujar(ventana)
    
    pygame.display.update()

pygame.quit()
sys.exit()