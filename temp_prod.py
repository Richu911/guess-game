from enum import StrEnum
from random import randint

RANGE_START = 1
RANGE_END = 10
ANSWER = randint(RANGE_START, RANGE_END)

class GuessOutcome(StrEnum):
    TOO_LOW = "guess is too low"
    TOO_HIGH = "guess is too high"
    OUT_OF_RANGE = "Number out of range"
    WIN = "you win !"
    UNRECOGNIZED = "input is invalid"
    QUIT = "game over"
    NOT_QUIT = "welcome back !"

def check_guess(guess: str) -> GuessOutcome:
    if guess == quit:
        return maybe_quit()
    
    try:
        guess_int = int(guess)
    except ValueError:
        return GuessOutcome.UNRECOGNIZED
    
    if guess_int == ANSWER:
        return GuessOutcome.WIN
    elif not RANGE_START <= guess_int <= RANGE_END:
        return GuessOutcome.OUT_OF_RANGE
    elif guess_int < ANSWER:
        return GuessOutcome.TOO_LOW
    elif guess_int > ANSWER:
        return GuessOutcome.TOO_HIGH
    
def maybe_quit() -> GuessOutcome:
    quit_conf = input("are you sure you want to quit - Y/n ?: ").lower
    if not quit_conf or quit_conf == "y":
        return GuessOutcome.QUIT
    elif quit_conf == "n":
        return GuessOutcome.NOT_QUIT
    else:
        return GuessOutcome.UNRECOGNIZED
    
def guess_game():
    while True:
        guess = input("enter a no b/w 1 and 10 (inclusive): ")
        result = check_guess(guess)
        print(result)
        if result in {GuessOutcome.WIN, GuessOutcome.QUIT}:
            return result

if __name__ == "__main__":
    guess_game()
