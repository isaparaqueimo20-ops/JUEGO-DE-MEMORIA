import pygame, sys
#from enfocate import GameBase, GameMetadata, COLORS
import constantes
from menu import ejecutar_menu
from game import ejecutar_juego

'''class Memoria(GameBase):
    def __init__(self) -> None:
        # 1. Registro de información técnica del juego
        meta = GameMetadata(
            title="Juego de Memoria",
            description="Breve descripción.",
            authors=["Nombre Apellido 1", "Nombre Apellido 2"],
            group_number=9
        )
        
        # 2. Inyección de metadatos al Core
        super().__init__(meta)
        
        # 3. Inicialización de estado interno
        self.puntuacion = 0

    def on_start(self):
        """Carga de recursos dinámicos (assets)."""
        pass

    def update(self, dt: float):
        """Actualización de lógica física y estados (dt = delta time)."""
        pass

    def draw(self):
        """Renderizado en la superficie inyectada por el motor."""
        self.surface.fill(COLORS["carbon_oscuro"])'''
        
pygame.init()

try:
    pygame.mixer.init()
except:
    print("Error inicializando el mixer")

ventana = pygame.display.set_mode((constantes.ANCHO, constantes.ALTO))
reloj = pygame.time.Clock()
pygame.display.set_caption("Juego Memoria")

pygame.mixer.music.load(str(constantes.SND_DIR / "sonido_fondo.mp3"))
if constantes.SONIDO_ACTIVADO:
    pygame.mixer.music.play(-1)

running = True

while running:

    dificultad = ejecutar_menu(ventana, reloj)

    if constantes.SONIDO_ACTIVADO:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()

    if dificultad is None:
        break

    while True:
        resultado = ejecutar_juego(ventana, reloj, dificultad)

        if constantes.SONIDO_ACTIVADO:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()

        if resultado in ["menu", None]:
            break

        elif resultado == "salir":
            running = False
            break

pygame.quit()
sys.exit()

    
        
'''if __name__ == "__main__":
    # Se instancia y se corre. 
    # El Core ya sabe qué hacer porque la lógica está en la base.
    game = Memoria()
    game.run_preview()'''
    