import unittest
from src.mathler import *

class test_mathler_isSign(unittest.TestCase):
		
	def	test_isSign_input_empty_returns_false(self):
		input = None
		expected_response = False

		response = isSign(input)
		self.assertEqual(response, expected_response)
		
	def	test_isSign_input_empty_returns_false(self):
		input = ""
		expected_response = False

		response = isSign(input)
		self.assertEqual(response, expected_response)
		
	def	test_isSign_times_returns_true(self):
		input =  "*"
		expected_response = True

		response = isSign(input)
		self.assertEqual(response, expected_response)
		
	def	test_isSign_division_and_number_returns_false(self):
		input =  "/0"
		expected_response = False

		response = isSign(input)
		self.assertEqual(response, expected_response)
		
	def	test_isSign__number_and_division_returns_false(self):
		input =  "0/"
		expected_response = False

		response = isSign(input)
		self.assertEqual(response, expected_response)

	def	test_isSign_single_division_returns_true(self):
		input = "/"
		expected_response = True

		response = isSign(input)
		self.assertEqual(response, expected_response)

	def	test_isSign_string_returns_false(self):
		input = "Hello!"
		expected_response = False
		
		response = isSign(input)
		self.assertEqual(response, expected_response)

	def	test_isSign_single_char_returns_false(self):
		input = "a"
		expected_response = False
		
		response = isSign(input)
		self.assertEqual(response, expected_response)

	def	test_isSign_number_returns_false(self):
		input = "1"
		expected_response = False
		
		response = isSign(input)
		self.assertEqual(response, expected_response)

class test_mathler_isNumber(unittest.TestCase):
	
	def	test_isNumber_input_none_returns_false(self):
		input = None
		expected_response = False
		
		response = isNumber(input)
		self.assertEqual(response, expected_response)
	
	def	test_isNumber_input_empty_returns_false(self):
		input = ""
		expected_response = False
		
		response = isNumber(input)
		self.assertEqual(response, expected_response)

	def	test_isNumber_number_1_returns_true(self):
		input = "1"
		expected_response = True
		
		response = isNumber(input)
		self.assertEqual(response, expected_response)

	def	test_isNumber_number_9_returns_true(self):
		input = "9"
		expected_response = True
		
		response = isNumber(input)
		self.assertEqual(response, expected_response)

	def	test_isNumber_char_a_returns_false(self):
		input = "a"
		expected_response = False
		
		response = isNumber(input)
		self.assertEqual(response, expected_response)

	def	test_isNumber_sign_times_returns_false(self):
		input = "*"
		expected_response = False
		
		response = isNumber(input)
		self.assertEqual(response, expected_response)
	
	def	test_isNumber_sign_minus_returns_false(self):
		input = "-"
		expected_response = False
		
		response = isNumber(input)
		self.assertEqual(response, expected_response)

	def test_isNumber_string_returns_false(self):
		input = "2ef2e*0"
		expected_response = False
		
		response = isNumber(input)
		self.assertEqual(response, expected_response)

class test_mathler_IsAValidCharacter(unittest.TestCase):
	
	def test_isAValidCharacter_input_none_returns_false(self):
		input = None
		expected_response = False
		
		response = IsAValidCharacter(input)
		self.assertEqual(response, expected_response)
	
	def test_isAValidCharacter_input_empty_returns_false(self):
		input = ""
		expected_response = False
		
		response = IsAValidCharacter(input)
		self.assertEqual(response, expected_response)
	
	def test_isAValidCharacter_valid_equation_returns_true(self):
		input = "31+1+2"
		expected_response = True
		
		response = IsAValidCharacter(input)
		self.assertEqual(response, expected_response)

	def test_isAValidCharacter_char_and_number_equation_returns_false(self):
		input = "31+a+2"
		expected_response = False
		
		response = IsAValidCharacter(input)
		self.assertEqual(response, expected_response)

	def test_isAValidCharacter_start_letter_numbers_equation_returns_false(self):
		input = "R+1242"
		expected_response = False
		
		response = IsAValidCharacter(input)
		self.assertEqual(response, expected_response)
		
	def test_isAValidCharacter_no_sign_returns_true(self):
		input = "542679"
		expected_response = True
		
		response = IsAValidCharacter(input)
		self.assertEqual(response, expected_response)
		
	def test_isAValidCharacter_only_signs_returns_true(self):
		input = "+-/**-"
		expected_response = True
		
		response = IsAValidCharacter(input)
		self.assertEqual(response, expected_response)


class test_mathler_isSignConsistent(unittest.TestCase):
	
	def test_isSignConsistent_input_none_returns_false(self):
		input = None
		expected_response = False
		
		response = isSignConsistent(input)
		self.assertEqual(response, expected_response)
	
	def test_isSignConsistent_input_empty_returns_false(self):
		input = ""
		expected_response = False
		
		response = isSignConsistent(input)
		self.assertEqual(response, expected_response)
	
	def test_isSignConsistent_only_signals_returns_false(self):
		input = "+-/**-"
		expected_response = False
		
		response = isSignConsistent(input)
		self.assertEqual(response, expected_response)

	def test_isSignConsistent_two_consecutive_signs_returns_false(self):
		input = "40++2"
		expected_response = False
		
		response = isSignConsistent(input)
		self.assertEqual(response, expected_response)
		
	def test_isSignConsistent_initial_times_sign_returns_false(self):
		input = "*40++2"
		expected_response = False
		
		response = isSignConsistent(input)
		self.assertEqual(response, expected_response)
	
	def test_isSignConsistent_initial_plus_sign_returns_true(self):
		input = "+40+12"
		expected_response = True
		
		response = isSignConsistent(input)
		self.assertEqual(response, expected_response)	

	def test_isSignConsistent_initial_minus_sign_returns_true(self):
		input = "-40+11"
		expected_response = True
		
		response = isSignConsistent(input)
		self.assertEqual(response, expected_response)
		
	def test_isSignConsistent_initial_minus_sign_returns_true(self):
		input = "-40+11"
		expected_response = True
		
		response = isSignConsistent(input)
		self.assertEqual(response, expected_response)
		
	def test_isSignConsistent_with_minus_sign_at_end_returns_false(self):
		input = "40+11-"
		expected_response = False
		
		response = isSignConsistent(input)
		self.assertEqual(response, expected_response)		

	def test_isSignConsistent_with_divide_sign_at_end_returns_false(self):
		input = "40+11/"
		expected_response = False
		
		response = isSignConsistent(input)
		self.assertEqual(response, expected_response)

class test_mathler_isValidToEval(unittest.TestCase):
	
	def test_isValidToEval_input_none_returns_false(self):
		input = None
		expected_response = False
		
		response = isValidToEval(input)
		self.assertEqual(response, expected_response)
		
	def test_isValidToEval_input_empty_returns_false(self):
		input = ""
		expected_response = False
		
		response = isValidToEval(input)
		self.assertEqual(response, expected_response)
		
	def test_isValidToEval_allZero_returns_false(self):
		input = "000000"
		expected_response = False
		
		response = isValidToEval(input)
		self.assertEqual(response, expected_response)
		
	def test_isValidToEval_divided_by_Zero_returns_false(self):
		input = "42/0-1"
		expected_response = False
		
		response = isValidToEval(input)
		self.assertEqual(response, expected_response)
		
	def test_isValidToEval_number_after_zero_returns_false(self):
		input = "042-32"
		expected_response = False
		
		response = isValidToEval(input)
		self.assertEqual(response, expected_response)
		
	def test_isValidToEval_zeroPlus_returns_true(self):
		input = "0+42-1"
		expected_response = True
		
		response = isValidToEval(input)
		self.assertEqual(response, expected_response)

	def test_isValidToEval_zero_divided_by_number_returns_true(self):
		input = "0/43-1"
		expected_response = True
		
		response = isValidToEval(input)
		self.assertEqual(response, expected_response)

	def test_isValidToEval_one_hundred_Division_returns_True(self):
		input = "100/20"
		expected_response = True
		
		response = isValidToEval(input)
		self.assertEqual(response, expected_response)

	def test_isValidToEval_one_thousand_Division_returns_True(self):
		input = "1000/2"
		expected_response = True
		
		response = isValidToEval(input)
		self.assertEqual(response, expected_response)

	def test_isValidToEval_number_4_after_zero_returns_false(self):
		input = "12+040"
		expected_response = False
		
		response = isValidToEval(input)
		self.assertEqual(response, expected_response)

class test_mathler_getClue(unittest.TestCase):
	
	def test_getClue_input_empty_equation_123_plus_45_returns_XXXXXX(self):
		input = ""
		equation = "123+45"
		expected_response = "XXXXXX"
		
		response = getClue(equation, input)
		self.assertEqual(response, expected_response)
	
	def test_getClue_input_123_plus_45_equation_45_minus_123_returns_TTTXTT(self):
		input = "123+45"
		equation = "45-123"
		expected_response = "TTTXTT"
		
		response = getClue(equation, input)
		self.assertEqual(response, expected_response)
	
	def test_getClue_input_123_plus_45_equation_123_plus_45_returns_CCCCCC(self):
		input = "123+45"
		equation = "123+45"
		expected_response = "CCCCCC"
		
		response = getClue(equation, input)
		self.assertEqual(response, expected_response)
	
	def test_getClue_input_67_minus_9_times_8_equation_123_plus_45_returns_XXXXXX(self):
		input = "67-9*8"
		equation = "123+45"
		expected_response = "XXXXXX"
		
		response = getClue(equation, input)
		self.assertEqual(response, expected_response)
	
	def test_getClue_input_none_returns_XXXXXX(self):
		input = None
		equation = "123+45"
		expected_response = "XXXXXX"
		
		response = getClue(equation, input)
		self.assertEqual(response, expected_response)