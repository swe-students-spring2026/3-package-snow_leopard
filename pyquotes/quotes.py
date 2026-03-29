import random

QUOTES=[
    {"text": "Be the change that you wish to see in the world.", "author": "Mahatma Gandhi", "type": "motivation"},
    {"text": "It does not matter how slowing you go as long as you do not stop", "author": "Confucius","type": "motivation"},
    {"text": "In three words I can sum up everything I've learned about life: it goes on.", "author": "Robert Frost","type": "life"},
    {"text": "You only live once, but if you do it right, once is enough", "author": "Mae West", "type": "life"},
    {"text": "A friend is someone who knows all about you and still loves you.", "author": "Elbert Hubbard", "type": "friendship"},
    {"text": "Friendship ... is born at the moment when one man says to another 'What! You too?'", "author": "C.S. Lewis", "type": "friendship"},
    {"text": "We accept the love we think we deserve.", "author": "Stephen Chbosky", "type": "love"},
    {"text": "You know you're in love when you can't fall asleep because reality is finally better than your dreams.", "author": "Dr.Seuss", "type": "love"},
]

COMPLIMENTS = [
    {"text": "Your smile could make a cloudy day file for overtime.", "appearance": True, "personality": False, "corny": True},
    {"text": "You look like you were rendered in high definition.", "appearance": True, "personality": False, "corny": False},
    {"text": "Your style is so sharp it could debug a dull room.", "appearance": True, "personality": False, "corny": True},
    {"text": "You have the kind of presence that turns heads quietly.", "appearance": True, "personality": False, "corny": False},
    {"text": "You make kindness look like a superpower.", "appearance": False, "personality": True, "corny": False},
    {"text": "Your positivity could charge a dead laptop.", "appearance": False, "personality": True, "corny": True},
    {"text": "You are the human version of a reassuring green check mark.", "appearance": False, "personality": True, "corny": True},
    {"text": "You make people feel heard, and that is rare.", "appearance": False, "personality": True, "corny": False},
]

def get_random_quote(num_of_quotes):
    """
    Returns a specified number of random quotes from QUOTES
    as a list of the text values
    """
    if num_of_quotes < 1:
        raise ValueError ("Number of quotes must be at least 1")
    if num_of_quotes > len(QUOTES):
        raise ValueError (f"Number of quotes cannot be greater than {len(QUOTES)}")
    random_quotes = random.sample(QUOTES, num_of_quotes)
    random_quote_texts =[]
    for q in random_quotes:
        random_quote_texts.append(q["text"])
    return random_quote_texts


def get_compliment(appearance=False, personality=False, corny=False):
    """
    Return one random compliment filtered by the requested boolean tags.
    """
    filters = {"appearance": appearance, "personality": personality, "corny": corny}

    if not all(isinstance(value, bool) for value in filters.values()):
        raise TypeError("appearance, personality, and corny must be booleans")

    # A compliment must satisfy every requested tag to be included.
    matches = [
        compliment["text"]
        for compliment in COMPLIMENTS
        if all(not filters[tag] or compliment[tag] for tag in filters)
    ]

    if not matches:
        raise ValueError("No compliments match the requested tags")

    return random.choice(matches)


