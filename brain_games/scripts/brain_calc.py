from brain_games.cli import welcome_user
import random
import prompt


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    number_of_question = 3
    operators_list = ['+', '-', '*']
    while number_of_question > 0:
        first_operand = random.randint(1, 100)
        second_operand = random.randint(1, 100)
        operator = operators_list[random.randint(0, 2)]
        print(f'Question: {first_operand} {operator} {second_operand}')
        user_answer = prompt.string('Your answer: ')
        match operator:
            case '+':
                correct_answer = first_operand + second_operand
            case '-':
                correct_answer = first_operand - second_operand
            case '*':
                correct_answer = first_operand * second_operand
        if user_answer != str(correct_answer):
            print(f'{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.')
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
        number_of_question -= 1
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
