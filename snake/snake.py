import pygame
import sys
import random

# Initialisatie van Pygame
pygame.init()

# Scherm instellen
width = 600
height = 400
cell_size = 20
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Kleuren instellen
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Slangklasse
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((width // 2), (height // 2))]
        self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])  # Richtingen als tuples
        self.color = green

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * cell_size)) % width), (cur[1] + (y * cell_size)) % height)
        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((width // 2), (height // 2))]
        self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])  # Opnieuw instellen van de richting

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (cell_size, cell_size))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, black, r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_UP:
                    self.turn((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.turn((0, 1))
                elif event.key == pygame.K_LEFT:
                    self.turn((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.turn((1, 0))

# Voedselklasse
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = red
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (width // cell_size) - 1) * cell_size,
                         random.randint(0, (height // cell_size) - 1) * cell_size)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (cell_size, cell_size))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, black, r, 1)

# Tekenen van het raster
def draw_grid(surface):
    for y in range(0, height, cell_size):
        for x in range(0, width, cell_size):
            r = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(surface, white, r, 1)

# Main functie
def main():
    # Slang en voedsel instellen
    snake = Snake()
    food = Food()
    clock = pygame.time.Clock()

    while True:
        screen.fill(black)  # Achtergrond wissen
        draw_grid(screen)   # Raster tekenen
        snake.handle_keys() # Toetsenbord invoer verwerken
        snake.move()        # Slang laten bewegen

        # Controleer of slang voedsel heeft gegeten
        if snake.get_head_position() == food.position:
            food.randomize_position()
            snake.length += 1

        snake.draw(screen)  # Slang tekenen
        food.draw(screen)   # Voedsel tekenen
        pygame.display.update() # Scherm bijwerken
        clock.tick(10)      # Frame rate instellen

if __name__ == "__main__":
    main()
