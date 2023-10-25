import pygame as pg
from random import  choice

pg.init()

class App:
    def __init__(self):
        self.sc = pg.display.set_mode((800, 500))
        pg.display.set_caption("Генератор фраз преподавателей ВШЭ")
        pg.display.set_icon(pg.image.load("ico.jpg").convert_alpha())
        self.clock = pg.time.Clock()
        self.generator = RandomPhrase()
        self.generator.load()
        self.current_phrase = ("", "")
        self.button = Button((250, 350, 300, 100), (48,227,202), "Сгенерировать фразу", 23, (64,81,78), self.new_phrase)
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
    def run(self):
        while 1:
            self.check_events()
            self.sc.fill((228,249,245))
            self.button.update()
            self.draw()
            pg.display.flip()
            self.clock.tick(60)
    def new_phrase(self):
        self.current_phrase = self.generator.get()

    def draw(self):
        text = pg.font.SysFont("arial", 20, italic=True).render("\"" + self.current_phrase[1] + "\"", 1, (64,81,78))
        x, y = text.get_size()
        self.sc.blit(text, (400 - x//2, 200 - y//2),)
        self.sc.blit(pg.font.SysFont("arial", 16, bold=True).render(self.current_phrase[0], 1, (64,81,78)), (350 + x//2, 220))

class RandomPhrase:
    def __init__(self):
        self.phrases = {}
        self.authors = []
    def load(self):
        with open("phrases.txt", "r", encoding='utf-8') as f:
            for t in f.read().split("\n"):
                if t == "0":
                    break
                if ":" in t:
                    self.authors.append(t[:-1])
                    self.phrases[self.authors[-1]] = []
                else:
                    self.phrases[self.authors[-1]].append(t)
    def get(self):
        author = choice(self.authors)
        return (author, choice(self.phrases[author]))

class Button:
    def __init__(self, coord, color, text, text_size, text_color, funct):
        self.sc = pg.display.get_surface()
        self.coord = coord
        self.color = color
        self.funct = funct
        rended_text = pg.font.SysFont("arial", text_size).render(text, 1, text_color)
        x, y = rended_text.get_size()
        self.image = pg.Surface(coord[2:])
        self.image.fill(color)
        self.image.blit(rended_text, ((coord[2] - x)//2, (coord[3] - y)//2))
        self.activ = True
        self.onButton = False
    def update(self):
        self.sc.blit(self.image, (self.coord[0], self.coord[1]))
        if self.activ:
            x, y = pg.mouse.get_pos()
            if self.coord[0] < x < self.coord[0] + self.coord[2] and self.coord[1] < y < self.coord[1] + self.coord[3]:
                if pg.mouse.get_pressed(3)[0]:
                    self.onButton = True
                else:
                    if self.onButton:
                        self.funct()
                        self.onButton = False

if "__main__" == name:
    app = App()
    app.run()
