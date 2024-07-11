#!/usr/bin/env python3


from brain_games.cli import welcome_user
import random
import prompt


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    number_of_question = 3
    while number_of_question > 0:
        numeric = random.randint(1, 100)
        print(f'Question: {numeric}')
        for i in range(2, numeric // 2):
            if numeric % i == 0:
                correct_answer = 'no'
                break
        else:
            correct_answer = 'yes'
        user_answer = prompt.string('Your answer: ')
        if user_answer.lower() != correct_answer:
            print(f'"{user_answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
        number_of_question -= 1
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
