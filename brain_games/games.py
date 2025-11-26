import math
import random


def task_text_selector(game_name):
    if game_name == 'brain_even':
        return 'Answer \"yes\" if the number is even, otherwise answer \"no\".'
    if game_name == 'brain_calc':
        return 'What is the result of the expression?'
    if game_name == 'brain_gcd':
        return 'Find the greatest common divisor of given numbers.'
    if game_name == 'brain_progression':
        return 'What number is missing in the progression?'
    if game_name == 'brain_prime':
        return 'Answer \"yes\" if given number is prime. Otherwise answer \"no\".'


def game_selector(game_name):
    if game_name == 'brain_even':
        return brain_even()
    if game_name == 'brain_calc':
        return brain_calc()
    if game_name == 'brain_gcd':
        return brain_gcd()
    if game_name == 'brain_progression':
        return brain_progression()
    if game_name == 'brain_prime':
        return brain_prime()


def brain_even():
    random_number = random.randint(1, 99)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return [random_number, correct_answer]


def brain_calc():
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
    return [math_formula, correct_answer]


def brain_gcd():
    x = random.randint(1, 99)
    y = random.randint(1, 99)
    result = math.gcd(x, y)
    task = f'{x} {y}'
    return [task, str(result)]
    
    
def brain_progression():
    start_number = random.randint(1, 99)
    difference = random.randint(1, 99)
    number_count = random.randint(5, 10)
    position_hidden_element = random.randint(0, number_count - 1)
    arithmetic_sequence = []
    for i in range(number_count):
        member_progression = start_number + i * difference
        arithmetic_sequence.append(member_progression)
    correct_answer = str(arithmetic_sequence[position_hidden_element])
    arithmetic_sequence[position_hidden_element] = '..'
    str_arithmetic_sequence = ''
    for i in range(len(arithmetic_sequence)):
        str_arithmetic_sequence = str_arithmetic_sequence + ' ' + str(arithmetic_sequence[i])
    str_arithmetic_sequence = str_arithmetic_sequence.strip()
    return [str_arithmetic_sequence, correct_answer]
    
    
def brain_prime():
    x = random.randint(1, 99)
    if x <= 1:
        return [x, 'no']
    for i in range(2, x):
        if x % i == 0:
            return [x, 'no']
    return [x, 'yes']
    