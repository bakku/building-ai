import math

def intermediate():
    s_old = 205
    s_new = 196

    target_prob = 0.5

    # prob = exp(-(s_old - s_new) / T)
    # -> prob = 1 / exp((s_old - s_new) / T)
    # -> 1 / prob = exp((s_old - s_new) / T)
    # -> ln(1 / prob) = (s_old - s_new) / T
    # -> T = (s_old - s_new) / ln(1 / prob)
    t = (s_old - s_new) / math.log(1 / target_prob)
    
    print(t)

def accept_prob(S_old, S_new, T):
    # this is the acceptance "probability" in the greedy hill-climbing method
    # where new solutions are accepted if and only if they are better
    # than the old one.
    # change it to be the acceptance probability in simulated annealing
    return math.exp(-(S_old - S_new) / T)

def advanced():
    prob = accept_prob(150, 140, 13)

    print("p = %f" % prob)
    
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
