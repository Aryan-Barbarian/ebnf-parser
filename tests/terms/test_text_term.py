import unittest
import ebnf_parser

class TestTextTerm(unittest.TestCase):


    def test_match_starts_at_start_of_text(self):
        text = "howdy123"
        match_string = "howdy"
        expected_match = ebnf_parser.TextMatch(0, 5)
        self.run_match_test(text, match_string, 0, expected_match)

    def test_match_starts_at_middle_of_text(self):
        text = "ahowdy123"
        match_string = "howdy"
        start_index = 1
        expected_match = ebnf_parser.TextMatch(1, 6)
        self.run_match_test(text, match_string, start_index, expected_match)

    def test_match_starts_at_middle_of_fails(self):
        text = "ahowdy123"
        match_string = "howdy"
        start_index = 0
        expected_match = None
        self.run_match_test(text, match_string, start_index, expected_match)

    def test_match_starts_at_end_of_text(self): 
        text = "aahowdy"
        match_string = "howdy"
        start_index = 2
        expected_match = ebnf_parser.TextMatch(2, 7)
        self.run_match_test(text, match_string, start_index, expected_match)

    def test_length_match_string_less_than_text(self):
        text = "howdy123"
        match_string = "howdy"
        expected_match = ebnf_parser.TextMatch(0, 5)
        self.run_match_test(text, match_string, 0, expected_match)

    def test_length_match_string_equal_text(self):
        text = "howdy"
        match_string = "howdy"
        expected_match = ebnf_parser.TextMatch(0, 5)
        self.run_match_test(text, match_string, 0, expected_match)

    def test_length_match_string_greater_than_text(self):
        text = "howdy"
        match_string = "howdyyy"
        self.run_match_test(text, match_string, 0, None) # TODO: expect error?

    def test_length_match_string_zero(self):
        text = "howdy"
        match_string = ""
        fn = lambda : self.run_match_test(text, match_string, 0, None)
        self.assertRaises(ValueError, fn)

    def test_num_differences_zero(self):
        self.test_length_match_string_equal_text()

    def test_num_differences_one(self):
        self.test_difference_at_beginning()

    def test_num_differences_all(self):
        text = "1234567890"
        match_string = "howdy"
        self.run_match_test(text, match_string, 0, None)

    def test_difference_at_beginning(self):
        text = "gowdy"
        match_string = "howdy"
        self.run_match_test(text, match_string, 0, None)

    def test_difference_in_middle(self):
        text = "hobdy"
        match_string = "howdy"
        self.run_match_test(text, match_string, 0, None)

    def test_difference_at_end(self):
        text = "howdu"
        match_string = "howdy"
        self.run_match_test(text, match_string, 0, None)

    def run_match_test(self, text, match_string, start_index, expected_match):
        rule_string = "\"{}\"".format(match_string)
        text_term = ebnf_parser.TextTerm(rule_string, match_string)
        actual_match = text_term.match_first(text, start_index)
        self.assertEqual(actual_match, expected_match)


if __name__ == '__main__':
    unittest.main()