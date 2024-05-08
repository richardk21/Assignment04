# Assignment 04 - Validating Input.
# Part 1
# Read in all questions in the csv

with open('questions.csv', 'r') as file:
    questions = file.readlines()

questions = [question.strip() for question in questions]

def is_question_correct(questions):
    if questions.endswith("?"):
        return "yes"
    else:
        return "No"

for quesiton in questions:
    while True:
        response = input(f"Is the question '{questions}' correct? (yes/no): ").lower()
        if response == is_question_correct(questions).lower():
            print("Yes!")
        else:
            print("No")

'''
# Part 3
# Read in all questions in the questions.csv file
questions = []
with open('questions.csv', 'r') as question_file:
    data = question_file.read().strip().split('\n')[1:]
    for row in data:
        parts = row.strip().split(',')
        questions.append([int(parts[0]), parts[1]])
print(questions)

# Read in all answers in the answers.csv file
answers = []
with open('answers.csv', 'r') as answers_file:
    data = answers_file.read().strip().split('\n')[1:]
    for row in data:
        parts = row.strip().split(',')
        parts[1] = int(parts[1])
        answers.append(parts)
print(answers)

# Prints out the questions, one at a time, along with corresponding set of answers from all interviewees.
for question in questions:
    print(question[1])
    for answer in answers:
        if(question[0]) == answer[1]:
            print(f'{answer[0]} answered {answer[2]}')
'''
