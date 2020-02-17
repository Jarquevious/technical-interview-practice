import pygame, sys, os

class SlidePuzzle:
    def __init__(self, gs, ts, ms):
        self.gs = gs
        self.ts = ts
        self.ms = ms
        self.tiles_len = gs[0]*gs[1]-1
        self.titles = [(x,y) for y in range(gs[1])] fir x in range(gs[0])

    def update(self,dt):
        pass
    def draw(self,screen):
        for i in range(self.tiles_len)


def main():
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption('Slide Puzzle')
    screen = pygame.display.set_mode((800,600))
    fpsclock = pygme.time.Clock()
    program = SlidePuzzle((3,3), 100, 5)

    while True:
        dt  fpsclock.tick()/1000
        screen.fill((0,0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quite();
            sys.exit()
        sys.exit()

if __name__ == '__main__':
    main()