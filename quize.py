questions = [
    {
        "prompt": "What does py extension in file stand for",
        "options": ["A. Pi", "B. Python", "C. Pie", "D. Pyrho"],
        "answer": "B",
    },
    {
        "prompt": "To display any data command used in Python is",
        "options": ["A. print", "B. Console.log", "C. printr", "D. println!"],
        "answer": "A",
    },
    {
        "prompt": "Python was created in year",
        "options": ["A. 1990", "B. 1993", "C. 1991", "D. 1994"],
        "answer": "C",
    },
]


def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)

        answer = input("Enter your answer ").upper()
        if answer == question["answer"]:
            score += 1

    print(f"you got {score} out of {len(questions)} questions correct.")


run_quiz(questions)
