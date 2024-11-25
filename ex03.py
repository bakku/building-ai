import math
import random

def climb_intermediate(x, h):
    # keep climbing until we've found a summit
    summit = False

    # edit here
    while not summit:
        summit = True         # stop unless there's a way up

        if h[x + 1] > h[x]:
            x = x + 1         # right is higher, go there
            summit = False    # and keep going

        if h[x - 1] > h[x]:
            x = x - 1
            summit = False

    return x

def intermediate():
    # generate random mountains                                                                               	 
    w = [random.random()/3, random.random()/3, random.random()/3]
    h = [1.+math.sin(1+x/6.)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]
    h[0] = 0.0; h[99] = 0.0

    # start at a random place
    x0 = random.randint(1, 98)
    x = climb_intermediate(x0, h)

    print("Venla started at %d and got to %d" % (x0, x))
    return x0, x

def climb_advanced(x, h):
    # keep climbing until we've found a summit
    summit = False

    # edit here
    while not summit:
        summit = True         # stop unless there's a way up

        bestmove = x

        for i in list(range(-5, 6)):
            if h[min(99, x + i)] > h[bestmove]:
                bestmove = x + i

        if bestmove != x:
            x = bestmove
            summit = False

    return x

def advanced():
    w = [.05, random.random()/3, random.random()/3]
    h = [1.+math.sin(1+x/.6)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]

    # start at a random place
    x0 = random.randint(1, 98)
    x = climb_advanced(x0, h)


if __name__ == "__main__":
    print("INTERMEDIATE")
    print("------------------")
    intermediate()
    print("------------------")

    # print()

    # print("ADVANCED")
    # print("------------------")
    # advanced()
    # print("------------------")
