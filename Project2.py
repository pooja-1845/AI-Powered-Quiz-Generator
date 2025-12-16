import random

# OOP: Question class
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

def quiz():
    score = 0

    for i in range(3):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        question = Question(f"What is {a} + {b}?", a + b)

        user_ans = int(input(question.question + " "))

        if user_ans == question.answer:
            print("Correct")
            score += 1
        else:
            print("Wrong")

    print("Final Score:", score)

quiz()
