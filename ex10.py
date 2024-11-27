import numpy as np


def flip(n):
    odds = 1.0
    r = 2

    for i in range(n):
        odds *= r

    print(odds)


def intermediate():
    flip(1)


def roll(loaded):
    p_normal = [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6]
    p_loaded = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]

    if loaded:
        print("rolling a loaded die")
        p = p_loaded
    else:
        print("rolling a normal die")
        p = p_normal

    sequence = np.random.choice(6, size=10, p=p) + 1
    for roll in sequence:
        print("rolled %d" % roll)

    return sequence


def bayes(sequence):
    odds = 1.0

    likelyhood_6 = 0.5 / (1 / 6)
    likelyhood_else = 0.1 / (1 / 6)

    for roll in sequence:
        if roll == 6:
            odds *= likelyhood_6
        else:
            odds *= likelyhood_else

    if odds > 1:
        return True
    else:
        return False


def advanced():
    sequence = roll(True)

    if bayes(sequence):
        print("I think loaded")
    else:
        print("I think normal")


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
