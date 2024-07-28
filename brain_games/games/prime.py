import random
from brain_games.constants import TASK_PRIME
from brain_games.engine import run_game


def prime_question_and_result():
    number = random.randint(2, 100)
    question = f'{number}'
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            result = 'no'
            break
    else:
        result = 'yes'
    return question, result


def run_prime_game():
    run_game(TASK_PRIME, prime_question_and_result)
