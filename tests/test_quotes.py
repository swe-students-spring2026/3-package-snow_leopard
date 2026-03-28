import pytest 
from pyquotes import quotes

class Tests:
    def test_get_random_quote_invalid_low(self):
       """
       Tests that get random quote raises an exception 
       when num_of_quote is less than 1
       """
       with pytest.raises(ValueError):
            quotes.get_random_quote(0)
    def test_get_random_quote_invalid_high(self):
        """
        Tests that get random quote raises an exception 
        when num_of_quote is larger than the list of quotes
        """
        with pytest.raises(ValueError):
            quotes.get_random_quote(1000)
    def test_get_random_quote_returns_list(self):
        """
        Test that get_random_quote returned a list
        """
        actual = quotes.get_random_quote(3)
        assert isinstance(actual,list), f"Expected get_random_quote to return a list. Instead it returned {actual}"
    def test_get_random_quote_content(self):
        """
        Test that get_random_quote returned quotes that are from QUOTE
        """
        actual = quotes.get_random_quote(1)
        assert actual[0] in [q["text"] for q in quotes.QUOTES],\
        f"Expected the quote to be from QUOTES list, instead got '{actual[0]}"
    def test_get_random_quote_length(self):
        "Verify get_random_quote returns correct number of quotes"
        actual = quotes.get_random_quote(3)
        assert len(actual) == 3, f"Expected 3 quotes and got {len(actual)}"

