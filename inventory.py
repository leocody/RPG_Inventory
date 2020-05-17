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
        try:
            self.mainscreen.update()
        except CanNotIncrement:
            print("CanNotIncrementError: Can't add to 8 items")
            print("leo@Mac-mini Inventory % /Users/leo/.pyenv/versions/3.8.1/bin/python /Users/leo/Documents/Python/Inventory/inventory.py")
        except BoundaryAppendError:
            print("BoundaryAppendError: Can't add to 4 kinds of items")
            print("leo@Mac-mini Inventory % /Users/leo/.pyenv/versions/3.8.1/bin/python /Users/leo/Documents/Python/Inventory/inventory.py")


class Mainscreen:
    def __init__(self):
        self.inventory = Inventory()
        self.item_selection = Item_Selection()

    def draw(self):
        pyxel.cls(0)
        self.inventory.draw()
        self.item_selection.draw()
    
    def update(self):

        if pyxel.btnp(pyxel.KEY_1):
            self.inventory.add(Item(C.KIND_POSTION))

        if pyxel.btnp(pyxel.KEY_2):
            self.inventory.add(Item(C.KIND_KEY))

        if pyxel.btnp(pyxel.KEY_3):
            self.inventory.add(Item(C.KIND_BOW))

        if pyxel.btnp(pyxel.KEY_4):
            self.inventory.add(Item(C.KIND_SHIELD))

        if pyxel.btnp(pyxel.KEY_5):
            self.inventory.add(Item(C.KIND_SWORD))

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

    # if item_list contains choosed_item
    #   then it will incremet amount of item.
    # Otherwise it will append choosed_item to item_list
    def add(self, choosed_item):
        for find_item in self.items:    
            if find_item.kind == choosed_item.kind:
                find_item.increment()
                return
        if not len(self.items) >= C.MAX_KIND:
            self.items.append(choosed_item)
        else:
            raise BoundaryAppendError




    def select_down(self):
        pass

    def select_up(self):
        pass

    def use_selected_item(self):
        pass

    def draw(self):
        y_counter = 0
        for item in self.items:
            item.draw(140, y_counter)
            y_counter += 30
            
            

class Item:
    def  __init__(self, kind):
        self.kind = kind
        self.amount = 1

    def __repr__(self):
        return "Item"

    def draw(self, x, y):
        pyxel.blt(x, y, 0, self.kind[0],  self.kind[1], 16, 16)
        pyxel.text(x + 16, y + 16, str(self.amount), pyxel.COLOR_GREEN)

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

class BoundaryAppendError(Exception):
    pass
App()

