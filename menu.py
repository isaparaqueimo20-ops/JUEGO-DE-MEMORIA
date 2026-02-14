import pygame
import sys
import constantes
from constantes import DIFICULTAD

def ejecutar_menu(ventana, reloj):

    pygame.display.set_caption("Menú")

    fondo = pygame.transform.scale(
        constantes.FONDO,
        (constantes.ANCHO, constantes.ALTO)
    )


    ESTADO_MENU = "menu"
    ESTADO_DIFICULTAD = "dificultad"
    ESTADO_INSTRUCCIONES = "instrucciones"

    estado = ESTADO_MENU
    sonido_menu = constantes.SONIDO_ACTIVADO

    def dibujar_texto(texto, fuente, color, x, y):
        superficie = fuente.render(texto, True, color)
        rect = superficie.get_rect(center=(x, y))
        ventana.blit(superficie, rect)
        return rect


    while True:

        reloj.tick(constantes.FPS)
        ventana.blit(fondo, (0, 0))

        # -------- EVENTOS --------
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if estado == ESTADO_MENU:
                    if boton_dificultad.collidepoint(evento.pos):
                        estado = ESTADO_DIFICULTAD
                    elif boton_instrucciones.collidepoint(evento.pos):
                        estado = ESTADO_INSTRUCCIONES
                    elif boton_salir.collidepoint(evento.pos):
                        return None
                    if boton_sonido.collidepoint(evento.pos):
                        constantes.SONIDO_ACTIVADO = not constantes.SONIDO_ACTIVADO
                            # Apaga o enciende música
                        if pygame.mixer.get_init():
                            if constantes.SONIDO_ACTIVADO:
                                if not pygame.mixer.music.get_busy():
                                    pygame.mixer.music.play(-1)
                                else:
                                    pygame.mixer.music.unpause()
                            else:
                                pygame.mixer.music.pause()

                elif estado == ESTADO_DIFICULTAD:
                    if boton_facil.collidepoint(evento.pos):
                        return "facil"
                    elif boton_medio.collidepoint(evento.pos):
                        return "medio"
                    elif boton_dificil.collidepoint(evento.pos):
                        return "dificil"
                    elif boton_libre.collidepoint(evento.pos):
                        return "libre"
                    elif boton_volver.collidepoint(evento.pos):
                        estado = ESTADO_MENU

                elif estado == ESTADO_INSTRUCCIONES:
                    if boton_volver.collidepoint(evento.pos):
                        estado = ESTADO_MENU

        # -------- DIBUJAR --------
        if estado == ESTADO_MENU:

            dibujar_texto("JUEGO DE MEMORIA",
                          constantes.fuente_titulo,
                          constantes.MORADO_P,
                          constantes.ANCHO // 2, 120)

            boton_dificultad = dibujar_texto(
                "Elegir dificultad",
                constantes.fuente_menu,
                constantes.AZUL_P,
                constantes.ANCHO // 2, 260)

            boton_instrucciones = dibujar_texto(
                "Instrucciones",
                constantes.fuente_menu,
                constantes.AZUL_P,
                constantes.ANCHO // 2, 320)

            boton_salir = dibujar_texto(
                "Salir",
                constantes.fuente_menu,
                constantes.AZUL_P,
                constantes.ANCHO // 2, 380)
            
            boton_sonido = dibujar_texto(
                f"Sonido: {'ON' if constantes.SONIDO_ACTIVADO else 'OFF'}",
                constantes.fuente_menu,
                constantes.AZUL_P,
                constantes.ANCHO - 100, 50
            )


        elif estado == ESTADO_DIFICULTAD:

            dibujar_texto("SELECCIONA DIFICULTAD",
                          constantes.fuente_titulo,
                          constantes.MORADO_P,
                          constantes.ANCHO // 2, 100)

            boton_facil = dibujar_texto("Fácil (6 pares)",
                                        constantes.fuente_menu,
                                        constantes.AZUL_P,
                                        constantes.ANCHO // 2, 200)

            boton_medio = dibujar_texto("Medio (8 pares)",
                                        constantes.fuente_menu,
                                        constantes.AZUL_P,
                                        constantes.ANCHO // 2, 260)

            boton_dificil = dibujar_texto("Difícil (12 pares)",
                                          constantes.fuente_menu,
                                          constantes.AZUL_P,
                                          constantes.ANCHO // 2, 320)

            boton_libre = dibujar_texto("Libre (10 pares)",
                                        constantes.fuente_menu,
                                        constantes.AZUL_P,
                                        constantes.ANCHO // 2, 380)

            boton_volver = dibujar_texto("Volver",
                                         constantes.fuente_menu,
                                         constantes.AZUL_P,
                                         constantes.ANCHO // 2, 450)

        elif estado == ESTADO_INSTRUCCIONES:

            dibujar_texto("INSTRUCCIONES",
                          constantes.fuente_titulo,
                          constantes.MORADO_P,
                          constantes.ANCHO // 2, 120)

            boton_volver = dibujar_texto("Volver",
                                         constantes.fuente_menu,
                                         constantes.BLANCO,
                                         constantes.ANCHO // 2, 420)


        pygame.display.update()
