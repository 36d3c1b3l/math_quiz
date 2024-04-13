import random
import time

OPERATORS = ["+", "-", "*"]
MIN = 3
MAX = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN, MAX)
    right = random.randint(MIN, MAX)
    operator = random.choice(OPERATORS)

    expr = f"{left} {operator} {right}"
    answer = eval(expr)
    return expr, answer


def main():
    score = 0
    input("Press enter to start ")
    print("-----------------------")
    start_time = time.time()

    for i in range(TOTAL_PROBLEMS):
        expr, answer = generate_problem()
        while True:
            guess = input(f"Problem #{i + 1}\n{expr} = ")
            if str(answer) == guess:
                score += 1
                print("Correct")
                break
            else:
                print("Incorrect")

    end_time = time.time()
    total_time = end_time - start_time
    
    print("-----------------------")
    print(f"Nicely done! You got it in {total_time} seconds")


if __name__ == "__main__":
    main()