import pygame


class obstacle:
    def __init__(self, color, x, y, orientation):
        self.x = x
        self.y = y
        self.color = color
        self.orient = orientation


    def draw(self, screen, thick):
        if self.orient == 0:
            pygame.draw.rect(screen, self.color, (self.x, self.y, screen.get_width(), 50), thick)
        elif self.orient == 90:
            pygame.draw.rect(screen, self.color, (self.x, self.y, 50, screen.get_height()),thick)
        elif self.orient == 45:
            points = [(0, 0 - 30),
                      (0 - 30, 0),
                      (screen.get_width(), screen.get_height() + 30),
                      (screen.get_width() + 30, screen.get_height())]
            pygame.draw.polygon(screen, self.color, points, thick)
        elif self.orient == -45:
            points = [
                (screen.get_width(), 0 - 30),
                (screen.get_width() + 30, 0),
                (0, screen.get_height() + 30),
                (0 - 30, screen.get_height())
            ]
            pygame.draw.polygon(screen, self.color, points,thick)

    def checkForCollision(self, screen, player):
        for pixel in player.hitPixel:
            if screen.get_at(pixel) == self.color:
                if not player.immune:
                    player.health -=1
                    player.immune = True
                break

