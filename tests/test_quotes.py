import pytest 
from pyquotes import quotes

class Tests:
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


 