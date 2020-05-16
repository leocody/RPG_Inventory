import pyxel
import constant as C

class App:
    def __init__(self):
        pyxel.init(C.SCREEN_WIDTH, C.SCREEN_HEIGHT, caption="Leo's Inventory", quit_key=True)
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
        self.selectable_items = [C.KIND_YAKUSOU, C.KIND_TOKUYAKUSOU, C.KIND_PET, C.KIND_MONEY, C.KIND_CLAW]

    def select(self, item_number):
        pass
    def draw(self):
        pass

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

