import random
import pygame
import sys
import constantes

fondo = pygame.transform.scale(constantes.FONDO, (constantes.ANCHO, constantes.ALTO))

def crear_cartas(pares):
    cartas = []

    if pares <= 6:      # Fácil
        columnas, filas = 4, 3
        ancho, alto = 100, 90
    elif pares <= 12:   # Medio  
        columnas, filas = 4, 4
        ancho, alto = 90, 80
    else:              # Difícil (18)
        columnas, filas = 6, 6
        ancho, alto = 80, 70
    
    margen = 18

    #cargar imagenes
    imagenes = []
    for i in range(1, pares+1):
        try:
            img = pygame.image.load(f"Assets/Images/{i}.png")
        except:
            try:
                img = pygame.image.load(f"Assets/Images/{i}.jpg")
            except:
                img = pygame.Surface((ancho, alto))
                img.fill((random.randint(100,255), 100, 150))
        
        img = pygame.transform.scale(img, (ancho, alto))
        imagenes.append(img)
        imagenes.append(img)  # Pareja

    random.shuffle(imagenes)
    
    ancho_total = columnas * ancho + (columnas - 1) * margen
    x_inicial = (constantes.ANCHO - ancho_total) // 2
    
    alto_total = filas * alto + (filas - 1) * margen
    y_inicial = (constantes.ALTO - alto_total) // 2
    
    # Crear cartas con posiciones perfectas
    idx = 0
    for fila in range(filas):
        for col in range(columnas):
            if idx < len(imagenes):  # No exceder cartas disponibles
                x = x_inicial + col * (ancho + margen)
                y = y_inicial + fila * (alto + margen)
                
                carta = {
                    "imagen": imagenes[idx],
                    "rect": pygame.Rect(x, y, ancho, alto),
                    "visible": False,
                    "emparejada": False
                }
                cartas.append(carta)
                idx += 1
    
    return cartas

seleccionadas = []
pares_encontrados = 0

# Función para verificar pares
def verificar_par():
    global seleccionadas, pares_encontrados
    c1, c2 = seleccionadas
    if c1["imagen"] == c2["imagen"]:
        c1["visible"] = True
        c2["visible"] = True
        pares_encontrados += 1
    else:
        pygame.time.delay(600)
        c1["emparejada"] = False
        c2["emparejada"] = False
    seleccionadas = []

def ejecutar_juego(ventana, reloj, dificultad):
   
    cartas = crear_cartas(dificultad)
    
    seleccionadas = []
    pares_encontrados = 0
    esperando_verificacion = False
    tiempo_voltear_atras = 0

    jugando = True
    while jugando:
        reloj.tick(constantes.FPS)

        ventana.blit(fondo, (0, 0))

        for evento in pygame.event.get(): 
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    jugando = False
            
            if (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 
                and not esperando_verificacion):
                    for carta in cartas:
                        if (carta["rect"].collidepoint(evento.pos) and 
                            not carta["visible"] and 
                            not carta["emparejada"] and
                            len(seleccionadas) < 2 ):
                            carta["visible"] = True
                            seleccionadas.append(carta)

            if len(seleccionadas) == 2 and not esperando_verificacion:
                esperando_verificacion = True
                tiempo_voltear_atras = pygame.time.get_ticks()

            if esperando_verificacion:
                tiempo_actual = pygame.time.get_ticks()
                if tiempo_actual - tiempo_voltear_atras > 800:
                    c1, c2 = seleccionadas
                    if c1["imagen"] == c2["imagen"]:
                        c1["emparejada"] = True
                        c2["emparejada"] = True
                        pares_encontrados += 1
                    else:
                        # voltear
                        c1["visible"] = False
                        c2["visible"] = False
                
                    seleccionadas = []
                    esperando_verificacion = False

        #DIBUJAR CARTAS 
        for carta in cartas:
            if carta["visible"] or carta["emparejada"]:
                ventana.blit(carta["imagen"], carta["rect"])
            else:
                pygame.draw.rect(ventana, (70, 130, 180), carta["rect"])
                
        # Mensaje si se completan todos los pares
        if pares_encontrados == dificultad:
            fuente = pygame.font.SysFont(None, 50)
            texto = fuente.render("¡Nivel completado!", True, constantes.MORADO)
            ventana.blit(texto, texto.get_rect(center=(constantes.ANCHO//2, 50)))


        # Texto dificultad
        fuente =  pygame.font.SysFont(None, 30)
        texto = fuente.render(f"Dificultad: {dificultad} pares",True, constantes.AZUL_P)
        ventana.blit(texto, (10, 20))

        pygame.display.update()
