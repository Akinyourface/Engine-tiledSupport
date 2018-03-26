from Globals import *


class GameStateManager:
    def __init__(self):
        self.states = []
        self.currentState = ""
        self.changeState = False
    def return_states(self):
        print(self.states)
    def add_state(self, name):
        self.states.append(name)
        print("Added the state" + str(name))
    def set_state(self, name):
        self.currentState = name
        if self.currentState in self.states:
            print("Found state for" + str(self.currentState))
            
        else:
            print("ERROR! The state" + str(self.currentState) + " could not be found!")
                  
    def def_states(self):
        self.add_state("MainMenu")
        self.add_state("MainGame")
