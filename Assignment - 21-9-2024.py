def get_season(month):
    seasons = ("Winter", "Winter", "Spring", "Spring", "Spring", "Summer",
               "Summer", "Summer", "Autumn", "Autumn", "Autumn", "Winter")

    if 1 <= month <= 12:

        return seasons[month - 1]
    else:
        return "Invalid month number"

def main():
    try:
        month = int(input("Enter a month number (1-12): "))

        season = get_season(month)
        print(f"The corresponding season is: {season}")

    except ValueError:
        print("Please enter a valid integer for the month.")

if __name__ == "__main__":
    main()


def collect_names():
    names_set = set()
    while True:
        name = input("Enter a name (or press Enter to stop): ")

        if name == "":
            break

        if name in names_set:
            print("Existing name")
        else:
            print("New name")
            names_set.add(name)

    return names_set

def print_names(names_set):
    print("\nThe names you entered are:")
    for name in names_set:
        print(name)

def main():
    names_set = collect_names()
    print_names(names_set)

if __name__ == "__main__":
    main()


def enter_airport(airports):
    icao_code = input("Enter the ICAO code of the airport: ").upper()
    if icao_code in airports:
        print("This airport is already in the system.")
    else:
        airport_name = input("Enter the name of the airport: ")
        airports[icao_code] = airport_name
        print(f"Airport {airport_name} with ICAO code {icao_code} has been added.")


def fetch_airport(airports):
    icao_code = input("Enter the ICAO code of the airport to fetch: ").upper()
    if icao_code in airports:
        print(f"The airport with ICAO code {icao_code} is: {airports[icao_code]}")
    else:
        print("No airport found with that ICAO code.")

def main():
    airports = {}

    while True:
        print("\nChoose an option:")
        print("1. Enter a new airport")
        print("2. Fetch airport information")
        print("3. Quit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            enter_airport(airports)
        elif choice == "2":
            fetch_airport(airports)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()