import random
quiz_questions = {
    "How many seconds in a day?\n3600\n86400\n216000\n36000": "86400",
    "The largest four digit number is?\n1000\n9000\n9999\n1111": "9999",
    "Anjali is 19 years old and her mother is 37,how many years ago was Anjali's mother age is 4 times to her age? ": "13",
    "In a group total number of ducks and cows is 12 and total count of their legs is 34,then how many ducks in that group? ": "7",
    "I am an odd number(in words)if a letter is deleted I will become as even,then who am i?\nfive\nseven\nnine\none": "seven"
}

def main():
    print("Welcome to the Quiz Game!")
    
    score = 0
    shuffled_questions=list(quiz_questions.items())
    random.shuffle(shuffled_questions)
    for question, correct_answer in shuffled_questions:
        print(question)
        user_answer = input("Type Your answer: ")
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")
    
    print(f"Quiz completed! Your final score is: {score}/{len(quiz_questions)}")
    if score == len(quiz_questions):
        print("Congratulations! You got all the answers correct.")
    else:
        print("Better luck next time!")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        main()
    else:
        print("Thank you for playing the Quiz Game!")

main()
