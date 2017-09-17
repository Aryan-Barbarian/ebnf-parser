MAX_REPEATS = 10

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
	def __init__(self, start, end, children=None):
		self.start = start
		self.end = end
		self.len = end - start
		self.children = children if children else []

	def __eq__(self, other):
		if isinstance(other, MatchNode):
			return (self.start == other.start and self.end == other.end)
		return False

class TextMatch(MatchNode):
	def __init__(self, start, end, children=None):
		super(TextMatch, self).__init__(start, end, children)

class RepeatMatch(MatchNode):
	def __init__(self, start, end, num_repeats, children=None):
		super(RepeatMatch, self).__init__(start, end, children)
		self.num_repeats = num_repeats


class BaseTerm(object):
	def __init__(self, rule_string):
		self.rule_string = rule_string

	def match(self, text, start_index):
		return False; # TODO: throw error

	def match_first(self, text, start_index):
		match_gen = self.match(text, start_index)
		for item in match_gen: # returns first
			return item
		return None # should this be explicit like this?

class TextTerm(BaseTerm):
	def __init__(self, rule_string, match_string):
		super(TextTerm, self).__init__(rule_string)
		if len(match_string) == 0:
			raise ValueError("Match string must have non-zero length")
		self.match_string = match_string

	def match_first(self, text, start_index):
		if start_index + len(self.match_string) > len(text):
			return None;
		for i in range(0, len(self.match_string)):
			j = i + start_index # text index
			if text[j] != self.match_string[i]:
				return None
		return TextMatch(start_index,  start_index + len(self.match_string));

	def match(self, text, start_index):
		ans = self.match_first(text, start_index)
		if ans:
			yield ans

class MultiTerm(BaseTerm):
	def __init__(self, rule_string, possibles):
		super(FullTerm, self).__init__(rule_string)
		self.possibles = possibles

	def match(self, text, start_index):
		for possible in self.possibles:
			for match in possible.match(text):
				yield match

class RepeatTerm(BaseTerm):
	def __init__(self, rule_string, inner_term):
		super(RepeatTerm, self).__init__(rule_string, possibles)
		self.inner_term = inner_term

	def match(self, text, start_index):
		curr_start = start_index
		curr_end = None

		for curr_match in self.inner_term.match(text, curr_start):
			curr_end = curr_match.end

	
class VariableTerm(BaseTerm): # TODO: Make sure we keep only one instance per variable
	def __init__(self, rule_string, inner_term):
		super(VariableTerm, self).__init__(rule_string, possibles)
