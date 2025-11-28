import math
import random

from brain_games.config import (
    BRAIN_CALC,
    BRAIN_EVEN,
    BRAIN_GCD,
    BRAIN_PRIME,
    BRAIN_PROGRESSION,
    CALC_FINAL_RAND,
    CALC_INIT_RAND,
    COUNT_FINAL_RAND,
    COUNT_INIT_RAND,
    DIF_FINAL_RAND,
    DIF_INIT_RAND,
    EVEN_FINAL_RAND,
    EVEN_INIT_RAND,
    FIREST_NUM_FINAL_RAND,
    FIRST_NUM_INIT_RAND,
    GCD_FINAL_NUM_RAND,
    GCD_INIT_NUM_RAND,
    PRIME_FINAL_RAND,
    PRIME_INIT_RAND,
    TASK_CALC,
    TASK_EVEN,
    TASK_GCD,
    TASK_PRIME,
    TASK_PROGRESSION,
)


def task_text_selector(game_name):
    if game_name == BRAIN_EVEN:
        return TASK_EVEN
    if game_name == BRAIN_CALC:
        return TASK_CALC
    if game_name == BRAIN_GCD:
        return TASK_GCD
    if game_name == BRAIN_PROGRESSION:
        return TASK_PROGRESSION
    if game_name == BRAIN_PRIME:
        return TASK_PRIME


def game_selector(game_name):
    if game_name == BRAIN_EVEN:
        return brain_even()
    if game_name == BRAIN_CALC:
        return brain_calc()
    if game_name == BRAIN_GCD:
        return brain_gcd()
    if game_name == BRAIN_PROGRESSION:
        return brain_progression()
    if game_name == BRAIN_PRIME:
        return brain_prime()


def brain_even():
    random_number = random.randint(EVEN_INIT_RAND, EVEN_FINAL_RAND)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return [random_number, correct_answer]


def brain_calc():
    # Указывал X и Y как стандартные обозначения в математических формулах
    x = random.randint(CALC_INIT_RAND, CALC_FINAL_RAND)
    y = random.randint(CALC_INIT_RAND, CALC_FINAL_RAND)
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
    # Указывал X и Y как стандартные обозначения в математических формулах
    x = random.randint(GCD_INIT_NUM_RAND, GCD_FINAL_NUM_RAND)
    y = random.randint(GCD_INIT_NUM_RAND, GCD_FINAL_NUM_RAND)
    result = math.gcd(x, y)
    task = f'{x} {y}'
    return [task, str(result)]
    
    
def brain_progression():
    start_number = random.randint(FIRST_NUM_INIT_RAND, FIREST_NUM_FINAL_RAND)
    difference = random.randint(DIF_INIT_RAND, DIF_FINAL_RAND)
    number_count = random.randint(COUNT_INIT_RAND, COUNT_FINAL_RAND)
    position_hidden_element = random.randint(0, number_count - 1)
    arithmetic_sequence = []
    for i in range(number_count):
        member_progression = start_number + i * difference
        arithmetic_sequence.append(member_progression)
    correct_answer = str(arithmetic_sequence[position_hidden_element])
    arithmetic_sequence[position_hidden_element] = '..'
    str_sequence = ''
    for i in range(len(arithmetic_sequence)):
        str_sequence = str_sequence + ' ' + str(arithmetic_sequence[i])
    str_sequence = str_sequence.strip()
    return [str_sequence, correct_answer]
    
    
def brain_prime():
    # Указывал X и Y как стандартные обозначения в математических формулах
    x = random.randint(PRIME_INIT_RAND, PRIME_FINAL_RAND)
    if x <= 1:
        return [x, 'no']
    for i in range(2, x):
        if x % i == 0:
            return [x, 'no']
    return [x, 'yes']
    