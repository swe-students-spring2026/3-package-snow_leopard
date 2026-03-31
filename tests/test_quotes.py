import pytest
from pyquotes import quotes

class Tests:
    def test_get_quote_by_type_invalid_type(self):
        """
        Tests that get_quote_by_type raises an exception 
        when the type does not exist
        """
        with pytest.raises(ValueError):
            quotes.get_quote_by_type("nonexistent_type")

    def test_get_quote_by_type_invalid_low(self):
        """
        Tests that get_quote_by_type raises an exception 
        when num_of_quotes is less than 1
        """
        with pytest.raises(ValueError):
            quotes.get_quote_by_type("love", 0)

    def test_get_quote_by_type_invalid_high(self):
        """
        Tests that get_quote_by_type raises an exception 
        when num_of_quotes is larger than available quotes of that type
        """
        with pytest.raises(ValueError):
            quotes.get_quote_by_type("love", 1000)

    def test_get_quote_by_type_returns_string(self):
        """
        Test that get_quote_by_type returns a string when requesting 1 quote
        """
        actual = quotes.get_quote_by_type("love")
        assert isinstance(actual, str), f"Expected a string, got {type(actual)}"

    def test_get_quote_by_type_returns_list(self):
        """
        Test that get_quote_by_type returns a list when requesting multiple quotes
        """
        actual = quotes.get_quote_by_type("life", 2)
        assert isinstance(actual, list), f"Expected a list, got {type(actual)}"

    def test_get_quote_by_type_content(self):
        """
        Test that returned quote(s) are from the correct type in QUOTES
        """
        actual = quotes.get_quote_by_type("motivation", 1)
        assert actual in [q["text"] for q in quotes.QUOTES if q["type"] == "motivation"], \
        f"Expected a motivation quote, got '{actual}'"

    def test_get_quote_by_type_length(self):
        """
        Verify get_quote_by_type returns correct number of quotes
        """
        actual = quotes.get_quote_by_type("friendship", 2)
        assert len(actual) == 2, f"Expected 2 quotes and got {len(actual)}"
    
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
        assert isinstance(actual,list)
    def test_get_random_quote_content(self):
        """
        Test that get_random_quote returned quotes that are from QUOTE
        """
        actual = quotes.get_random_quote(1)
        assert actual[0] in [q["text"] for q in quotes.QUOTES]
    def test_get_random_quote_length(self):
        "Verify get_random_quote returns correct number of quotes"
        actual = quotes.get_random_quote(3)
        assert len(actual) == 3

    def test_get_compliment_returns_string(self):
        """
        Test that get_compliment returns one compliment string by default.
        """
        actual = quotes.get_compliment()
        assert isinstance(actual, str)

    def test_get_compliment_appearance_filter(self):
        """
        Test that appearance=True only returns appearance compliments.
        """
        actual = quotes.get_compliment(appearance=True)
        expected = [c["text"] for c in quotes.COMPLIMENTS if c["appearance"]]
        assert actual in expected

    def test_get_compliment_personality_filter(self):
        """
        Test that personality=True only returns personality compliments.
        """
        actual = quotes.get_compliment(personality=True)
        expected = [c["text"] for c in quotes.COMPLIMENTS if c["personality"]]
        assert actual in expected

    def test_get_compliment_corny_filter(self):
        """
        Test that corny=True uses the default appearance=True filter.
        """
        actual = quotes.get_compliment(corny=True)
        expected = [
            c["text"] for c in quotes.COMPLIMENTS if c["appearance"] and c["corny"]
        ]
        assert actual in expected

    def test_get_compliment_personality_and_corny_filter(self):
        """
        Test that personality and corny can be combined successfully.
        """
        actual = quotes.get_compliment(personality=True, corny=True)
        expected = [
            c["text"] for c in quotes.COMPLIMENTS if c["personality"] and c["corny"]
        ]
        assert actual in expected

    def test_get_quotes_by_author_name_invalid_type(self):
        """
        Test if author name inserted is a string
        """
        with pytest.raises(TypeError):
            quotes.get_quotes_by_author_name(123)

    def test_get_quotes_by_author_name_invalid_author(self):
        """
        Test to see if the author given exists
        """
        with pytest.raises(ValueError):
            quotes.get_quotes_by_author_name("nonexistent_author")

    def test_get_quotes_by_author_name_returns_list(self):
        """
        Test that function returns a list
        """
        actual = quotes.get_quotes_by_author_name("Mahatma Gandhi")
        assert isinstance(actual, list), f"Expected a list, got {type(actual)}"

    def test_get_quotes_by_author_name_content(self):
        """
        Test that quotes are from author
        """
        actual = quotes.get_quotes_by_author_name("Mahatma Gandhi")
        expected = [q["text"] for q in quotes.QUOTES if q["author"] == "Mahatma Gandhi"]
        assert actual == expected, f"Expected {expected}, got {actual}"

    def test_get_quotes_by_author_name_case_insensitive(self):
        """
        Test that author matching is case-insensitive
        """
        actual = quotes.get_quotes_by_author_name("mahatma gandhi")
        expected = [q["text"] for q in quotes.QUOTES if q["author"] == "Mahatma Gandhi"]
        assert actual == expected, f"Expected {expected}, got {actual}"

    def test_get_quotes_by_author_name_strips_whitespace(self):
        """
        Test that leading and trailing spaces are ignored
        """
        actual = quotes.get_quotes_by_author_name("  Mahatma Gandhi  ")
        expected = [q["text"] for q in quotes.QUOTES if q["author"] == "Mahatma Gandhi"]
        assert actual == expected, f"Expected {expected}, got {actual}"

    def test_get_quotes_by_author_name_length(self):
        """
        Tests for the correct number of quotes
        """
        actual = quotes.get_quotes_by_author_name("Mahatma Gandhi")
        expected = [q["text"] for q in quotes.QUOTES if q["author"] == "Mahatma Gandhi"]
        assert len(actual) == len(expected), f"Expected {len(expected)}, got {len(actual)}"