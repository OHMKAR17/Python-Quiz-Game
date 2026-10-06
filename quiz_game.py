questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is mainly used for web page structure?",
        "options": ["A. Python", "B. Java", "C. HTML", "D. C++"],
        "answer": "C"
    },
    {
        "question": "What is 10 × 5?",
        "options": ["A. 15", "B. 50", "C. 100", "D. 25"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. fun", "D. def"],
        "answer": "D"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. Float"],
        "answer": "C"
    }
]


score = 0

print("==============================")
print("       PYTHON QUIZ GAME")
print("==============================")

name = input("Enter your name: ")

print(f"\nWelcome, {name}!")
print("Answer each question by entering A, B, C, or D.\n")

for number, question in enumerate(questions, start=1):

    print(f"Question {number}: {question['question']}")

    for option in question["options"]:
        print(option)

    answer = input("Your answer: ").upper()

    if answer == question["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! Correct answer: {question['answer']}\n")


print("==============================")
print("           RESULTS")
print("==============================")

print(f"Player: {name}")
print(f"Score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100

print(f"Percentage: {percentage:.0f}%")

if percentage == 100:
    print("Excellent! Perfect score.")
elif percentage >= 60:
    print("Good job!")
else:
    print("Keep practicing!")