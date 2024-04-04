hr_question_database = {
    'general': [
        "Tell me about yourself.",
        "Why are you interested in this position?",
        "What are your strengths and weaknesses?",
        "Where do you see yourself in 5 years?",
        "Why are you looking to leave your current job?"
    ],
    'experience': [
        "Describe a challenging situation you faced and how you overcame it.",
        "What is your greatest professional achievement?",
        "How do you handle conflicts or difficult coworkers?",
        "Give an example of a time when you had to adapt to a new situation.",
        "Describe a time when you had to make a difficult decision."
    ],
    'motivation': [
        "What motivates you?",
        "What interests you about our company/industry?",
        "What are your career goals?",
        "Why should we hire you?",
        "What do you know about our company culture?"
    ],
    'management': [
        "How would you motivate your team members?",
        "Describe your leadership style.",
        "How do you handle performance issues with team members?",
        "How do you prioritize tasks and manage your time effectively?",
        "How do you handle criticism or feedback?"
    ]
}

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
        break

    selected_categories = []
    for number in category_input.split():
        try:
            category_index = int(number) - 1
            if 0 <= category_index < len(remaining_categories):
                selected_category = remaining_categories.pop(category_index)
                selected_categories.append(selected_category)
        except ValueError:
            print(f"Invalid input: {number}")

    questions = generate_questions(selected_categories)
    print("\nCommon HR Interview Questions:")
    for question in questions:
        print("- " + question)

    if not selected_categories:
        print("All categories covered. Exiting...")
        break
