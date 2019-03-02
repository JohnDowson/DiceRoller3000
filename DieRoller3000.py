import random
class Die:
	def __init__(self, sides):
		self.sides = sides
	
	def roll(self):
		return random.randrange(1, self.sides)

def makeDie(dice, sides):
	return [Die(sides) for x in range(dice)]

def main():
	print("Welcome to DieRoller3000")
	result = 0
	dice = int(input("Enter number of dice: "))
	sides = int(input("Enter number of sides: "))
	dice = makeDie(dice, sides)
	for die in dice:
		result += die.roll()
	print(result)

if __name__ == "__main__":
    main()