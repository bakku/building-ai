import random

def intermediate():
    prob = 0.80

    if random.random() < prob:
        print("dog")
    else:
        print("cat")

def advanced():
    rand = random.random()

    favourite = ""

    if rand < 0.8:
        favourite = "dogs"
    elif 0.8 <= rand < 0.9:
        favourite = "cats"
    else:
        favourite = "bats"

    print(f"I love {favourite}")

if __name__ == "__main__":
    print("INTERMEDIATE")
    print("------------------")
    intermediate()
    print("------------------")

    print()

    print("ADVANCED")
    print("------------------")
    advanced()
    print("------------------")
