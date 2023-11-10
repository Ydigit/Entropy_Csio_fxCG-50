import math

def calculate_entropy(probabilities):
    return -sum(p * math.log(p, 2) for p in probabilities if p > 0)

def menu():
    print("Menu:")
    print("1. Insert probabilities")
    print("2. Calculate entropy")
    print("3. Exit")

events = []
probabilities = []

while True:
    menu()
    choice = input("Choose: ")

    if choice == "1":
        num_events = int(input("Enter number of events: "))
        events = []
        probabilities = []
        for i in range(num_events):
            event = input("Event name {}: ".format(i + 1))
            prob = float(input("Probability for event {}: ".format(event)))
            events.append(event)
            probabilities.append(prob)
    elif choice == "2":
        if not probabilities:
            print("Insert probabilities.")
        else:
            entropy = calculate_entropy(probabilities)
            print("\nEvents and probabilities:")
            for event, prob in zip(events, probabilities):
                print("{}: {:.2f}".format(event, prob))
            print("Entropy: {:.2f}".format(entropy))
    elif choice == "3":
        break
    else:
        print("Invalid option.")
