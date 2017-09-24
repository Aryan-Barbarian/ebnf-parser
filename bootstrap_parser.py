from ebnf_parser import *

# Utils
def text_term(letter):
	rule_string = "\"{}\"".format(letter)
	return TextTerm(rule_string, letter)

def make_text_terms(*letters):
	return map(text_term, letters)

def make_or_term(*possibles):
	rule_string = "<OR_TERM>"
	return OrTerm(rule_string, possibles)

def make_and_term(*terms):
	rule_string = "<AND_TERM>"
	return AndTerm(rule_string, terms)

def generate_letter():
	lowercase = [
		"a", "b", "c", "d", "e", "f", "g", "h", "i", 
		"j", "k", "l", "m", "n", "o", "p", "q", "r", 
		"s", "t", "u", "v", "w", "x", "y", "z"
		]
	uppercase = [letter.upper() for letter in lowercase]
	all_letters = lowercase + uppercase
	return make_text_terms(*all_letters)

def generate_bounded_term(open_char, close_char):
	ans = \
		make_and_term(
			make_text_term(open_char)
			make_zero_or_more_term( anything )
			make_text_term(close_char)
		)

letter = generate_letter()


digit = \
	make_or_term(
		make_text_terms("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"))

escape_char = \
	make_or_term(
		make_text_terms("\\", "\n", "\t", "\r", "\""))

wspace = \
	make_or_term(
		make_text_terms(" ", "\n", "\t"))

terminal = make_text_term(";")

anything = \
	make_or_term(
		letter, digit, escape_char, wspace
	)


variable_name = \
	make_and_term(
		letter,
		make_zero_or_more_term(
			make_or_term(
				letter,
				digit,
				make_text_term("_"))
		)
	)


variable_term = variable_name # TODO: Rename??

text_term = generate_bounded_term("\"", "\"")
zero_or_more_term = generate_bounded_term("{", "}")
zero_or_one_term = generate_bounded_term("[", "]")
