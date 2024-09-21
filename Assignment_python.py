'''print("Hello Vidhi")

name = input("Name? ")
print(f"Hello, {name}! Very Nice to meet you!")

import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print(f"The area of the circle with radius {radius} is {area:.2f}")

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
perimeter = 2 * (length + width)
area = length * width
print(f"The perimeter of the rectangle is {perimeter:.2f}")
print(f"The area of the rectangle is {area:.2f}")

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

sum_of_numbers = num1 + num2 + num3
product_of_numbers = num1 * num2 * num3
average_of_numbers = sum_of_numbers / 3

print(f"The sum of the numbers is: {sum_of_numbers}")
print(f"The product of the numbers is: {product_of_numbers}")
print(f"The average of the numbers is: {average_of_numbers:.2f}")

LOT_TO_GRAMS = 13.3
POUND_TO_LOTS = 32
TALENT_TO_POUNDS = 20

talents = int(input("Enter the number of talents: "))
pounds = int(input("Enter the number of pounds: "))
lots = int(input("Enter the number of lots: "))

total_lots = (talents * TALENT_TO_POUNDS * POUND_TO_LOTS) + (pounds * POUND_TO_LOTS) + lots
total_grams = total_lots * LOT_TO_GRAMS

kilograms = int(total_grams // 1000)
grams = total_grams % 1000
print(f"The total weight is {kilograms} kilograms and {grams:.2f} grams.")

import random
code_3_digit = [random.randint(0, 9) for _ in range(3)]
code_4_digit = [random.randint(1, 6) for _ in range(4)]
print(f"3-digit lock code: {''.join(map(str, code_3_digit))}")
print(f"4-digit lock code: {''.join(map(str, code_4_digit))}")

SIZE_LIMIT = 42
zander_length = float(input("Enter the length of the zander in centimeters: "))
if zander_length < SIZE_LIMIT:
    difference = SIZE_LIMIT - zander_length
    print(f"The zander is too small and must be released back into the lake. It is {difference:.2f} cm below the size limit.")
else:
    print("The zander meets the size limit. You can keep it!")

cabin_class = input("Enter the cabin class (LUX, A, B, C): ").upper()
if cabin_class == "LUX":
    print("LUX: upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("A: above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("B: windowless cabin above the car deck.")
elif cabin_class == "C":
    print("C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

gender = input("Enter your biological gender (male/female): ").lower()
hemoglobin_value = float(input("Enter your hemoglobin value (g/l): "))

if gender == "female":
    if hemoglobin_value < 117:
        print("Your hemoglobin level is low.")
    elif 117 <= hemoglobin_value <= 155:
        print("Your hemoglobin level is normal.")
    else:
        print("Your hemoglobin level is high.")
elif gender == "male":
    if hemoglobin_value < 134:
        print("Your hemoglobin level is low.")
    elif 134 <= hemoglobin_value <= 167:
        print("Your hemoglobin level is normal.")
    else:
        print("Your hemoglobin level is high.")
else:
    print("Invalid gender entered. Please enter either 'male' or 'female'.")

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")'''


'''days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Friday", "Saturday", "Sunday")
day_number = int(input("Enter a day number 1-7: "))
print(days_of_the_week[day_number])
fruits = "apple", "banana", "cherry", "blueberry"
print(type(fruits))
(first, second, third,fourth) = fruits
print(first)
print(second)
print(third)
print(fourth)'''
games = {"monopoly", "chess", "cluedo"}
print(games)
games.add("dominion")
games.remove("chess")
print(games)
for g in games:
    print(g)
import random

# Function to roll the dice and calculate the sum
def roll_dice(number_of_dice):
    total_sum = 0
    for _ in range(number_of_dice):
        roll = random.randint(1, 6)  # Simulate a die roll (1 to 6)
        total_sum += roll
        print(f"Die roll: {roll}")  # Print the result of each roll
    return total_sum

# Main function
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

# Run the main function
if __name__ == "__main__":
    main()