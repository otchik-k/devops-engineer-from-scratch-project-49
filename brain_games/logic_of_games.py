from brain_games.user_interaction import get_user_name, get_user_answer, greet
from brain_games.games import game_selector


def logic_of_games(game_name):
    greet()
    user_name = get_user_name()
    correct_answers_count = 0
    game_information = [ 'question', 'correct_unswer']
    while correct_answers_count < 3:
        game_information = game_selector(game_name)
        print(game_information[2])
        print(f'Question: {game_information[0]}')
        user_answer = get_user_answer()
        if user_answer == game_information[1]:
            correct_answers_count +=1
            print('Correct!')
        else:
            correct_answers_count = 4
            print(f'\'{user_answer}\' is wrong answer ;(. Correct answer was \'{game_information[1]}\'.')
            print(f'Let\'s try again, {user_name}!')

    if correct_answers_count == 3:
        print(f'Congratulations, {user_name}!')
