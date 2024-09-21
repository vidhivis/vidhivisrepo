# Function to determine the season based on the month number
def get_season(month):
    # Tuple holding the seasons in the order of their corresponding months
    seasons = ("Winter", "Winter", "Spring", "Spring", "Spring", "Summer",
               "Summer", "Summer", "Autumn", "Autumn", "Autumn", "Winter")

    # Check if the month is within the valid range
    if 1 <= month <= 12:
        # Subtract 1 to match the index (since list/tuple indices start from 0)
        return seasons[month - 1]
    else:
        return "Invalid month number"


# Main function to get user input and print the corresponding season
def main():
    try:
        # Ask for the month number
        month = int(input("Enter a month number (1-12): "))

        # Get the season and print the result
        season = get_season(month)
        print(f"The corresponding season is: {season}")

    except ValueError:
        print("Please enter a valid integer for the month.")


# Run the main function
if __name__ == "__main__":
    main()
