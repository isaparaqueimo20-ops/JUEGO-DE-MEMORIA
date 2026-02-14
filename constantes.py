import pygame
from pathlib import Path

pygame.init()

BASE_DIR = Path(__file__).resolve().parent

# 2. Definir carpetas de recursos
ASSETS_DIR = BASE_DIR / "Assets"
IMG_DIR = ASSETS_DIR / "Images"
SND_DIR = ASSETS_DIR / "Sonido"
IMG_DIRS = {
    "facil": IMG_DIR / "facil",
    "medio": IMG_DIR / "medio",
    "dificil": IMG_DIR / "dificil",
    "libre": IMG_DIR / "libre"
}


#Ancho de ventana
ANCHO = 1280
ALTO = 720

#fondo de las ventanas 
FONDO = pygame.image.load(str(IMG_DIR / "fondo.png"))

#Imagenes de las cartas
CARTA_VOLTEADA = (str(IMG_DIR / "volteada.png"))

FPS = 60

#colores
BLANCO = (255, 255, 255)
MORADO_P = (175, 126, 173)
AZUL_P = (132,182,244)


# Fuente
fuente_titulo = pygame.font.SysFont("arial", 60)
fuente_menu = pygame.font.SysFont("arial", 36)


DIFICULTAD = {
    "facil": {
        "num_pares": 6,
        "ancho_alto": (120, 110),
        "margen": 20,
        "columnas": 4,
        "filas": 3,
        "tiempo": 600  # 10 minutos
    },
    "medio": {
        "num_pares": 8,
        "ancho_alto": (110, 100),
        "margen": 20,
        "columnas": 4,  
        "filas": 4,
        "tiempo": 420  # 7 minutos
    },
    "dificil": {
        "num_pares": 12,
        "ancho_alto": (100, 90),
        "margen": 20,
        "columnas": 6,
        "filas": 4,
        "tiempo": 300  # 5 minutos
    },
    "libre": {
        "num_pares": 10,
        "ancho_alto": (120, 110),
        "margen": 20,
        "columnas": 4,
        "filas": 4,
        "tiempo": None # Sin tiempo límite
    }
}

MUSICA_FONDO = SND_DIR / "sonido_fondo.mp3"
SONIDO_ACTIVADO = True  # ← Variable global