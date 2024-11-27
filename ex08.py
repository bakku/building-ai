import numpy as np

def intermediate():
    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    populations = [5615000, 5439000, 324000, 5080000, 9609000]
    fishers = [1891, 2652, 3800, 11611, 1757]

    total_fishers = sum(fishers)
    total_population = sum(populations)

    probabilities = [(f / total_fishers) * 100 for f in fishers]

    for country, probability in zip(countries, probabilities):
        print("%s %.2f%%" % (country, probability))

def guess(winner_gender):
    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    populations = [5615000, 5439000, 324000, 5080000, 9609000]
    male_fishers = [1822, 2575, 3400, 11291, 1731]
    female_fishers = [69, 77, 400, 320, 26] 

    if winner_gender == 'female':
        fishers = female_fishers
    else:
        fishers = male_fishers

    total_fishers = sum(fishers)

    probabilities = [(f / total_fishers) * 100 for f in fishers]

    idx = np.argmax(probabilities)

    return (countries[idx], probabilities[idx])  

def advanced():
    country, fraction = guess("male")
    print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (country, fraction))
    country, fraction = guess("female")
    print("if the winner is female, my guess is she's from %s; probability %.2f%%" % (country, fraction))

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
