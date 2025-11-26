from brain_games.games import game_selector, task_text_selector
from brain_games.user_interaction import get_user_answer, get_user_name, greet


def logic_of_games(game_name):
    greet()
    user_name = get_user_name()
    correct_answers_count = 0
    game_info = ['question', 'correct_unswer']
    task_text = task_text_selector(game_name)
    print(task_text)
    while correct_answers_count < 3:
        game_info = game_selector(game_name)
        print(f'Question: {game_info[0]}')
        user_answer = get_user_answer()
        if user_answer == game_info[1]:
            correct_answers_count += 1
            print('Correct!')
        else:
            correct_answers_count = 4
            text = 'is wrong answer ;(. Correct answer was'
            print(f'\'{user_answer}\' {text} \'{game_info[1]}\'.')
            print(f'Let\'s try again, {user_name}!')

    if correct_answers_count == 3:
        print(f'Congratulations, {user_name}!')
