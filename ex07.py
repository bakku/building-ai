import numpy as np

def count11(seq):
    occurrences = 0

    for i in range(0, len(seq) - 1):
        if seq[i] == 1 and seq[i + 1] == 1:
            occurrences += 1

    return occurrences

def intermediate():
    print(count11([0, 0, 1, 1, 1, 0])) # this should print 2

def generate(p1):
    return np.random.choice([0,1], p=[1-p1, p1], size=10000)

def count(seq):
    occurrences = 0

    for i in range(0, len(seq) - 4):
        occurrence = True

        for j in range(0, 5):
            if seq[i + j] != 1:
                occurrence = False
                break

        if occurrence:
            occurrences += 1

    return occurrences
            

def advanced_runner(p1):
    return count(generate(p1))

def advanced():
    print(advanced_runner(2/3))

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
