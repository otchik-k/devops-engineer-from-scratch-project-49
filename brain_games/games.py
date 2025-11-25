import random


def game_selector(game_name):
    if game_name == 'brain_even':
        return brain_even()
    if game_name == 'brain_calc':
        return brain_calc()


def brain_even():
    task = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'
    random_number = random.randint(1, 99)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return [random_number, correct_answer, task]


def brain_calc():
    task = 'What is the result of the expression?'
    x = random.randint(1, 99)
    y = random.randint(1, 99)
    math_action = random.choice(['-', '+', '*'])
    math_formula = ''
    correct_answer = ''
    if math_action == '-':
        math_formula = f'{x} - {y}'
        correct_answer = str(x - y)
    elif math_action == '+':
        math_formula = f'{x} + {y}'
        correct_answer = str(x + y)
    elif math_action == '*':
        math_formula = f'{x} * {y}'
        correct_answer = str(x * y)
    return [math_formula, correct_answer, task]
