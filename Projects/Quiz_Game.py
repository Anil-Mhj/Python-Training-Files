def quiz_game():
    questions = [
        "What is the capital of France?",
        "Which planet is known as the Red Planet?",
        "What is 5 + 7?",
        "Who wrote 'To Kill a Mockingbird'?",
        "What is the chemical symbol for gold?",
        "What is the largest ocean on Earth?",
        "Who painted the Mona Lisa?",
        "What is the square root of 64?",
        "Which is the longest river in the world?",
        "What is the national animal of China?",
    ]

    choices = [
        ["A) Paris", "B) London", "C) Rome", "D) Berlin"],
        ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        ["A) 10", "B) 11", "C) 12", "D) 13"],
        ["A) J.K. Rowling", "B) Harper Lee", "C) Mark Twain", "D) Jane Austen"],
        ["A) Au", "B) Ag", "C) Pb", "D) Fe"],
        ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
        [
            "A) Vincent van Gogh",
            "B) Pablo Picasso",
            "C) Leonardo da Vinci",
            "D) Claude Monet",
        ],
        ["A) 6", "B) 7", "C) 8", "D) 9"],
        [
            "A) Amazon River",
            "B) Nile River",
            "C) Yangtze River",
            "D) Mississippi River",
        ],
        ["A) Tiger", "B) Panda", "C) Elephant", "D) Kangaroo"],
    ]

    answers = ["A", "B", "C", "B", "A", "D", "C", "C", "B", "B"]

    score = 0

    for i in range(len(questions)):
        print(f"\{i + 1}: {questions[i]}")
        for choice in choices[i]:
            print(choice)

        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

        if user_answer == answers[i]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {answers[i]}.")

    print(f"\nGame Over! Your final score is {score}/{len(questions)}")


def main():
    print("\nWelcome to the Quiz Game!")
    print("1) Start Game")
    print("2) Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        quiz_game()
    elif choice == "2":
        print("Goodbye!")
    else:
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
