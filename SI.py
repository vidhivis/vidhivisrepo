'''def si(p,r,t):
    cal = (p*r*t)/100
    return cal
principal = int(input("Enter the principal: "))
Rate = float(input("Enter the rate: "))
time = int(input("Enter the time: "))
c =si(principal,Rate,time)
print(f"Your simple interest is {c}")'''
from tkinter.font import names

from numpy.distutils.line_endings import dos2unix_dir

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

'''def get_cities():
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
    main()'''
'''file = open("example.txt","w")
file.write("Life is beautiful")
file.close()
file = open("example.txt","r")
content = file.read()
print(content)
file.close()'''
'''file = open("example.txt","r")
content = file.read()
print(content)
file.close()'''
'''file = open("example.txt","a")
file.write("\njourney is tough but destination is wonderful\nlife is lessons")
file.close()
with open("example.txt","r") as file:
    content = file.read()
    print(content)'''
'''try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"result: {result}")
except Exception as e:
    print(f"Error: {e}")'''
'''class Dog:
    pass
dog = Dog()
dog.name = "Tommy"
dog.birth_year = 2022
print(f"{dog.name} was born in {dog.birth_year}")'''
'''class Dog:
    def_init(self, name, birth_year):
    self.name = name
    self.birth_year = birth_year
dog = Dog("Bubbles", 2022)
print(f"{dog.name} was born in {dog.birth_year}.")'''

'''class Dog:
    def __init__(self, name, birth_year,sound="Woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound
    def bark(self,times):
        for i in range(times):
            print(self.sound)
        return

dog1 = Dog("Tommy", 2018)
dog2 = Dog("Boi", 2022, "yip yip")
dog1.bark(2)
dog2.bark(5)'''
'''class Dog:
    created = 0
    def __init__(self, name, birth_year,sound="Woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound
        Dog.created = Dog.created + 1

dog1 = Dog("Tommy", 2018)
dog2 = Dog("Boi", 2022, "yip yip")
dog3 = Dog("Zoravar", 2018)
dog4 = Dog("Bruno", 2022, "yip yip")
print(f"{Dog.created}")'''
# Assignment - 6
'''number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1'''
'''inch_to_cm = 2.54
while True:
    inches = float(input("Enter inches (negative value to stop): "))
    if inches < 0:
        print("Negative value entered. Program ending.")
        break
    centimeters = inches * inch_to_cm
    print(f"{inches} inches is equal to {centimeters:.2f} centimeters")'''
'''smallest = None
largest = None
while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break
    try:
        number = float(user_input)

        if smallest is None or number < smallest:
            smallest = number
        if largest is None or number > largest:
            largest = number

    except ValueError:
        print("Invalid input, please enter a valid number.")
        continue
if smallest is not None and largest is not None:
    print(f"The smallest number entered is: {smallest}")
    print(f"The largest number entered is: {largest}")
else:
    print("No numbers were entered.")'''
'''import random
correct_number = random.randint(1, 10)
while True:
    guess = input("Guess the number (between 1 and 10): ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please enter a valid number.")
        continue
    if guess < correct_number:
        print("Too low!")
    elif guess > correct_number:
        print("Too high!")
    else:
        print("Correct! You guessed the number.")
        break'''
'''correct_username = "python"
correct_password = "rules"
max_attempts = 5
attempts = 0
while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("Welcome!")
        break
    else:
        attempts += 1
        print(f"Incorrect login. Attempts left: {max_attempts - attempts}")
    if attempts == max_attempts:
        print("Access denied.")'''
'''import random
def approximate_pi(num_points):
    inside_circle = 0
    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 < 1:
            inside_circle += 1
    pi_approx = 4 * (inside_circle / num_points)
    return pi_approx
while True:
    try:
        num_points = int(input("Enter the number of random points to generate (e.g., 1000000): "))
        if num_points <= 0:
            print("Please enter a positive integer.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
pi_value = approximate_pi(num_points)
print(f"Approximation of π using {num_points} random points: {pi_value}")'''
# Assignment - 7
'''import random
def roll_dice():
    return random.randint(1, 6)
def main():
    roll = 0
    while roll != 6:
        roll = roll_dice()
        print(f"Rolled: {roll}")
if __name__ == "__main__":
    main()'''
'''import random
def roll_dice(sides):
    return random.randint(1, sides)
def main():
    while True:
        try:
            sides = int(input("Enter the number of sides on the dice: "))
            if sides < 2:
                print("Please enter a number greater than or equal to 2.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    roll = 0
    while roll != sides:
        roll = roll_dice(sides)
        print(f"Rolled: {roll}")
    print(f"Congratulations! You rolled the maximum value: {sides}")
if __name__ == "__main__":
    main()'''
'''def gallons_to_liters(gallons):
    liters = gallons * 3.78541
    return liters
def main():
    while True:
        try:
            gallons = float(input("Enter volume in gallons (negative value to quit): "))
            if gallons < 0:
                print("Negative value entered. Program ending.")
                break
            liters = gallons_to_liters(gallons)
            print(f"{gallons} gallons is equal to {liters:.2f} liters.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
if __name__ == "__main__":
    main()'''
'''def sum_of_list(numbers):
    return sum(numbers)
def main():
    numbers = [10, 20, 30, 40, 50]
    total_sum = sum_of_list(numbers)
    print(f"The sum of the numbers in the list is: {total_sum}")
if __name__ == "__main__":
    main()'''
'''def remove_odd_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]
def main():
    original_list = [10, 21, 32, 43, 54, 65, 76, 87, 98]
    even_list = remove_odd_numbers(original_list)
    print("Original list:", original_list)
    print("List after removing odd numbers:", even_list)
if __name__ == "__main__":
    main()'''
import math
def calculate_unit_price(diameter, price):
    radius = diameter / 2  # Calculate the radius
    area = math.pi * (radius ** 2)
    area_square_meters = area / 10000
    unit_price = price / area_square_meters
    return unit_price
def main():
    print("Enter details for Pizza 1:")
    diameter1 = float(input("Diameter (cm): "))
    price1 = float(input("Price (€): "))
    print("Enter details for Pizza 2:")
    diameter2 = float(input("Diameter (cm): "))
    price2 = float(input("Price (€): "))
    unit_price1 = calculate_unit_price(diameter1, price1)
    unit_price2 = calculate_unit_price(diameter2, price2)
    print(f"\nUnit price for Pizza 1: {unit_price1:.2f} €/m²")
    print(f"Unit price for Pizza 2: {unit_price2:.2f} €/m²")
    if unit_price1 < unit_price2:
        print("Pizza 1 provides better value for money.")
    elif unit_price2 < unit_price1:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas provide the same value for money.")
if __name__ == "__main__":
    main()