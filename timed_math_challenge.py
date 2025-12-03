import random
import time


OPERATORS = ["+", "-", "*"]
low = 1
high = 10


def generate_problem():
    left = random.randint(low, high)
    right = random.randint(low, high)
    operator = random.choice(OPERATORS)

    expre = f"{str(left)} {operator} {str(right)}"
    ans = eval(expre)
    return expre, ans


input("Press enter to start.")
print("---------------------")
starting_time = time.time()

for i in range(10):
    expre, ans = generate_problem()

    while True:
        guess = str(input(f"Problem #{str(i + 1)}: {expre} = "))
        if guess == str(ans):
            break

ending_time = time.time()
total_time = round(ending_time - starting_time, 2)

print("---------------------")
print(f"Nice work! You finished in {total_time} seconds.")
