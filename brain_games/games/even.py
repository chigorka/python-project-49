import random
from brain_games.engine import run_game
from brain_games.constants import TASK_EVEN


def even_question_and_result():
    number = random.randint(1, 100)
    question = f'{number}'
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return question, result


def run_even_game():
    run_game(TASK_EVEN, even_question_and_result)
