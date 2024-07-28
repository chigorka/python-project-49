import random
from brain_games.engine import run_game
from brain_games.constants import TASK_CALC


def calc_question_and_result():
    operators_list = ['+', '-', '*']
    operator = random.choice(operators_list)
    first_operand = random.randint(1, 100)
    second_operand = random.randint(1, 100)
    question = f'{first_operand} {operator} {second_operand}'
    match operator:
        case '+':
            result = first_operand + second_operand
        case '-':
            result = first_operand - second_operand
        case '*':
            result = first_operand * second_operand
    return question, str(result)


def run_calc_game():
    run_game(TASK_CALC, calc_question_and_result)
