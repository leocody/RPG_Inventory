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
            pyxel.play(3, C.SE_ERROR)

        except BoundaryAppendError:
            pyxel.play(3, C.SE_ERROR)

        except ItemNotFoundError:
            pyxel.play(3, C.SE_ERROR)


class Mainscreen:
    def __init__(self):
        self.inventory = Inventory()
        self.item_selection = Item_Selection()

    def draw(self):
        pyxel.cls(pyxel.COLOR_LIME)

        self.inventory.draw()
        self.item_selection.draw()
    
    def update(self):

        if pyxel.btnp(pyxel.KEY_1):
            self.inventory.add(Item(C.KIND_POSTION))
            pyxel.playm(0, loop=False)
            

        if pyxel.btnp(pyxel.KEY_2):
            self.inventory.add(Item(C.KIND_BOMB))
            pyxel.playm(0, loop=False)
            

        if pyxel.btnp(pyxel.KEY_3):
            self.inventory.add(Item(C.KIND_SHIELD))
            pyxel.playm(0, loop=False)
           

        if pyxel.btnp(pyxel.KEY_4):
            self.inventory.add(Item(C.KIND_SWORD))
            pyxel.playm(0, loop=False)
            

        if pyxel.btnp(pyxel.KEY_5):
            self.inventory.add(Item(C.KIND_HELMET))
            pyxel.playm(0, loop=False)
            

        if pyxel.btnp(pyxel.KEY_6):
            self.inventory.add(Item(C.KIND_APPLE))
            pyxel.playm(0, loop=False)
            
      
        if pyxel.btnp(pyxel.KEY_7):
            self.inventory.add(Item(C.KIND_BOW))
            pyxel.playm(0, loop=False)
            

        if pyxel.btnp(pyxel.KEY_8):
            self.inventory.add(Item(C.KIND_DIAMOND))
            pyxel.playm(0, loop=False)
            

        if pyxel.btnp(pyxel.KEY_DOWN):
            self.inventory.select_down()
            pyxel.play(3, C.SE_SELECT)
            

        if pyxel.btnp(pyxel.KEY_UP):
            pyxel.play(3, C.SE_SELECT)
            self.inventory.select_up()
        
        if pyxel.btnp(pyxel.KEY_ENTER):
            self.inventory.use_selected_item()
            pyxel.playm(1, loop=False)
            
        

class Item_Selection:
    def __init__(self):
        self.selectable_items_kinds = [
            C.KIND_POSTION, 
            C.KIND_BOMB, 
            C.KIND_SHIELD, 
            C.KIND_SWORD, 
            C.KIND_HELMET,
            C.KIND_APPLE,
            C.KIND_BOW,
            C.KIND_DIAMOND
        ]

    def select(self, item_number):
        pass

    def draw(self):
        y_counter = 0
        for item_kind in self.selectable_items_kinds:
            pyxel.blt(item_kind[3], item_kind[4], 0, item_kind[0], item_kind[1], 16, 16)
            
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
        self.selected_item_index += 1
        self.selected_item_index %= C.MAX_KIND

    def select_up(self):
        self.selected_item_index -= 1
        self.selected_item_index += C.MAX_AMOUNT
        self.selected_item_index %= C.MAX_AMOUNT

    def use_selected_item(self):
        if len(self.items) == self.selected_item_index:
                raise ItemNotFoundError
        using_item = self.items[self.selected_item_index]
        if using_item.amount >= 2:
            using_item.decrement()
        else:
            self.items.pop(self.selected_item_index)


    def draw(self):
        y_counter = 0
        for item in self.items:
            item.draw(140, y_counter)
            y_counter += 20
        for i in range(C.MAX_AMOUNT):
         #Inventory Square
            pyxel.rectb(140, (20 * i) + 10, 16, 16, pyxel.COLOR_BLACK)
        #Highlight
        pyxel.rectb(140, 20 * self.selected_item_index + 10, 16, 16, pyxel.COLOR_PINK)
            
            

class Item:
    def  __init__(self, kind):
        self.kind = kind
        self.amount = 1

    def __repr__(self):
        return "Kind : " + self.kind[2] + " Amount: " + str(self.amount)  

    def draw(self, x, y):
        pyxel.blt(x, y + 10, 0, self.kind[0],  self.kind[1], 16, 16)
        pyxel.text(x + 16, y + 16, str(self.amount), pyxel.COLOR_BLACK)


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

class ItemNotFoundError(Exception):
    pass
App()
