# Import Python's built-in json module to read from and write to JSON files
import json

# Constant holding the name of the file where Omondi's car fleet data is stored
FILE_NAME = "fleet.json"


def load_fleet():
    """Reads the car fleet dictionary from the JSON file and returns it."""
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_fleet(fleet):
    """Writes the updated car fleet dictionary back to the JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(fleet, file, indent=4)


def add_car(fleet, model, release_year, acquired_year, plate_number):
    """Adds a new car to Omondi's fleet if the plate number is not already registered."""
    if plate_number in fleet:
        print("Car already available")
        return

    fleet[plate_number] = {
        "model": model,
        "release_year": release_year,
        "acquired_year": acquired_year,
        "money_made": 0.0,
        "times_rented": 0,
    }
    save_fleet(fleet)
    print("Car added successfully")


def remove_car(fleet, plate_number):
    """Removes a car from the fleet using its plate number."""
    if plate_number in fleet:
        del fleet[plate_number]
        save_fleet(fleet)
        print("Removed successfully")
    else:
        print("Car not found")


def rent_car(fleet, plate_number, rental_fee):
    """Records a rental transaction by updating the car's rental count and revenue."""
    if plate_number not in fleet:
        print("Car not found in collection")
        return

    fleet[plate_number]["times_rented"] += 1
    fleet[plate_number]["money_made"] += rental_fee
    save_fleet(fleet)
    print("Car rented successfully")


def display_report(fleet):
    """Displays the rental count and total money made for every car in the fleet."""
    print("\n--- Omondi's Car Rental Report ---")
    if not fleet:
        print("No cars currently in the fleet.")
        return

    for plate_number, details in fleet.items():
        print(
            f"Plate: {plate_number} | Model: {details['model']} "
            f"({details['release_year']}) | Acquired: {details['acquired_year']} | "
            f"Rented: {details['times_rented']} times | "
            f"Money Made: ${details['money_made']:.2f}"
        )


def main():
    """Runs an interactive menu loop for managing Omondi's car rental business."""
    # Load the initial fleet from fleet.json once when the program starts
    fleet = load_fleet()

    # Keep showing the menu until the user chooses option 5 to exit
    while True:
        print("\n===============================")
        print("  OMONDI'S CAR RENTAL SYSTEM")
        print("===============================")
        print("1. Rent a car")
        print("2. Add a new car")
        print("3. Remove a car")
        print("4. View fleet report (rentals & money made)")
        print("5. Exit")

        # Read the user's menu choice and strip any accidental whitespace
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            # Normalize plate input to uppercase so 'kda 101a' matches 'KDA 101A'
            plate_number = input("Enter car plate number to rent: ").strip().upper()
            try:
                rental_fee = float(input("Enter rental fee ($): "))
                if rental_fee < 0:
                    print("Rental fee cannot be negative.")
                    continue
                rent_car(fleet, plate_number, rental_fee)
            except ValueError:
                print("Invalid amount. Please enter a numeric rental fee.")

        elif choice == "2":
            plate_number = input("Enter new car plate number: ").strip().upper()
            model = input("Enter car model: ").strip()
            try:
                release_year = int(input("Enter release year: "))
                acquired_year = int(input("Enter year acquired: "))
                add_car(fleet, model, release_year, acquired_year, plate_number)
            except ValueError:
                print("Invalid year. Please enter whole numbers for years.")

        elif choice == "3":
            plate_number = input("Enter car plate number to remove: ").strip().upper()
            remove_car(fleet, plate_number)

        elif choice == "4":
            display_report(fleet)

        elif choice == "5":
            print("Exiting Omondi's Car Rental System. Goodbye!")
            break  # Exit the while True loop

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()