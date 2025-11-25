import random

import prompt

from brain_games.welcome_user import welcome_user


def game_checking_party():

    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count_correct_answers = 0

    while count_correct_answers < 3:
        random_number = random.randint(1, 99)
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = ''
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if user_answer == correct_answer:
            count_correct_answers += 1
            print('Correct!')
        else:
            count_correct_answers = 4
            print(f'\'{user_answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {user_name}')

    if count_correct_answers == 3:
        print(f'Congratulations, {user_name}!')
