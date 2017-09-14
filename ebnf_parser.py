class Parser(object):
	"""docstring for Parser"""
	def __init__(self):
		pass;

	def read_rules(rule_string=None, inputfilepath=None):
		if inputfilepath:
			with open(inputfilepath) as fp:
				rule_string = fp.read()
		if rule_string is None:
			print("no rules string or filepath passed in!")
		print(rule_string)
	
	def match(self, text):
		print("Matching text")
		print(text)

class BaseTerm(object):
	def __init__(self, rule_string):
		self.rule_string = rule_string

	def match(self, text):
		return None, 0;

class TextTerm(BaseTerm):
	def __init__(self, rule_string):
		super(TextTerm, self).__init__(rule_string)
		self.possibles = possibles
	
class FullTerm(BaseTerm):
	def __init__(self, rule_string, possibles):
		super(FullTerm, self).__init__(rule_string)
		self.possibles = possibles

class RepeatTerm(BaseTerm):
	def __init__(self, rule_string, possibles):
		super(RepeatTerm, self).__init__(rule_string, possibles)
		
