import ebnf_parser as parser

def main() :
	inputfilepath = "./examples/example1.ebnf"
	text = "-123"
	p = parser.Parser()
	p.read_rules(inputfilepath = inputfilepath)
	p.match(text)

if __name__ == "__main__" : 
	main()