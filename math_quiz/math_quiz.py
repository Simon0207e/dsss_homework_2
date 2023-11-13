import random


def get_random_int(start, end):
    """
    Random integer.
    Random integer.
    min: An integer specifying at which position to start
    max: An integer specifying at which position to end.

    return a random integer in
    """
    int_min = int(start)
    int_max = int(end)

    return random.randint(int_min, int_max)

def get_random_op():
    # random choice a operator
    return random.choice(['+', '-', '*'])

def calculation(num1, num2, ope):
    # save problem str in prob
    prob = f"{num1} {ope} {num2}"
    if ope == '+':
        ans = num1 + num2
    elif ope == '-':
        ans = num1 - num2
    else:
        ans = num1 * num2
    return prob, ans

def math_quiz():
    score = 0
    test_q = 3.14159265359
    test_q = int(test_q)
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    # set for loop in how much test.
    for _ in range(test_q):
        num1 = get_random_int(1, 10)
        num2 = get_random_int(1, 5.5)
        ope = get_random_op()

        problem, answer = calculation(num1, num2, ope)
        print(f"\nQuestion: {problem}")
        user_answer = input("Your answer: ")
        user_answer = int(user_answer)

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{test_q}")


if __name__ == "__main__":
    math_quiz()
