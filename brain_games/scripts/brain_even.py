from brain_games.cli import welcome_user
import random
import prompt


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number_of_question = 3
    while number_of_question > 0:
        numeric = random.randint(1, 100)
        print(f'Question: {numeric}')
        user_answer = prompt.string('Your answer: ')
        if numeric % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
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
