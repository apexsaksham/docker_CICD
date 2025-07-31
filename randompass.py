import random
import string






   

qa_dict = {
    "What is the capital of India?": "New Delhi",
    "Who developed Python programming language?": "Guido van Rossum",
    "What does CPU stand for?": "Central Processing Unit",
    "What is the largest planet in our solar system?": "Jupiter",
    "What is the chemical symbol for water?": "H2O",
    "What year did India gain independence?": "1947",
    "What is the national animal of India?": "Tiger",
    "Which language is primarily used for web development?": "JavaScript",
    "What is the square root of 144?": "12",
    "Who wrote the Harry Potter series?": "J.K. Rowling"
}


def python_game():
        question_list = list(qa_dict.keys())
        total_question = 5
        score = 0

        selected_questions = random.sample(question_list, total_question)
        for idx,  questions in enumerate(selected_questions):
            print(f"{idx + 1}. {questions}")
            user_input = input("your answer: ").lower().strip()
            correct_answer = qa_dict[questions]
            if user_input == correct_answer.lower():
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Incorrect! Correct answer is: {correct_answer}\n")

        print(f"🎯 Your final score: {score}/{total_question}")
       
          

def generate_pass():
        length = int(input("Enter the desired length : "))
        include_uppercase = input("include uppercase letter? (yes/no): ").lower()
        include_special = input("include special letter? (yes/no): ").lower()
        include_digits = input("include digits letter? (yes/no): ").lower()

        if length < 4:
            print("password atlest must be 4 characters")
            return
        
        
        lower = string.ascii_lowercase
        uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""
        special = string.punctuation if include_uppercase == "yes" else ""
        digits = string.digits if include_digits == "yes" else ""
        all_characters = lower + uppercase + special + digits
        

        if not all_characters:
            print("❌ You must select at least one character type.")
            return
        
        password = ''.join(random.choices(all_characters, k=length))
        print("✅ Generated password:", password)
    

    
while True:
    print("🔽 Choose an option:")
    print("1. Python Quiz Game")
    print("2. Password Generator")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice (1/2/3): "))
    except ValueError:
        print("⚠️ Invalid input. Please enter a number.\n")
        continue

    if choice == 1:
        python_game()
    elif choice == 2:
        generate_pass()
    elif choice == 3:
        print("👋 Exiting the program. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice. Please select 1, 2, or 3.\n")