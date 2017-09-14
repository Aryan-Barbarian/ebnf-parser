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

class MatchNode(object):
	def __init__(self, start, end, children):
		self.start = start
		self.end = end
		self.children = children

class TextMatch(MatchNode):
	def __init__(self, start, end, children):
		super(TextMatch, self).__init__(start, end, children)

class RepeatMatch(MatchNode):
	def __init__(self, start, end, children, num_repeats):
		super(RepeatMatch, self).__init__(start, end, children)
		self.num_repeats = num_repeats

class RepeatMatch(MatchNode):
	def __init__(self, start, end, children, num_repeats):
		super(RepeatMatch, self).__init__(start, end, children)
		self.num_repeats = num_repeats



class BaseTerm(object):
	def __init__(self, rule_string):
		self.rule_string = rule_string

	def match(self, text):
		return None, 0;

class TextTerm(BaseTerm):
	def __init__(self, rule_string):
		super(TextTerm, self).__init__(rule_string)
	
class FullTerm(BaseTerm):
	def __init__(self, rule_string, possibles):
		super(FullTerm, self).__init__(rule_string)
		self.possibles = possibles

class RepeatTerm(FullTerm):
	def __init__(self, rule_string, possibles):
		super(RepeatTerm, self).__init__(rule_string, possibles)
		
class VariableTerm(FullTerm): # TODO: Make sure we keep only one instance per variable
	def __init__(self, rule_string, possibles):
		super(VariableTerm, self).__init__(rule_string, possibles)
