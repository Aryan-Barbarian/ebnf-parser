import unittest
from ebnf_parser import *

class TestMultiTerm(unittest.TestCase):

    def test_one_option(self):
        text = "123abc123abcabc"
        curr_string = "\"abc\" | "
        option1 = TextTerm("123", "\"123\"")
        option2 = TextTerm("abc", "\"abc\"")

        pass

    def test_many_options(self):
        pass

    def test_matched_option_is_none(self):
        pass

    def test_matched_option_is_one(self):
        pass

    def test_matched_option_is_many(self):
        pass

    def test_matched_option_is_all(self):
        pass

    def test_matched_option_is_first(self):
        pass

    def test_matched_option_is_in_middle(self):
        pass

    def test_matched_option_is_last(self):
        pass



if __name__ == '__main__':
    unittest.main()