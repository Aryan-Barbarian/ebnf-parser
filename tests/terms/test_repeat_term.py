import unittest
from parsing.ebnf_parser import *

class TestRepeatTerm(unittest.TestCase):

    def test_inner_term_text(self):
        raise NotImplementedError("Test not implemented");

    def test_inner_term_repeat(self):
        raise NotImplementedError("Test not implemented");

    def test_inner_term_or(self):
        # TODO: should be multiple tests with different patterns of matching
        raise NotImplementedError("Test not implemented");

    def test_inner_term_and(self):
        raise NotImplementedError("Test not implemented");

    def test_inner_term_variable(self):
        raise NotImplementedError("Test not implemented");

    def test_length_match_equal_to_text_single(self):
        raise NotImplementedError("Test not implemented")

    def test_length_match_equal_to_text_with_repeats(self):
        raise NotImplementedError("Test not implemented")

    def test_length_match_greater_than_text(self):
        raise NotImplementedError("Test not implemented")

    def test_matches_zero_times(self):
        raise NotImplementedError("Test not implemented")
        
    def test_matches_one_time(self):
        raise NotImplementedError("Test not implemented")
        
    def test_matches_many_times(self):
        raise NotImplementedError("Test not implemented")
        




if __name__ == '__main__':
    unittest.main()