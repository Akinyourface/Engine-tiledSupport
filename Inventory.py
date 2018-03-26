from Globals import *
from InventorySlot import *
class Inventory:
    def __init__(self):
        self.inventorySize = 5
        #print(self.items)
        #for x in range(self.inventorySizeX):
        #    for y in range(self.inventorySizeY):
        #        slot = InventorySlot(x, y, self.items[y][x])
        #        self.items.append(slot)
        self.items = [InventorySlot() for x in range(self.inventorySize)]
        self.str_items = ["null" for x in range(self.inventorySize)]
        self.currentItem = self.items[0].containedItem
        #self.items[0] = "default_sword"
    def add_closest_item(self, name):
        #for x in range(self.inventorySizeX):
            #for y in range(self.inventorySizeY):
                #if(self.items[y][x].containedItem == "null"):
                #    self.items[y][x].containedItem = name
                #    break
                #else:
                #    print("it didnt work")
                #    break
                #print(self.items[y][x].containedItem)
        #self.items[0][0].containedItem = "item_wood"
        for item in range(self.inventorySize):
            if self.items[item].containedItem == "null":
                self.items[item].containedItem = name
    def does_have_item(self, name):
        for item in range(self.inventorySize):
            if self.items[item].containedItem == name:
                return True
            else:
                return False
    def change_current_item(self, name):
        self.currentItem = name
            
        
            
