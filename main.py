import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 680
NUM_STARS = 400
stars = []
LEFT = -1
RIGHT = 1

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Starfield Warp Drive")
clock = pygame.time.Clock()
dt = clock.tick(60) / 1000 # limits FPS to 60

class Star():
    def __init__(self, size, speed, surface):
        self.size = size
        self.speed = speed
        self.surface = surface

        self.pos = [0, 0] # will change after this instantiation
        self.dir = [0, 0]

        self.start_x = 0
        self.start_y = 0

        self.dx = 1
        self.dy = 1

        self.colour = (255, 255, 255)
        self.centre = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def gen_star(self):
        self.pos[0] = random.randint(-SCREEN_WIDTH, SCREEN_WIDTH)
        self.pos[1] = random.randint(-SCREEN_HEIGHT, SCREEN_HEIGHT)
        self.start_x = self.pos[0]
        self.start_y = self.pos[1]

        if (self.pos[0] >= SCREEN_WIDTH//2): 
            self.dir[0] = abs((self.pos[0] - SCREEN_WIDTH//2) / SCREEN_WIDTH)
        else: 
            self.dir[0] = abs((self.pos[0] - SCREEN_WIDTH//2) / SCREEN_WIDTH) * -1 #random.randint(0, SCREEN_WIDTH) / SCREEN_WIDTH  

        if (self.pos[1] >= SCREEN_HEIGHT//2):
            self.dir[1] = abs((self.pos[1] - SCREEN_HEIGHT//2) / SCREEN_HEIGHT)
        else:
            self.dir[1] = abs((self.pos[1] - SCREEN_HEIGHT//2) / SCREEN_HEIGHT) * -1

    def draw_star(self):
        pygame.draw.circle(screen, self.colour, (self.pos[0], self.pos[1]), self.size//2)

    def move_star(self, speed_incr):
        #print("dir: ", self.dir)
        self.pos[0] += self.dir[0] * self.speed * dt
        self.pos[1] += self.dir[1] * self.speed * dt

        if self.pos[0] < 0 or self.pos[0] > screen.get_width() or self.pos[1] < 0 or self.pos[1] > screen.get_height():
            self.gen_star()
            self.speed = 0

        # Recalculate speed
        self.speed += speed_incr #50
    
        # Calculate the change in x and y
        if (self.pos[0] >= SCREEN_WIDTH//2): 
            self.dx = self.start_x + (self.speed * self.dir[0])
        else:
            self.dx = self.start_x + (self.speed * self.dir[0])

        if (self.pos[1] >= SCREEN_HEIGHT//2): 
            self.dy = self.start_y + (self.speed * self.dir[1])
        else:
            self.dy = self.start_y + (self.speed * self.dir[1])
        
    def draw_line(self, line_thickness):
        pygame.draw.line(screen, (255, 255, 255), (self.pos[0], self.pos[1]), (self.dx, self.dy), line_thickness)#(self.pos[0] + self.dx, self.pos[1] + self.dy), 2)

def main():
    pg_surf = pygame.Surface((20, 20))

    stars = []
    for i in range(NUM_STARS):
        new_star = Star(10, 100, pg_surf)
        new_star.gen_star()
        stars.append(new_star)

    running = True
    while running:
        screen.fill((0, 0, 0))
        mouse_pos = pygame.mouse.get_pos()
        speed_increase = int((mouse_pos[0] / screen.get_width()) * 150)
        line_thickness = int((mouse_pos[1] / screen.get_height()) * 6)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for _, star in enumerate(stars):
            star.move_star(speed_increase)
            #star.draw_star()
            star.draw_line(line_thickness)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000 # limits FPS to 60

if __name__ == "__main__":
    main()