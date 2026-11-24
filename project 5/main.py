class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def compute_area(self) -> float:
        # Calculates and returns the area of the rectangle.
        return self.length * self.width

def main():
    try:
        # Prompt the user for length and width of the rectangle
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))

        if length <= 0 or width <= 0:
            print("Length and width must be positive numbers.")
            return
        # Create a Rectangle object with the provided dimensions
        rect = Rectangle(length, width)

        # Compute and display the area of the rectangle
        print(f"The area of the rectangle is: {rect.compute_area()}")

    except ValueError:
        print("Invalid input. Please enter numeric values for length and width.")

if __name__ == "__main__":
    main()
