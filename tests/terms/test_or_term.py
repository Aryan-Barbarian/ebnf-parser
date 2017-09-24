import unittest
from ebnf_parser import *

class TestOrTerm(unittest.TestCase):

    def test_one_option(self):
        text = "123abc123abcabc"
        curr_string = "\"abc\" | "
        option1 = TextTerm("123", "\"123\"")
        option2 = TextTerm("abc", "\"abc\"")
        raise NotImplementedError("Test not implemented")

    def test_many_options(self):
        raise NotImplementedError("Test not implemented")

    def test_matched_option_is_none(self):
        raise NotImplementedError("Test not implemented")

    def test_matched_option_is_one(self):
        raise NotImplementedError("Test not implemented")

    def test_matched_option_is_many(self):
        raise NotImplementedError("Test not implemented")

    def test_matched_option_is_all(self):
        raise NotImplementedError("Test not implemented")

    def test_matched_option_is_first(self):
        raise NotImplementedError("Test not implemented")

    def test_matched_option_is_in_middle(self):
        raise NotImplementedError("Test not implemented")

    def test_matched_option_is_last(self):
        raise NotImplementedError("Test not implemented")



if __name__ == '__main__':
    unittest.main()