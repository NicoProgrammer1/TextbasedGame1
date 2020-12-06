# from Game import Game
from Location import Location
from Person import Person
import time


p = Person()

gameplaying = True 
currentLevel = Location.FILES['house.txt']

lineNumber = 0
choices = list()

# go to line in the current room
def goToLine(ln):
	global lineNumber
	lineNumber = ln - 1

def goTo(locationName):
	global lineNumber
	global currentLevel
	currentLevel = Location.FILES[locationName + '.txt']
	lineNumber = 0

while gameplaying:
	if lineNumber >= len(currentLevel):
		time.sleep(1.5)
		print("THE END")	
		break;

	gameLine = currentLevel[lineNumber]

	# adds one for next loop of gameplaying
	lineNumber += 1

	if gameLine.startswith('~'):
		index = 1
		for choice in choices:
			print(f"{index})  {eval(choice[2:].split('//')[0])}")
			index += 1

		inputIsWrong = True
		y = 0
		while inputIsWrong:
			x = input("Choose ")
			try:
				y = int(x)
			except ValueError:
				print("Please enter a numbered chioce")
				continue
			if y >0 and y <= len(choices):
				inputIsWrong = False
		
		y -= 1
			
		chosenLine = choices[y]
		toExec = chosenLine[2:].split("//")[1]
		time.sleep(1.5)
		exec(toExec[1:])
		choices = list()

	if gameLine.startswith('$'):
		print(eval(gameLine.split('//')[0][1:]))
		s = input("  ")
		string = str(s)
		exec(gameLine.split('//')[1][1:])

	if gameLine.startswith((':')):
		choices.append(gameLine)

	if gameLine.startswith(('!')):
		exec(gameLine[1:])
		continue;
	if gameLine.startswith('f\"'):
		print(eval(gameLine))
		time.sleep(1.5)
		continue;

print("THE END")
