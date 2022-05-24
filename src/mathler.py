EQUATION_SIZE = 6

# nao pode ter letras ou algo diferente de dígitos e +-*/ - OK
# nao pode ter sinais repetidos (ex. 2++2) - OK
# nao pode começar com * ou / - OK
# nao pode terminar com sinal nenhum - OK
# validar tamanho - OK
# ver se dá 42 - OK
def mathler(guess):
	equation = "39+1+2"

	if (guess == None or guess == ""):
		return ("Empty input!")
	if (len(guess) != EQUATION_SIZE):
		return (f"Wrong size! Has to be {EQUATION_SIZE} long.")
	elif (IsAValidCharacter (guess) == False):
		return ("Not a Valid Character")
	elif (isSignConsistent(guess) == False):
		return("Sign inconsistency")
	elif (isValidToEval (guess) == False):
		return ("The current equation it's not eligible to Eval function!")
	elif (eval(guess) != 42):
		return("Your equation does not yield 42!")
	else:
		return(getClue(equation, guess))

def isValidToEval (guess):
	trigger = False

	if (guess == "" or guess == None):
		return False
	for i in range (len(guess)):
		if (i < 5 and guess[i] == "0" and isNumber (guess[i + 1]) == True and trigger == False):
			return (False)
		elif (i < 5 and guess[i] == "/" and guess[i + 1] == "0"):
			return (False)
		elif (isNumber (guess[i]) == True):
			trigger = True
		elif (isNumber (guess[i]) == False):
			trigger = False
	return (True)

def getClue(secret_equation, guess):
	clue = ""
	i = 0

	if (secret_equation == None or guess == None or guess == "" or secret_equation == ""):
		return ("XXXXXX")
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
	if (guess == None or guess == ""):
		return False
	for element in guess:
		if (isNumber(element) == False and isSign(element) == False):
			return False
	return True

def isNumber(element):
	valid_characters = "1234567890"

	if (element == None or element == ""):
		return False
	for x in valid_characters:
		if (element == x):
			return True
	return False

def isSign(character):
	list_of_Sign = "-+/*"

	if (character == None or character == ""):
		return False
	for i in list_of_Sign:
		if character == i:
			return True
	return False

def isSignConsistent(guess):
	prev = 0

	if (guess == None or guess == ""):
		return False
	if (guess[0] == "/" or guess[0] == "*"):
		return False
	if isSign(guess[len(guess) - 1]):
		return False
	for element in guess:
		if isSign(element) == True and prev == 1:
			return False
		if prev == 1 and isSign(element) == False:
			prev = 0
		if isSign(element) == True:
			prev = 1
	return True
