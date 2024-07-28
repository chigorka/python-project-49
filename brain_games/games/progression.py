import random
from brain_games.constants import TASK_PROGRESSION
from brain_games.engine import run_game


def progression_question_and_result():
    seria = []
    current_number = random.randint(1, 50)
    delta = random.randint(1, 10)
    for _ in range(10):
        seria.append(str(current_number))
        current_number += delta
    skip_index = random.randint(0, 9)
    result = seria[skip_index]
    seria[skip_index] = '..'
    progression = ' '.join(seria)
    question = f'{progression}'
    return question, result


def run_progression_game():
    run_game(TASK_PROGRESSION, progression_question_and_result)
