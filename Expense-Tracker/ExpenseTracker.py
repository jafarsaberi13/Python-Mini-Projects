
def menu():
    print("1: Your details")
    print("2: Expense details")
    print("3: Income details")
    print("4: Total")

def welcomeMenu():
    print("1: Login")
    print("2: SignUp")
    print("3: Exit")

def Login():
    s = str(input("Enter your username: "))
    password = input("Enter your password: ")


def SignUp():
    s = str(input("Enter your username: "))
    password = str(input("Enter your password: "))
def main():
    print("Welcome to Expense Tracker")
    while True:
        welcomeMenu()
        choice = input("Please select your option:")
        if choice == "1":
            pass

if __name__ == '__main__':
    main()