#!/usr/bin/env python3


from brain_games.cli import welcome_user
import random
import prompt


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    number_of_question = 3
    while number_of_question > 0:
        first_numeric = random.randint(1, 100)
        second_numeric = random.randint(1, 100)
        print(f'Question: {first_numeric} {second_numeric}')
        user_answer = prompt.string('Your answer: ')
        while first_numeric != 0 and second_numeric != 0:
            if first_numeric > second_numeric:
                first_numeric = first_numeric % second_numeric
            else:
                second_numeric = second_numeric % first_numeric
        correct_answer = str(first_numeric + second_numeric)
        if user_answer != correct_answer:
            print(f'{user_answer} is wrong answer ;(. '
                  f'Correct answer was {correct_answer}.')
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
        number_of_question -= 1
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
