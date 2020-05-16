import pyxel
import constant as C

class App:
    def __init__(self):
        pyxel.init(C.SCREEN_WIDTH, C.SCREEN_HEIGHT, caption="Leo's Inventory", quit_key=True)
        pyxel.run(self.update, self.draw)

    def draw(self):
        pass

    def update(self):
        pass

App()