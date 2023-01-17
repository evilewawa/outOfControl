import pygame


class player(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.dimensions = [100, 100]
        self.rect = (self.x, self.y, self.dimensions[0], self.dimensions[1])
        self.movePixels = 5
        self.controls = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
        self.hitPixel = [
            (self.x, self.y),
            (self.x + self.dimensions[0], self.y),
            (self.x + self.dimensions[0], self.y + self.dimensions[1]),
            (self.x, self.y + self.dimensions[1])
        ]
        self.health = 3
        self.immune = False
        self.gotHit = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self,screen):
        keys = pygame.key.get_pressed()
        if keys[self.controls[0]]:  # would be left normally etc.
            if self.x > 0 + 5:
                self.x -= self.movePixels
        if keys[self.controls[1]]:
            if self.x < screen.get_width()-self.dimensions[1]-5:
                self.x += self.movePixels
        if keys[self.controls[2]]:
            if self.y > 0+5:
                self.y -= self.movePixels
        if keys[self.controls[3]]:
            if self.y < screen.get_height() - self.dimensions[1] -5:
                self.y += self.movePixels
        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.dimensions[0], self.dimensions[1])
        self.hitPixel = [
            (self.x, self.y),
            (self.x + self.dimensions[0], self.y),
            (self.x + self.dimensions[0], self.y + self.dimensions[1]),
            (self.x, self.y + self.dimensions[1])
        ]
    def get_controls(self):
        strControls = []

        for key in self.controls:
            if key == pygame.K_LEFT:
                strControls.append("left")
            elif key == pygame.K_RIGHT:
                strControls.append("right")
            elif key == pygame.K_UP:
                strControls.append("up")
            elif key == pygame.K_DOWN:
                strControls.append("down")
        return strControls

#
