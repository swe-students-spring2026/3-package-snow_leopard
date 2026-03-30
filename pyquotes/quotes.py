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

FORTUNES = [
    # --- TECH & DEBUGGING ---
    {"text": "Your code will compile on the first try today.", "topic": "tech"},
    {"text": "A missing semicolon will reveal itself to you in a dream.", "topic": "tech"},
    {"text": "You will soon discover yet another JavaScript framework to learn.", "topic": "tech"},
    {"text": "The bug you have been chasing for three days is actually just a typo.", "topic": "tech"},
    {"text": "Your next Stack Overflow search will yield an answer from 2014 that perfectly solves your problem.", "topic": "tech"},
    {"text": "The technical debt you ignored yesterday will introduce itself tomorrow.", "topic": "tech"},
    {"text": "You will soon experience the deep, spiritual joy of deleting thousands of lines of legacy code.", "topic": "tech"},
    {"text": "An unexpected 'git push --force' will test your patience and your backups.", "topic": "tech"},
    {"text": "A sudden debugging epiphany will strike you the moment you step away from your keyboard.", "topic": "tech"},
    {"text": "Your server logs will actually contain the exact error message you need.", "topic": "tech"},
    {"text": "You will spend 4 hours automating a task that would have taken 5 minutes to do manually.", "topic": "tech"},
    
    # --- CAREER & TEAMWORK ---
    {"text": "An exciting opportunity will present itself at your next standup meeting.", "topic": "career"},
    {"text": "The senior engineer will finally approve your pull request without requesting any changes.", "topic": "career"},
    {"text": "A meeting that was scheduled for a full hour will magically end in 15 minutes.", "topic": "career"},
    {"text": "Your next performance review will feature the phrase '10x developer'.", "topic": "career"},
    {"text": "You will successfully explain what an API is to a non-technical manager.", "topic": "career"},
    {"text": "Your code deployment on a Friday afternoon will surprisingly go off without a hitch.", "topic": "career"},
    
    # --- LOVE & GENERAL ---
    {"text": "A thrilling time is in your immediate future.", "topic": "general"},
    {"text": "The caffeine will hit exactly when you need it most.", "topic": "general"},
    {"text": "Someone is admiring your beautifully formatted README from afar.", "topic": "love"},
    {"text": "True love is just one approved pull request away.", "topic": "love"},
    {"text": "You and your pair-programming partner will share a moment of pure synergy.", "topic": "love"}
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



