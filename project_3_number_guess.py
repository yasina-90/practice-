import random
import time

def generate_question():
    operands = ['+', '-', '*']
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    operan_choiced = random.choice(operands)
    question = (f"what is the answer of  {num1} {operan_choiced} {num2} = ?")
    if operan_choiced == '+':
        answer = num1 + num2
    elif operan_choiced == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return question, answer


def play_game():
    questions = []
    num_answers = 0
    score = 0
    num_questions = 2
    time_limit = 5
    while num_answers < num_questions:
        question, answer = generate_question()
        questions.append((question, answer))

        start_time = time.time()########## time start
        user_guess = int(input(question + " = "))
        end_time = time.time()########## time end

        time_diff = end_time - start_time

        if time_diff < time_limit:
            if user_guess == answer:
                num_answers += 1
                score += 1
                print(f"Correct!, score is: {score}")
            else:
                print("Incorrect!")
                num_answers += 1
        else:
            print("time out! try again")
            continue
    print(f"You got {score} out of {len(questions)} questions correct")
    if (score >= num_questions):
        print("you won!")
    else:
        print("you lost!, try again!")


play_game()