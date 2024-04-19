import json

hr_question_database = {}

with open('questions.json') as questions:
    hr_question_database = json.load(questions)


def generate_questions(categories):
    questions = []
    for category in categories:
        if category in hr_question_database:
            questions.extend(hr_question_database[category])
    return questions


print("Categories of HR questions available:")
category_list = list(hr_question_database.keys())
for i, category in enumerate(category_list, start=1):
    print(f"{i}. {category.capitalize()}")

while True:
    remaining_categories = category_list.copy()
    print("\nEnter the category number for HR questions ('q' to quit):")
    category_input = input()
    if category_input.lower() == 'q':
        print("Exiting program...")
        break

    selected_categories = []
    for number in category_input.split():
        try:
            category_index = int(number) - 1
            if 0 <= category_index < len(remaining_categories):
                selected_category = remaining_categories.pop(category_index)
                selected_categories.append(selected_category)
            else:
                print(f"Invalid input: {number}")
        except ValueError:
            print(f"Invalid input: {number}")

    if not selected_categories:
        print("Please Enter Valid Input From Categories.")
        continue
    questions = generate_questions(selected_categories)
    print("\nCommon HR Interview Questions:")
    for question in questions:
        print("- " + question)
