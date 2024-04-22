import json
import os
import random


def select_questions():
    question_database: dict[str, list[str]] = {}
    with open('questions.json') as questions:
        question_database = json.load(questions)
    selected_questions = {}
    for category in question_database.keys():
        # Selecting 2 random questions per category from `questions database`
        selected_questions.update(
            {category: random.sample(question_database[category], 3)}
        )
    return selected_questions


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    previous_output = ''
    questions = select_questions()
    while True:
        clear_screen()
        print(previous_output, '\n')
        if not len(questions.keys()):
            print('All questions have been displayed.')
            break
        print('Enter the category number for HR questions ' +
              '(\'q\' to quit): ')
        for i, category in enumerate(questions.keys()):
            print(f'{i+1}: {category}')
        user_input = input()
        if user_input.isalpha():
            if user_input == 'q':
                break
            else:
                continue
        else:
            user_input = int(user_input)
        if user_input in range(len(questions.items())+1):
            previous_output = '\n'.join(questions.pop(
                list(questions.keys())[user_input-1]))
