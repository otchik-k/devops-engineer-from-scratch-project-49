import prompt

greeting_text = "Welcome to the Brain Games!"


def greet():
    print(greeting_text)


def get_user_name():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_user_answer():
    answer = prompt.string('Your answer: ')
    return answer