from erk import *
import random

class DiceRoller(Plugin):

    def __init__(self):
        self.name = "Dice Roller"
        self.description = "A dice rolling plugin."
        
        self.author = "Dan Hetrick"
        self.version = "1.0"
        self.website = None
        self.source = None

    def input(self,client,name,text):
        """Executed when the user inputs text.
        
        Arguments:
        self -- The plugin's instance
        client -- The Twisted IRC client object
        name -- The channel/username of the input that triggered the plugin
        text -- The user input
        """
        tokens = text.split()
        if len(tokens)==3:
            if tokens[0].lower()=="/roll":
                number_of_dice = tokens[1]
                try:
                    number_of_dice = int(number_of_dice)
                except:
                    self.print("Usage: /roll NUMBER_OF_DICE NUMBER_OF_SIDES")
                    return True
                number_of_sides = tokens[2]
                try:
                    number_of_sides = int(number_of_sides)
                except:
                    self.print("Usage: /roll NUMBER_OF_DICE NUMBER_OF_SIDES")
                    return True
                
                total = 0
                for n in range(number_of_dice):
                    roll = random.randint(1,number_of_sides)
                    total = total + roll
                    self.print("<b>Roll "+str(n+1)+":</b> "+str(roll))
                self.print("<b>Total:</b> "+str(total))
                return True
            
        if len(tokens)==2:
            if tokens[0].lower()=="/roll":
                number_of_sides = tokens[1]
                try:
                    number_of_sides = int(number_of_sides)
                except:
                    self.print("Usage: /roll NUMBER_OF_SIDES")
                    return True
                    
                roll = random.randint(1,number_of_sides)
                self.print("<b>Roll :</b> "+str(roll))
                return True
        
        if len(tokens)==1:
            if tokens[0].lower()=="/roll":
                self.print("Usage: /roll NUMBER_OF_SIDES <b>or</b> /roll NUM_DICE NUM_SIDES")
                return True
                
