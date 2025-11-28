import prompt

from brain_games.config import GREETING_TEXT


def greet():
    print(GREETING_TEXT)


def get_user_name():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_user_answer():
    answer = prompt.string('Your answer: ')
    return answer