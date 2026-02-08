import pygame

pygame.init()

#Ancho de ventana
ANCHO = 800
ALTO = 600

#fondo de las ventanas 
FONDO = pygame.image.load("Assets/Images/fondo.png")

#Imagenes de las cartas
COLOR_CARTA_ESCONDIDA = ("Assets/Images/escondida.png")

FPS = 60

#colores
BLANCO = (255, 255, 255)
AMARILLO = (255, 220, 0)
MORADO_P = (175, 126, 173)
AZUL_P = (132,182,244)

# Fuente
fuente_titulo = pygame.font.SysFont("arial", 60)
fuente_menu = pygame.font.SysFont("arial", 36)


DIFICULTAD = {
    "facil": {
        "num_pares": 6,
        "ancho_alto": (80, 100),
        "margen": 20,
        "columnas": 4,
        "filas": 3,
        "tiempo": 600  # 10 minutos
    },
    "medio": {
        "num_pares": 12,
        "ancho_alto": (80, 100),
        "margen": 20,
        "columnas": 6,  
        "filas": 4,
        "tiempo": 420  # 7 minutos
    },
    "dificil": {
        "num_pares": 18,
        "ancho_alto": (80, 100),
        "margen": 20,
        "columnas": 6,
        "filas": 6,
        "tiempo": 300  # 5 minutos
    },
    "libre": {
        "num_pares": 16,
        "ancho_alto": (80, 100),
        "margen": 20,
        "columnas": 4,
        "filas": 4,
        "tiempo": None # Sin tiempo límite
    }
}

