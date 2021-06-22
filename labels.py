from pygame import font

class Label:
    '''Create label per button.'''
    def __init__(self, font, sym, pos, color):
        self.txt = font.render(sym, 1, color)
        self.pos = pos