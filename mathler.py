EQUATION_SIZE = 6

# nao pode começar com * ou / - OK
# nao pode terminar com sinal nenhum - OK
# validar tamanho - OK
# ver se dá 42 - OK
def mathler():
	equation = "39+1+2"

	guess = input("Type your guess: ")
	if (len(guess) != EQUATION_SIZE):
		print (f"Wrong size! Has to be {EQUATION_SIZE} long.")
	if (IsAValidCharacter (guess) == 0):
		print ("Not a Valid Character")
	if (isSignalConsistent(guess) == False):
		print("Signal inconsistency")
	if (eval(guess) != 42):
		print("Your equation does not yield 42!")
	elif (guess == equation):
		print ("You guessed correctly, Mothafocka!!")
	else:
		print("Not the correct equation ): try again!")

def IsAValidCharacter(guess):

	for element in guess:
		if (CheckChar (element) == 0):
			return (0)
	return (1)

def CheckChar(element):
	valid_characters = "1234567890+-*/"

	for x in valid_characters:
		if (element == x):
			return (1)
	return (0)

def isSignal(character):
	list_of_signal = "-+/*"

	for i in list_of_signal:
		if character == i:
			return True
	return False

def isSignalConsistent(guess):

	prev = 0

	if (guess[0] == "/" or guess[0] == "*"):
		return False
	if isSignal(guess[len(guess) - 1]):
		return False
	for element in guess:
		if isSignal(element) == True and prev == 1:
			return False
		if prev == 1 and isSignal(element) == False:
			prev = 0
		if isSignal(element) == True:
			prev = 1
	return True


if __name__ == "__main__":
	mathler()
