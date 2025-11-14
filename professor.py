import random


def main():
    level = get_level()  # First get the level from user
    score = 0

    # Generate 10 math problems
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        error_count = 0

        # Give up to 3 attempts per problem
        while error_count < 3:
            try:
                user_answer = input(f"{x} + {y} = ")
                if user_answer.isdecimal():
                    user_answer = int(user_answer)
                    if user_answer == correct_answer:
                        score += 1
                        break  # Correct answer, move to next problem
                    else:
                        print("EEE")
                        error_count += 1
                else:
                    print("EEE")
                    error_count += 1
            except ValueError:
                print("EEE")
                error_count += 1

        # After 3 wrong attempts, show the correct answer
        if error_count == 3:
            print(f"{x} + {y} = {correct_answer}")

    print(f"Score: {score}")


def get_level():
    #prompt the user until respond with valid level (1, 2 or 3).
    while True:
        try:
            level = int(input('Level: '))
            if level in [1, 2, 3]:
                return(level)
        except ValueError:
            pass

def generate_integer(level):
    #generate integer according to the difficulty: 1, 2, or 3 digits.
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    #else: raise ValueError -- NO illogical


if __name__ == "__main__":
    main()
