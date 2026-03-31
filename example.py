"""Example script demonstrating the pyquotes package."""

from pyquote import quotes


def show_random_quotes():
    print("Random quotes (2):")
    for q in quotes.get_random_quote(2):
        print(f"- {q}")
    print()


def show_quotes_by_type():
    print("Quote by type (love):")
    print(f"- {quotes.get_quote_by_type('love')}")
    print("\nQuotes by type (life, 2):")
    for q in quotes.get_quote_by_type("life", 2):
        print(f"- {q}")
    print()


def show_compliments():
    print("Compliment (default):")
    print(f"- {quotes.get_compliment()}")
    print("\nCompliment (appearance):")
    print(f"- {quotes.get_compliment(appearance=True)}")
    print("\nCompliment (personality):")
    print(f"- {quotes.get_compliment(personality=True)}")
    print("\nCompliment (corny):")
    print(f"- {quotes.get_compliment(corny=True)}")
    print()


def show_fortunes():
    for topic in ("general", "tech", "career", "love"):
        print(f"Fortune ({topic}):")
        print(f"- {quotes.get_fortune(topic)}\n")


def show_quotes_by_author():
    print("Quotes by Mahatma Gandhi:")
    for q in quotes.get_quotes_by_author_name("Mahatma Gandhi"):
        print(f"- {q}")
    print()


def main():
    print(" 'Pyquotes Demo' \n")
    show_random_quotes()
    show_quotes_by_type()
    show_compliments()
    show_fortunes()
    show_quotes_by_author()


if __name__ == "__main__":
    main()
