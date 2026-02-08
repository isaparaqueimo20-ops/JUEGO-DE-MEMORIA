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

ventana = pygame.display.set_mode((constantes.ANCHO, constantes.ALTO))
pygame.display.set_caption("Juego de Memoria")

fondo = pygame.transform.scale(constantes.FONDO, (constantes.ANCHO, constantes.ALTO))
reloj = pygame.time.Clock()

#bucle principal del juego
running = True
while running:
    dificultad = ejecutar_menu(ventana, reloj)

    if dificultad is None:
        running = False
        break

    print("Dificultad elegida:", dificultad)
    ejecutar_juego(ventana, reloj, dificultad)

pygame.quit()
sys.exit()
    
        
'''if __name__ == "__main__":
    # Se instancia y se corre. 
    # El Core ya sabe qué hacer porque la lógica está en la base.
    game = Memoria()
    game.run_preview()'''