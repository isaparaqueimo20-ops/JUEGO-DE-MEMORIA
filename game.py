import random
import pygame
import sys
from pathlib import Path
import constantes
from constantes import DIFICULTAD

fondo = pygame.transform.scale(constantes.FONDO, (constantes.ANCHO, constantes.ALTO))

class Carta:
    def __init__(self, imagen, x, y, ancho, alto):
        self.imagen = imagen
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.visible = False
        self.emparejada = False
    
    def dibujar(self, ventana):
        if self.visible or self.emparejada:
            ventana.blit(self.imagen, self.rect)
        else:
            pygame.draw.rect(ventana, constantes.MORADO_P, self.rect)
    
    def clic_en_carta(self, pos):
        return (self.rect.collidepoint(pos) and 
                not self.visible and 
                not self.emparejada)

class Boton:
    def __init__(self, texto, x, y, ancho, alto, fuente=None, color_texto=constantes.BLANCO, color_fondo=(100, 150, 200)):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = texto
        self.fuente = fuente or pygame.font.SysFont(None, 36)
        self.color_texto = color_texto
        self.color_fondo = color_fondo
        self.superficie_texto = self.fuente.render(texto, True, color_texto)
    
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color_fondo, self.rect)
        pygame.draw.rect(ventana, constantes.BLANCO, self.rect, 3)
        text_rect = self.superficie_texto.get_rect(center=self.rect.center)
        ventana.blit(self.superficie_texto, text_rect)
    
    def clic_en_boton(self, pos):
        return self.rect.collidepoint(pos)

def obtener_config(pares):
    for config in DIFICULTAD.values():
        if config["num_pares"] == pares:
            return config
    return DIFICULTAD["facil"]

def crear_cartas(pares):
    config = obtener_config(pares)
    cartas = []
    ancho, alto = config["ancho_alto"]
    margen = config["margen"]
    columnas, filas = config["columnas"], config["filas"]
    
    # Cargar imágenes
    imagenes = []
    for i in range(1, pares + 1):
        imagen = None
        for ext in ['.png', '.jpg']:
            ruta_img = constantes.IMG_DIR / f"{i}{ext}"
            try:
                imagen_original = pygame.image.load(str(ruta_img)).convert_alpha()
                imagen = pygame.transform.scale(imagen_original, (ancho, alto))
                #print(f"Cargada: {ruta_img}")
                break
            except (FileNotFoundError, pygame.error):
                continue
    
        # Fallback si nada funciona
        if imagen is None:
            print(f"No se pudo cargar {i}.png/.jpg. Usando color.")
            imagen = pygame.Surface((ancho, alto))
            imagen.fill((random.randint(100, 255), 100, 150))
    
        imagenes.append(imagen)
        imagenes.append(imagen)  # Pareja

    random.shuffle(imagenes)
    
    # Posiciones centradas
    ancho_total = columnas * ancho + (columnas - 1) * margen
    x_inicial = (constantes.ANCHO - ancho_total) // 2
    alto_total = filas * alto + (filas - 1) * margen
    y_inicial = (constantes.ALTO - alto_total) // 2
    
    idx = 0
    for fila in range(filas):
        for col in range(columnas):
            if idx < len(imagenes):
                x = x_inicial + col * (ancho + margen)
                y = y_inicial + fila * (alto + margen)
                carta = Carta(imagenes[idx], x, y, ancho, alto)
                cartas.append(carta)
                idx += 1
    return cartas

def ejecutar_juego(ventana, reloj, dificultad):
        
    config = DIFICULTAD[dificultad]
    num_pares = config["num_pares"]

    cartas = crear_cartas(num_pares)
    
    tiempo_agotado = False
    
    tiempo_limite = config["tiempo"]  # en segundos
    tiempo_inicio = pygame.time.get_ticks()
    
    seleccionadas = []
    pares_encontrados = 0
    esperando_verificacion = False
    tiempo_voltear_atras = 0
    
    # Botones de juego
    btn_reiniciar = Boton("Reiniciar", 10, constantes.ALTO - 60, 120, 50)
    btn_menu = Boton("Menú", 140, constantes.ALTO - 60, 120, 50)

    jugando = True
    while jugando:
        reloj.tick(constantes.FPS)
        ventana.blit(fondo, (0, 0))
        
        # temporizador
        if tiempo_limite:  # Solo si la dificultad tiene tiempo
            tiempo_actual = pygame.time.get_ticks()
            tiempo_transcurrido = (tiempo_actual - tiempo_inicio) // 1000
            tiempo_restante = tiempo_limite - tiempo_transcurrido

            if tiempo_restante <= 0:
                tiempo_restante = 0
                tiempo_agotado = True
        else:
            tiempo_restante = None


        for evento in pygame.event.get(): 
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                jugando = False
            
            if (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 
                and not esperando_verificacion and not tiempo_agotado):
                
                # Clic en cartas
                for carta in cartas:
                    if carta.clic_en_carta(evento.pos) and len(seleccionadas) < 2:
                        carta.visible = True
                        seleccionadas.append(carta)
                
                # Clic en botones
                if btn_reiniciar.clic_en_boton(evento.pos):
                    return "reiniciar" 
                if btn_menu.clic_en_boton(evento.pos):
                    return "menu"

        # Lógica de pares
        if len(seleccionadas) == 2 and not esperando_verificacion:
            esperando_verificacion = True
            tiempo_voltear_atras = pygame.time.get_ticks()

        if esperando_verificacion:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - tiempo_voltear_atras > 800:
                c1, c2 = seleccionadas
                if c1.imagen == c2.imagen: 
                    c1.emparejada = True
                    c2.emparejada = True
                    pares_encontrados += 1
                else:
                    c1.visible = False
                    c2.visible = False
                
                seleccionadas = []
                esperando_verificacion = False

        # Dibujar cartas con CLASE
        for carta in cartas:
            carta.dibujar(ventana)
        
        # Dibujar botones
        btn_reiniciar.dibujar(ventana)
        btn_menu.dibujar(ventana)
        
        # Textos con DIFICULTAD
        fuente = pygame.font.SysFont(None, 28)
        nombre_dif = next(k for k, v in DIFICULTAD.items() if v["num_pares"] == num_pares)
        texto_dif = fuente.render(f"{nombre_dif.upper()}: {num_pares} pares", True, constantes.AZUL_P)
        ventana.blit(texto_dif, (10, 10))
        
        if tiempo_restante is not None:
            minutos = tiempo_restante // 60
            segundos = tiempo_restante % 60
            tiempo_formateado = f"{minutos:02}:{segundos:02}"

            texto_prog = fuente.render(
                f"{pares_encontrados}/{num_pares} | Tiempo: {tiempo_formateado}",
                True,
                constantes.MORADO_P
         )
        else:
            texto_prog = fuente.render(
                f"{pares_encontrados}/{num_pares} | Tiempo: ∞",
                True,
             constantes.MORADO_P
        )

        ventana.blit(texto_prog, (10, 40))

        # Victoria
        if pares_encontrados == num_pares and not tiempo_agotado:
            fuente_victoria = pygame.font.SysFont(None, 60)
            texto_victoria = fuente_victoria.render("¡Nivel completado!", True, constantes.BLANCO)
            texto_rect_v = texto_victoria.get_rect(center=(constantes.ANCHO//2, constantes.ALTO//2))
            
            fuente_sub = pygame.font.SysFont(None, 32)
            texto_sub = fuente_sub.render("Enter=Menú | R=Reiniciar | ESC=Salir", True, constantes.BLANCO)
            texto_rect_sub = texto_sub.get_rect(center=(constantes.ANCHO//2, constantes.ALTO//2 + 80))
            
            victoria_activa = True
            while victoria_activa:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        return "salir"
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_RETURN:
                            return "menu"
                        if evento.key == pygame.K_r:
                            return "reiniciar"
                        if evento.key == pygame.K_ESCAPE:
                            return "menu"
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        if btn_reiniciar.clic_en_boton(evento.pos):
                            return "reiniciar"
                        if btn_menu.clic_en_boton(evento.pos):
                            return "menu"
                ventana.blit(fondo, (0, 0))
                
                
                for carta in cartas:
                    carta.dibujar(ventana)  # Muestra todas las cartas ganadas
                btn_reiniciar.dibujar(ventana)
                btn_menu.dibujar(ventana)
                
                overlay_victoria = pygame.Surface((constantes.ANCHO, constantes.ALTO))
                overlay_victoria.fill((100, 150, 255))
                overlay_victoria.set_alpha(120)  # Transparencia (0-255)
                ventana.blit(overlay_victoria, (0, 0))
                
                ventana.blit(texto_victoria, texto_rect_v)
                ventana.blit(texto_sub, texto_rect_sub)
                pygame.display.update()
                reloj.tick(60)         
                
            jugando = False
                

        # Derrota por tiempo
        elif tiempo_agotado:
            fuente_derrota = pygame.font.SysFont(None, 60)
            texto_derrota = fuente_derrota.render("¡Tiempo agotado!", True, constantes.BLANCO)
            texto_rect_d = texto_derrota.get_rect(center=(constantes.ANCHO//2, constantes.ALTO//2))
            
            texto_sub_d = fuente_sub.render("Enter=Menú | R=Reiniciar", True, constantes.BLANCO)
            texto_rect_sub_d = texto_sub_d.get_rect(center=(constantes.ANCHO//2, constantes.ALTO//2 + 80))
            
            derrota_activa = True
            while derrota_activa:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        return "salir"
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_RETURN or evento.key == pygame.K_r:
                            return "reiniciar"  # Reinicia por defecto en derrota
                        if evento.key == pygame.K_ESCAPE:
                            return "menu"
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        if btn_reiniciar.clic_en_boton(evento.pos) or btn_menu.clic_en_boton(evento.pos):
                            return "reiniciar"
                
                ventana.blit(fondo, (0, 0))
                
                for carta in cartas:
                    carta.dibujar(ventana)
                btn_reiniciar.dibujar(ventana)
                btn_menu.dibujar(ventana)
                
                overlay_derrota = pygame.Surface((constantes.ANCHO, constantes.ALTO))
                overlay_derrota.fill((150, 50, 50))
                overlay_derrota.set_alpha(140)
                ventana.blit(overlay_derrota, (0, 0))
                
                ventana.blit(texto_derrota, texto_rect_d)
                ventana.blit(texto_sub_d, texto_rect_sub_d)
                pygame.display.update()
                reloj.tick(60)
            jugando = False
             
        pygame.display.update()
