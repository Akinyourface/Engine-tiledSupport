from Globals import *
class InventorySlot:
    def __init__(self):
        self.containedItem = "null"
        self.numberOfItems = 0
        
        #print("x: " + str(indexX) + " " + "y: " + str(indexY) + " " + str(item))
        
    def put_item(self, name):
        if name == "":
            self.containedItem = name
        else:
            print("You already have an item in this inventory")
