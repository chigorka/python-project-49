import random
from brain_games.constants import TASK_GCD
from brain_games.engine import run_game


def gcd_question_and_result():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    question = f'{first_number} {second_number}'
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number
    result = first_number + second_number
    return question, str(result)


def run_gcd_game():
    run_game(TASK_GCD, gcd_question_and_result)
