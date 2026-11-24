class StringHandler:
    def __init__(self):
        # initialize a attribute to store the user's string
        self.text = ""

    def get_string(self):
        # prompt the user to enter a string and store it in the text attribute
        self.text = input("Enter a string: ")

    def print_string(self):
        # print the string in uppercase
        print(self.text.upper())  

def main():
    # creates an object for the string class
    handler = StringHandler()

    # calls the two methods
    handler.get_string()
    handler.print_string()

if __name__ == "__main__":
    main()