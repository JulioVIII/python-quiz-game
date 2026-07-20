#python_game.py

questions = [
    {
        "question": "What is the capital of France?",
        "answer": "paris"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "answer": "def"
    },
    {
        "question": "What symbol is used to start a comment in Python?",
        "answer": "#"
    },
    {
        "question": "Which data type is used to store True or False?",
        "answer": "boolean"
    },
    {
        "question": "What function is used to display text on the screen?",
        "answer": "print"
    }
]

score = 0

print("===== PYTHON QUIZ GAME =====")

for question in questions:
    print()
    print(question["question"])

    answer = input("Your answer: ").lower()

    if answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {question['answer']}")

print()
print("===== RESULTS =====")
print(f"Your score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100

print(f"Percentage: {percentage:.1f}%")

if percentage == 100:
    print("Excellent!")
elif percentage >= 80:
    print("Great job!")
elif percentage >= 60:
    print("Good work!")
else:
    print("Keep practicing!")
