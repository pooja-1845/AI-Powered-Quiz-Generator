import random
from datetime import datetime

# OOP: Quiz Question class
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# Function to generate random math questions
def generate_math_questions(n=5):
    questions = []
    for _ in range(n):
        a, b = random.randint(1,50), random.randint(1,50)
        op = random.choice(["+", "-", "*"])
        prompt = f"What is {a} {op} {b}?"
        # Lambda to calculate correct answer
        answer = (lambda x,y,o: x+y if o=="+" else x-y if o=="-" else x*y)(a,b,op)
        questions.append(Question(prompt, answer))
    return questions

def conduct_quiz(questions):
    score = 0
    for q in questions:
        try:
            user_ans = int(input(q.prompt + " "))
            if user_ans == q.answer:
                print("Correct!")
                score += 1
            else:
                print("Wrong! Correct answer:", q.answer)
        except ValueError:
            print("Invalid input!")
    print(f"\nYour score: {score}/{len(questions)}")
    return score

def save_score(score, filename="scores.csv"):
    """Save score with timestamp"""
    try:
        with open(filename, "a") as f:
            f.write(f"{datetime.now()},{score}\n")
    except Exception as e:
        print("Error saving score:", e)

def main():
    print("Welcome to AI-Powered Quiz Generator!")
    qlist = generate_math_questions(5)
    score = conduct_quiz(qlist)
    save_score(score)

if __name__=="__main__":
    main()
