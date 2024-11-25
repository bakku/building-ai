portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

def intermediate():
    port1 = 0

    for port2 in range(1, 5):
        for port3 in range(1, 5):
            for port4 in range(1, 5):
                for port5 in range(1, 5):
                    route = [port1, port2, port3, port4, port5]

                    # Modify this if statement to check if the route is valid
                    if (sorted(route) == list(range(0, 5))):
                        # do not modify this print statement
                        print(' '.join([portnames[i] for i in route]))

def permutations(route, ports):
    if (len(ports) == 0):
        # Print the port names in route when the recursion terminates
        print(' '.join([portnames[i] for i in route]))
        return

    for port in ports:
        permutations(route + [port], [x for x in ports if x != port])

def advanced():
    permutations([0], list(range(1, len(portnames))))

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
