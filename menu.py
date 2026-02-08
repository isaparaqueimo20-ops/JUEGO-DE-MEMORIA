import pygame
import sys
import constantes
from constantes import DIFICULTAD


def ejecutar_menu(ventana, reloj):
    pygame.display.set_caption("Menú")

    fondo = pygame.transform.scale(constantes.FONDO,(constantes.ANCHO, constantes.ALTO))

    MENU = "menu"
    DIFICULTAD = "dificultad"
    INSTRUCCIONES = "instrucciones"

    estado = MENU

    def dibujar_texto(texto, fuente, color, x, y):
        superficie = fuente.render(texto, True, color)
        rect = superficie.get_rect(center=(x, y))
        ventana.blit(superficie, rect)
        return rect

    while True:
        reloj.tick(constantes.FPS)
        ventana.blit(fondo, (0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if estado == MENU:
                    if boton_dificultad.collidepoint(evento.pos):
                        estado = DIFICULTAD
                    elif boton_instrucciones.collidepoint(evento.pos):
                        estado = INSTRUCCIONES
                    elif boton_salir.collidepoint(evento.pos):
                        pygame.quit()
                        sys.exit()

                elif estado == DIFICULTAD:
                    if boton_facil.collidepoint(evento.pos):
                        return 6
                    elif boton_medio.collidepoint(evento.pos):
                        return 12
                    elif boton_dificil.collidepoint(evento.pos):
                        return 18
                    elif boton_volver.collidepoint(evento.pos):
                        estado = MENU

                elif estado == INSTRUCCIONES:
                    if boton_volver.collidepoint(evento.pos):
                        estado = MENU

        #dibujar menu
        if estado == MENU:
            dibujar_texto(
                "JUEGO DE MEMORIA",
                constantes.fuente_titulo,
                constantes.MORADO_P,
                constantes.ANCHO // 2,
                120
            )

            dibujar_texto(
                "MENÚ PRINCIPAL",
                constantes.fuente_menu,
                constantes.MORADO_P,
                constantes.ANCHO // 2,
                180
            )

            boton_dificultad = dibujar_texto(
                "Elegir dificultad", constantes.fuente_menu, constantes.AZUL_P,
                constantes.ANCHO // 2, 260
            )
            boton_instrucciones = dibujar_texto(
                "Instrucciones", constantes.fuente_menu, constantes.AZUL_P,
                constantes.ANCHO // 2, 320
            )
            boton_salir = dibujar_texto(
                "Salir", constantes.fuente_menu, constantes.AZUL_P,
                constantes.ANCHO // 2, 380
            )

        elif estado == DIFICULTAD:
            dibujar_texto(
                "SELECCIONA DIFICULTAD",
                constantes.fuente_titulo,
                constantes.MORADO_P,
                constantes.ANCHO // 2,
                100
            )

            boton_facil = dibujar_texto(
                "Fácil (6 pares)", constantes.fuente_menu, constantes.AZUL_P,
                constantes.ANCHO // 2, 260
            )
            boton_medio = dibujar_texto(
                "Medio (12 pares)", constantes.fuente_menu, constantes.AZUL_P,
                constantes.ANCHO // 2, 320
            )
            boton_dificil = dibujar_texto(
                "Difícil (18 pares)", constantes.fuente_menu, constantes.AZUL_P,
                constantes.ANCHO // 2, 380
            )
            boton_volver = dibujar_texto(
                "Volver", constantes.fuente_menu, constantes.AZUL_P,
                constantes.ANCHO // 2, 450
            )

        elif estado == INSTRUCCIONES:
            dibujar_texto(
                "INSTRUCCIONES",
                constantes.fuente_titulo,
                constantes.AMARILLO,
                constantes.ANCHO // 2,
                120
            )

            boton_volver = dibujar_texto(
                "Volver", constantes.fuente_menu, constantes.BLANCO,
                constantes.ANCHO // 2, 420
            )

        pygame.display.update()
