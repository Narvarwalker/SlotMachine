"""
"""
from breezypythongui import EasyFrame
import random
from tkinter.font import Font

class SlotMachine(EasyFrame):
	
	def __init__(self):
		"""Sets up the window and the widgets."""
		EasyFrame.__init__(self, title = "Test Your Luck!", width = 400, height = 300, background = "limegreen", resizable = False)
		
		# Title label
		self.addLabel(text = "Lucky Slots!", row = 0, column = 0, columnspan = 3, background = "limegreen", foreground = "yellow", font = Font(family = "Impact", size = 28), sticky = "NSEW")
		
		# Funds label and field-  ***read only****
		self.addLabel(text = "Available funds:", row = 1, column = 0, background = "limegreen", sticky = "NE")
		self.fundsField = self.addIntegerField(value = 100, row = 1, column = 1, state = "readonly")
		
		# Fields for the random numbers to appear
		self.numField1 = self.addIntegerField(value = 0, row = 2, column = 0, sticky = "NSEW")
		self.numField2 = self.addIntegerField(value = 0, row = 2, column = 1, sticky = "NSEW")
		self.numField3 = self.addIntegerField(value = 0, row = 2, column = 2, sticky = "NSEW")
		
		# Command button
		self.playButton = self.addButton(text = "Spin", row = 3, column = 0, columnspan = 3, command = self.slots)
		# Label for the output message
		self.outputLabel = self.addLabel(text = "", row = 4, column = 0, columnspan = 3, sticky = "NSEW", background = "limegreen", foreground = "white", font = Font(family = "Georgia", size = 18))
	# Evnet Handling method
	def slots(self):
		# Variables and constants
		num1 = random.randint(1, 9)
		num2 = random.randint(1, 9)
		num3 = random.randint(1, 9)
		# Grab the current funds value from the fundsField componet
		fundsLeft = self.fundsField.getNumber()
		# Determine the outcome of the game
		if num1 == num2 == num3:
			result = " JACKPOT!!!!"
			fundsLeft += 30
		elif num1 == num2 or num2 == num3 or num3 == num1:
			result = "Two of a kind!"
			fundsLeft += 20
		else:
			result = "Sorry, you loose..."
			fundsLeft -= 10
		# Determine if there are any funds left	
		if fundsLeft == 0:
			result = "You loose and GAME OVER"
			self.playButton["state"] = "disabled"
		# Output phase
		self.numField1.setNumber(num1)	
		self.numField2.setNumber(num2)
		self.numField3.setNumber(num3)
		self.outputLabel["text"] = result
		# Update the fundsField value before this function is triggered again
		self.fundsField.setNumber(fundsLeft)	
# definition of the main() function for program entry
def main():
	"""Instantiates and pops up the window."""
	SlotMachine().mainloop()
# global call to trigger the main() function
if __name__ == "__main__":
	main()