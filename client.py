import sys, pygame
# @Hardcoded :- fix this later
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Client")

class Entity():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.c = color
        self.rect = (x, y, width, height)

    def draw(self, win):
        pygame.draw.rect(win, self.c, self.rect)

    def move(self):
        pygame.init()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.x -= 0.1
        if pressed[pygame.K_RIGHT]:
            self.x += 0.1
        if pressed[pygame.K_UP]:
            self.y -= 0.1
        if pressed[pygame.K_DOWN]:
            self.y += 0.1

        self.rect = (self.x, self.y, self.w, self.h)

        


def redrawWindow(win, entity):
    win.fill((255, 255, 255))
    entity.draw(win)
    pygame.display.flip()


def main():
    p = Entity(50, 50, 25, 25, (75, 125, 255))

    run = True
    while run:
        print("Running")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win, p)
main()