EQUATION_SIZE = 6

# nao pode ter letras ou algo diferente de dígitos e +-*/ - OK
# nao pode ter sinais repetidos (ex. 2++2) - OK
# nao pode começar com * ou / - OK
# nao pode terminar com sinal nenhum - OK
# validar tamanho - OK
# ver se dá 42 - OK
def mathler(guess):
	equation = "39+1+2"

	if (len(guess) != EQUATION_SIZE):
		return (f"Wrong size! Has to be {EQUATION_SIZE} long.")
	elif (IsAValidCharacter (guess) == False):
		return ("Not a Valid Character")
	elif (isSignalConsistent(guess) == False):
		return("Signal inconsistency")
	elif (eval(guess) != 42):
		return("Your equation does not yield 42!")
	elif (guess == equation):
		return ("You guessed correctly, Mothafocka!!")
	else:
		return(getClue(equation, guess))

def getClue(secret_equation, guess):
	clue = ""
	i = 0
	# loop externo, no string de chute
	for i in range(EQUATION_SIZE):
		j = 0
		if guess[i] == secret_equation[i]:
			clue += "C"
		elif guess[i] != secret_equation[i]:
			# loop interno, no string secret_equation
			for j in range(EQUATION_SIZE):
				if secret_equation[j] == guess[i]:
					clue += "T"
					break
				if j + 1 == EQUATION_SIZE:
					clue += "X"
	return clue

def IsAValidCharacter(guess):

	for element in guess:
		if (isNumber(element) == False and isSignal(element) == False):
			return False
	return True

def isNumber(element):
	valid_characters = "1234567890"

	for x in valid_characters:
		if (element == x):
			return True
	return False

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
