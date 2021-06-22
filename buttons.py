from os.path import isfile, join
from os import listdir
from constants import barrier, S
import pygame

class Button(pygame.sprite.Sprite):
    '''Create buttons.'''
    def __init__(self, pos_x, pos_y, path):
        '''Load sprites and create one rect per image.'''
        super().__init__()
        self.sprites = []
        self.is_animating = False
        images = [f for f in listdir(path) if isfile(join(path, f))]
        for img in images:
            self.sprites.append(pygame.image.load("imgs/sprites_button/"+img))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animate(self):
        '''toggle animation'''
        self.is_animating = True

    def update(self):
        '''one loop of animations'''
        if self.is_animating == True:
            self.current_sprite += 0.3

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]

    def check_click(self, mouse, user_text, control):
        '''check what button was pressed and print in the screen it's function'''
        if self.rect.collidepoint(mouse):
            if self.rect.topleft == (10, 250) and barrier.x < 365:
                self.animate()
                barrier.x += 4*S
                return "log("
            elif self.rect.topleft == (67, 250) and barrier.x < 365:
                self.animate()
                barrier.x += S
                return "√"
            elif self.rect.topleft == (124, 250) and barrier.x < 365:
                self.animate()
                barrier.x += 4*S
                return "pow("
            elif self.rect.topleft == (181, 250) and barrier.x < 365:
                self.animate()
                barrier.x += 5*S
                return "comb("
            elif self.rect.topleft == (238, 250) and barrier.x < 365:
                self.animate()
                barrier.x += 5*S
                return "perm("
            elif self.rect.topleft == (295, 250) and barrier.x < 365:
                self.animate()
                barrier.x += S
                return "!"
            elif self.rect.topleft == (352, 250):
                self.animate()
                barrier.x -= 5000
                return ""
            elif self.rect.topleft == (10, 300) and barrier.x < 365:
                self.animate()
                barrier.x += 4*S
                return "sin("
            elif self.rect.topleft == (67, 300) and barrier.x < 365:
                self.animate()
                barrier.x += 4*S
                return "cos("
            elif self.rect.topleft == (124, 300) and barrier.x < 365:
                self.animate()
                barrier.x += 4*S
                return "tan("
            elif self.rect.topleft == (181, 300) and barrier.x < 365:
                self.animate()
                barrier.x += 4*S
                return "gcd("
            elif self.rect.topleft == (238, 300) and barrier.x < 365:
                self.animate()
                barrier.x += 4*S
                return "lcm("
            elif self.rect.topleft == (295, 300) and barrier.x < 365:
                self.animate()
                barrier.x += S
                return "%"
            elif self.rect.topleft == (352, 300) and barrier.x < 365:
                self.animate()
                barrier.x += len(control)*S
                return control
            elif self.rect.topleft == (10, 350) and barrier.x < 365:
                self.animate()
                barrier.x += S
                return "π"
            elif self.rect.topleft == (67, 350) and barrier.x < 365:
                self.animate()
                barrier.x += S
                return "e"
            elif self.rect.topleft == (124, 350) and barrier.x < 365:
                self.animate()
                barrier.x += S
                return "τ"
            elif self.rect.topleft == (181, 350) and barrier.x < 365:
                self.animate()
                return "Σ(" 
            elif self.rect.topleft == (238, 350) and barrier.x < 365:
                self.animate()
                return "prod("
            elif self.rect.topleft == (295, 350) and barrier.x < 365:
                self.animate()
                print(self.rect)
                return "log10("
            elif self.rect.topleft == (352, 350) and barrier.x < 365:
                self.animate()
                return ""
            else:
                return ""
        else:
            return ""