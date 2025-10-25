questions = ("What function is used to display text on the screen in Python ?",
             "How do you write a single-line comment in Python?",
             "Which of the following is a correct variable name in Python?",
             "What is the correct way to get input from a user in Python?",
             "What will print(2 + 3 * 4) output?",
             "What type of data is produced by this code: name = ""John""?",
             "Which keyword is used to create a function in Python?",
             "Which loop is best for repeating a block of code a known number of times?",
             "What does this code do?: for i in range(3): print(i)",
             "What is the output of this code?: Print(""Python"")")

options = (("A. echo()","B. printf()","C. print()","D. display"),
                ("A. //comment","B. #comment","C. /*comment*/","D. <!--comment-->"),
                ("A. 2name","B. my-name","C. my_name","D. my name"),
                ("A. get()","B. input()","C. scan()","D. read()"),
                ("A. 20","B. 14","C. 24","D. 19"),
                ("A. Integer","B. String","C. Float","D. Boolean"),
                ("A. define","B. func","C. def","D. function"),
                ("A. while loop","B. for loop","C. repeat loop","D. do loop"),
                ("A. print 0 1 2","B. 1 2 3","C. 1 2 3 4","D. 0 1 2 3"),
                ("A. error","B. P","C. yes","D. Python"))

answers = ("C","B","C","B","B","B","C","B","A","A")

guesses = []
question_num = 0
score = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    try:
        if guess == answers[question_num]:
            score += 1
            print("----------")
            print("CORRECT !")
            print("----------")
        else:
            print("----------")
            print("WRONG !")
            print("----------")
            print(f"Correct answer is: {answers[question_num]}")
        question_num += 1
        print()
    except IndexError:
        print("No more questions available.")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        break
print("-------------------------RESULTS-----------------------")
print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()
print("-------------------------------------------------------")
perc = int(score / len(questions) * 100)
print(f"Your score is: {score} / {len(questions)}")
print(f"Your got: {perc}%")