import pyxel
import constant as C

class App:
    def __init__(self):
        pyxel.init(C.SCREEN_WIDTH, C.SCREEN_HEIGHT, caption="Leo's Inventory", quit_key=True)
        pyxel.load("assets/Leo_Inventory.pyxres")
        self.mainscreen = Mainscreen()
        pyxel.run(self.update, self.draw)

    def draw(self):
        self.mainscreen.draw()

    def update(self):
        pass

class Mainscreen:
    def __init__(self):
        self.inventory = Inventory()
        self.item_selection = Item_Selection()

    def draw(self):
        self.inventory.draw()
        self.item_selection.draw()

class Item_Selection:
    def __init__(self):
        self.selectable_items_kinds = [
            C.KIND_POSTION, 
            C.KIND_KEY, 
            C.KIND_BOW, 
            C.KIND_SHIELD, 
            C.KIND_SWORD
        ]

    def select(self, item_number):
        pass

    def draw(self):
        y_counter = 0
        for item_kind in self.selectable_items_kinds:
            pyxel.blt(0, y_counter, 0, item_kind[0], item_kind[1], 16, 16)
            y_counter += 30

class Inventory:
    def __init__(self):
        self.items = []
        self.selected_item_index = 0

    def add(self, item):
        pass

    def select_down(self):
        pass

    def select_up(self):
        pass

    def use_selected_item(self):
        pass

    def draw(self):
        pass

class Item:
    def  __init__(self, kind):
        self.kind = kind
        self.amount = 1

    def draw(self, x, y):
        pass
    def increment(self):
        if self.amount >= C.MAX_AMOUNT:
            raise CanNotIncrement()
        self.amount += 1
    def decrement(self):
        if self.amount <= C.MIN_AMOUNT:
            raise CanNotDecrement()
        self.amount -= 1

class CanNotIncrement(Exception):
    pass

class CanNotDecrement(Exception):
    pass

App()

