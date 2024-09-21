'''def si(p,r,t):
    cal = (p*r*t)/100
    return cal
principal = int(input("Enter the principal: "))
Rate = float(input("Enter the rate: "))
time = int(input("Enter the time: "))
c =si(principal,Rate,time)
print(f"Your simple interest is {c}")'''
'''import random

def roll_dice(number_of_dice):
    total_sum = 0
    for _ in range(number_of_dice):
        roll = random.randint(1, 6)
        total_sum += roll
        print(f"Die roll: {roll}")
    return total_sum

def main():
    try:
        number_of_dice = int(input("How many dice do you want to roll? "))
        if number_of_dice <= 0:
            print("Please enter a positive number.")
            return

        total_sum = roll_dice(number_of_dice)
        print(f"\nThe sum of all dice rolls is: {total_sum}")

    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()'''


'''def find_top_five_numbers():
    numbers = []

    while True:
        user_input = input("Enter a number (or press Enter to stop): ")


        if user_input == "":
            break

        try:

            number = float(user_input)
            numbers.append(number)
        except ValueError:

            print("Please enter a valid number.")


    numbers.sort(reverse=True)

    top_five = numbers[:5]

    print("\nThe five greatest numbers are:", top_five)

def main():
    find_top_five_numbers()

if __name__ == "__main__":
    main()'''

'''def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    try:
        number = int(input("Enter an integer: "))

        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")

    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()'''

def get_cities():
    cities = []

    for i in range(5):
        city = input(f"Enter the name of city {i + 1}: ")
        cities.append(city)

    return cities

def print_cities(cities):
    print("\nThe cities you entered are:")

    for city in cities:
        print(city)

def main():
    cities = get_cities()
    print_cities(cities)

if __name__ == "__main__":
    main()