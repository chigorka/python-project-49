#!/usr/bin/env python3


from brain_games.cli import welcome_user
import random
import prompt


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    number_of_question = 3
    while number_of_question > 0:
        seria = []
        skip_index = random.randint(0, 9)
        current_number = random.randint(1, 50)
        delta = random.randint(1, 10)
        for _ in range(10):
            seria.append(str(current_number))
            current_number += delta
        correct_answer = seria[skip_index]
        seria[skip_index] = '..'
        progression = ' '.join(seria)
        print(f'Question: {progression}')
        user_answer = prompt.string('Your answer: ')
        if str(user_answer) != correct_answer:
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
