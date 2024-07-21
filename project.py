import random

WORDS = ["Python","java", "C+", "jumble", "CS50", "easy", "difficult", "answer", "telephone", "testing", "important"]

def main():
    score = 0
    display_rules()
    while True:
        word = get_random_words()
        scrambled_word = scramble_word(word)
        print(f"Scrambled word: {scrambled_word}")

        guess = input("Your guess: ")
        if guess.lower() == 'exit':
            break

        if check_guess(word, guess):
            print("Correct Guess!!\n")
            score += 1
        else:
            print(f"Wrong! The correct word was {word}.\n")

    print(f"\nYour final score is {score}.\n")


def display_rules():
    rules = """
    Welcome to the Word Scramble Game!
    Rules:
    1. A scrambled word will be displayed.
    2. You need to guess the original word.
    3. Type your guess and press Enter.
    4. Result will be shown!!.
    5. Type 'exit' to end the game and see your final score.
    """
    print(rules)

def get_random_words():
    return random.choice(WORDS)

def scramble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)


def check_guess(correct_word, guess):
    return correct_word == guess

if __name__ == "__main__":
    main()
