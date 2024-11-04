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
'''import math
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
    main()'''
# Assignment - 8
'''class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def __str__(self):
        return (f"Registration Number: {self.registration_number}\n"
                f"Maximum Speed: {self.max_speed} km/h\n"
                f"Current Speed: {self.current_speed} km/h\n"
                f"Travelled Distance: {self.travelled_distance} km")

def main():
    new_car = Car("ABC-123", 142)
    print(new_car)

if __name__ == "__main__":
    main()


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def __str__(self):
        return (f"Registration Number: {self.registration_number}\n"
                f"Maximum Speed: {self.max_speed} km/h\n"
                f"Current Speed: {self.current_speed} km/h\n"
                f"Travelled Distance: {self.travelled_distance} km")

def main():
    new_car = Car("ABC-123", 142)
    new_car.accelerate(30)
    new_car.accelerate(70)
    new_car.accelerate(50)
    print(f"Current Speed after acceleration: {new_car.current_speed} km/h")
    new_car.accelerate(-200)
    print(f"Final Speed after emergency brake: {new_car.current_speed} km/h")
if __name__ == "__main__":
    main()'''


'''class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

    def __str__(self):
        return (f"Registration Number: {self.registration_number}\n"
                f"Maximum Speed: {self.max_speed} km/h\n"
                f"Current Speed: {self.current_speed} km/h\n"
                f"Travelled Distance: {self.travelled_distance} km")
def main():
    new_car = Car("ABC-123", 142)
    new_car.accelerate(30)
    new_car.accelerate(70)
    new_car.accelerate(50)
    print(f"Current Speed after acceleration: {new_car.current_speed} km/h")
    new_car.accelerate(-200)
    print(f"Final Speed after emergency brake: {new_car.current_speed} km/h")
    new_car.accelerate(60)
    new_car.drive(1.5)
    print(f"Travelled Distance after driving: {new_car.travelled_distance} km")
if __name__ == "__main__":
    main()'''
'''import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def accelerate(self):
        speed_change = random.randint(-10, 15)
        self.current_speed += speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self):
        self.distance_traveled += self.current_speed

def print_race_status(cars):
    print(f"{'Car':<10}{'Max Speed (km/h)':<20}{'Current Speed (km/h)':<20}{'Distance Traveled (km)':<20}")
    print("=" * 70)
    for car in cars:
        print(f"{car.registration_number:<10}{car.max_speed:<20}{car.current_speed:<20}{car.distance_traveled:<20.2f}")
    print("\n")

def main():
    cars = []
    for i in range(1, 11):
        reg_num = f"ABC-{i}"
        max_speed = random.randint(100, 200)
        cars.append(Car(reg_num, max_speed))
    race_over = False
    hour = 0
    while not race_over:
        hour += 1
        print(f"Hour: {hour}")
        for car in cars:
            car.accelerate()
            car.drive()
            if car.distance_traveled >= 10000:
                race_over = True
        print_race_status(cars)
    print("Race Over!\nFinal Results:")
    print_race_status(cars)

if __name__ == "__main__":
    main()'''

'''class InsufficientFundsException(Exception):
    """Custom exception for insufficient funds."""
    pass

class NegativeAmountException(Exception):
    """Custom exception for negative amount."""
    pass

def get_float_input(prompt):
    """Function to get numeric input and handle invalid input."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def main():
    try:
        balance = get_float_input("Enter your account balance: ")
        if balance < 0:
            raise NegativeAmountException("Account balance cannot be negative!")
        withdrawal_amount = get_float_input("Enter the amount to withdraw: ")
        if withdrawal_amount < 0:
            raise NegativeAmountException("Withdrawal amount cannot be negative!")
        if withdrawal_amount > balance:
            raise InsufficientFundsException("Withdrawal amount exceeds account balance!")
        balance -= withdrawal_amount
        print(f"Withdrawal successful! Your new balance is: {balance:.2f}")

    except NegativeAmountException as e:
        print(f"Error: {e}")
    except InsufficientFundsException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()'''


'''def write_notes(filename):
    """Writes new notes to the file, overwriting any existing content."""
    with open(filename, 'w') as file:
        print("Enter your notes (type 'STOP' to finish):")
        while True:
            note = input()
            if note.upper() == 'STOP':
                break
            file.write(note + '\n')
        print("Notes saved successfully!\n")


def read_notes(filename):
    """Reads and displays the existing notes from the file."""
    try:
        with open(filename, 'r') as file:
            notes = file.read()
            if notes:
                print("Here are your notes:\n")
                print(notes)
            else:
                print("No notes found in the file.\n")
    except FileNotFoundError:
        print("No notes file found. Please write new notes first.\n")


def append_notes(filename):
    """Appends additional notes to the existing file."""
    try:
        with open(filename, 'a') as file:
            print("Enter additional notes (type 'STOP' to finish):")
            while True:
                note = input()
                if note.upper() == 'STOP':
                    break
                file.write(note + '\n')
            print("Notes appended successfully!\n")
    except FileNotFoundError:
        print("No notes file found. Please write new notes first.\n")


def main():
    filename = "notes.txt"

    while True:
        print("Menu:")
        print("1. Write new notes (this will overwrite any existing notes)")
        print("2. Read existing notes")
        print("3. Append additional notes")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            write_notes(filename)
        elif choice == '2':
            read_notes(filename)
        elif choice == '3':
            append_notes(filename)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()'''
# Assignment - 1 - AI with python
# Question - 1
'''import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 200)

y1 = 2 * x + 1
y2 = 2 * x + 2
y3 = 2 * x + 3

plt.figure(figsize=(10, 6))

plt.plot(x, y1, color="black", linestyle="solid", linewidth=1.5, label="y = 2x + 1")
plt.plot(x, y2, color="red", linestyle="dashed", linewidth=1.5, label="y = 2x + 2")
plt.plot(x, y3, color="green", linestyle="dotted", linewidth=1.5, label="y = 2x + 3")

plt.title("Graphs of the Lines y=2x+1, y=2x+2, y=2x+3")
plt.xlabel("x")
plt.ylabel("y")

plt.legend()

plt.grid(True)
plt.show()'''
# Question - 2
'''import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([-0.57, -2.57, -4.80, -7.36, -8.78, -10.52, -12.85, -14.69, -16.78])


plt.figure(figsize=(8, 5))
plt.scatter(x, y, marker='+', color="black")

plt.title("Scatter Plot of Points (x, y)")
plt.xlabel("x")
plt.ylabel("y")

plt.grid(True)
plt.show()'''
# question - 3
'''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("weight-height.csv")

height_inches = data['Height']
weight_pounds = data['Weight']

height_cm = height_inches * 2.54

weight_kg = weight_pounds * 0.453592

mean_height_cm = np.mean(height_cm)
mean_weight_kg = np.mean(weight_kg)

print(f"Mean Height (cm): {mean_height_cm}")
print(f"Mean Weight (kg): {mean_weight_kg}")

plt.figure(figsize=(8, 5))
plt.hist(height_cm, bins=20, color="skyblue", edgecolor="black")
plt.title("Histogram of Heights (in cm)")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()'''
'''# question - 4
import numpy as np

A = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])

A_inv = np.linalg.inv(A)

AA_inv = np.dot(A, A_inv)
A_invA = np.dot(A_inv, A)

print("A * A_inv:\n", AA_inv)
print("A_inv * A:\n", A_invA)'''
# Assignment - 3
# Question - 1
'''import numpy as np
import matplotlib.pyplot as plt

n_values = [500, 1000, 2000, 5000, 10000, 15000, 20000, 50000, 100000]

for n in n_values:
    dice1 = np.random.randint(1, 7, size=n)  # Roll dice 1
    dice2 = np.random.randint(1, 7, size=n)  # Roll dice 2
    s = dice1 + dice2

    h, h2 = np.histogram(s, range(2, 14))  # Histogram of sums

    plt.figure(figsize=(8, 5))
    plt.bar(h2[:-1], h / n)
    plt.title(f"Histogram of Dice Sums for n = {n}")
    plt.xlabel("Sum of two dice")
    plt.ylabel("Relative Frequency")
    plt.xticks(range(2, 13))
    plt.show()'''
# Question - 2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv('weight-height.csv')

print(data.head())

plt.figure(figsize=(10, 6))
plt.scatter(data['Height'], data['Weight'], alpha=0.5)
plt.title('Scatter Plot of Height vs. Weight')
plt.xlabel('Height (inches)')
plt.ylabel('Weight (pounds)')
plt.grid()
plt.show()

X = data[['Height']]
y = data['Weight']

model = LinearRegression()
model.fit(X, y)

plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.5, label='Data points')
plt.plot(X, model.predict(X), color='red', label='Regression line')
plt.title('Height vs. Weight with Regression Line')
plt.xlabel('Height (inches)')
plt.ylabel('Weight (pounds)')
plt.legend()
plt.grid()
plt.show()

predictions = model.predict(X)
rmse = np.sqrt(mean_squared_error(y, predictions))
r2 = r2_score(y, predictions)

print(f'RMSE: {rmse}')
print(f'R²: {r2}')

if r2 < 0.5:
    quality = "Poor fit"
elif 0.5 <= r2 < 0.8:
    quality = "Moderate fit"
else:
    quality = "Good fit"

print(f'Quality of the regression: {quality}')






