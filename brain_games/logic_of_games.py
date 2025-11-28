from brain_games.config import (
    CONGRATULATIONS_TEXT,
    CORRECT_ANSWER_TEXT,
    QUESTION_TEXT,
    TEXT_TO_LOSE,
    TRY_AGAIN_TEXT,
)
from brain_games.games import game_selector, task_text_selector
from brain_games.user_interaction import get_user_answer, get_user_name, greet


def logic_of_games(game_name):
    greet()
    user_name = get_user_name()
    correct_answers_count = 0
    game_info = ['question', 'correct_answer']
    QUESTION = 0
    CORRECT_ANSWER = 1
    task_text = task_text_selector(game_name)
    print(task_text)
    while correct_answers_count < 3:
        game_info = game_selector(game_name)
        print(f'{QUESTION_TEXT} {game_info[QUESTION]}')
        user_answer = get_user_answer()
        if user_answer == game_info[CORRECT_ANSWER]:
            correct_answers_count += 1
            print(CORRECT_ANSWER_TEXT)
        else:
            correct_answers_count = 4
            print(f'\'{user_answer}\'{TEXT_TO_LOSE}\'{game_info[CORRECT_ANSWER]}\'.')
            print(f'{TRY_AGAIN_TEXT}, {user_name}!')

    if correct_answers_count == 3:
        print(f'{CONGRATULATIONS_TEXT}, {user_name}!')