import pygame
from random import randrange

def events_tick():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False


def logic_tick(screensize, starfield, depth):
    move_stars(screensize, starfield, depth)


def graphics_tick(screen, starfield, depth):
    screen.fill((0, 22, 33))

    for star in starfield:
        draw_star(screen, star, depth)

    pygame.display.flip()


def draw_star(screen, star, depthmax):
    x, y, depth = star
    colour    = int(255 * (1 - (float(depth)/float(depthmax+1))))
    colour    = (colour, colour, colour)
    trail_len = (depthmax - depth - 1)
    pygame.draw.line(screen, colour, (x, y), (x+trail_len, y))


def move_stars(screensize, starfield, depthmax):
    speed = 0.5
    width, height = screensize

    for i in range(len(starfield)):
        x, y, depth = starfield[i]

        if x < 0:
            # Create a new star
            x, y, depth = random_star(width, height, depthmax, new=True)

        move_multiplier = depthmax * (1 - float(depth)/float(depthmax+1))
        
        x = x - (speed*move_multiplier)
        
        starfield[i] = x, y, depth


def generate_starfield(screensize, numstars, depth):
    width, height = screensize
    return [random_star(width, height, depth) for _ in xrange(numstars)]

def random_star(widthmax, heightmax, depthmax, new = False):
    return (randrange(widthmax) if not new else widthmax,
            randrange(heightmax),
            randrange(depthmax))

def main():
    pygame.init()

    screensize = (1000, 500)
    depth = 8

    screen = pygame.display.set_mode(screensize)
    pygame.display.set_caption("Stars")

    starfield = generate_starfield(screensize, 100, depth)
    clock = pygame.time.Clock() 
    quit  = False
    while not quit:
        quit = events_tick()
        logic_tick(screensize, starfield, depth)
        graphics_tick(screen, starfield, depth)
        clock.tick(100)

    pygame.quit()
           

if __name__ == '__main__':
    main()
