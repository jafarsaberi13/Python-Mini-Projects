
def menu():
    print("1: Your details")
    print("2: Expense details")
    print("3: Income details")
    print("4: Total")
    print("5: Add Income")
    print("6: Add Expense")

def welcomeMenu():
    print("1: Login")
    print("2: SignUp")
    print("3: Exit")

def Login():
    s = str(input("Enter your username: "))
    password = input("Enter your password: ")

    with open("UserInfo.txt") as userInfo:
        for i in userInfo.readlines():
            l = i.split(",")
            if s == l[0] and password == l[1]:
                return True, s, password

    return False, "", ""

def signUp():
    s = str(input("Enter your username: "))
    password = str(input("Enter your password: "))
    firstName = str(input("Enter your first name: "))
    lastName = str(input("Enter your last name: "))
    email = str(input("Enter your email: "))

    userInfo = open("UserInfo.txt", "a")
    userInfo.write(f"{s},{password},{firstName},{lastName},{email},{0},{0}\n")
    userInfo.close()

def readFile(userName, password):
    with open("UserInfo.txt") as userInfo:
        for i in userInfo.readlines():
            l = i.split(",")
            if l[0] == userName and l[1] == password:
                return l

    return None

def main():
    usersInfo = open("UserInfo.txt", "a")
    usersInfo.close()

    print("Welcome to Expense Tracker")
    while True:
        welcomeMenu()
        choice = int(input("Please select your option: "))
        if choice == 1:
            b, username, password = Login()
            print(b , username, password)
            if b:
                print("logined successfully")
                menu()
                ch = 0
                while True:
                    ch = int(input("Select your option: "))
                    if ch in range(1, 5):
                        break
                    else:
                        print("Enter a valid option (1, 2, 3, 4)")

                if ch == 1: # showing details
                    info = readFile(username, password)
                    print("Your Details")
                    print(f"User name: {info[0]}\nPassword: {info[1]}\nFirst Name: {info[2]}\nLast Name: {info[3]}\nEmail: {info[4]}\nIncome: {info[5]}\nExpense: {info[6]}")
                    print("=====================================")
                elif ch == 2: #expense details
                    pass
                elif ch == 3: # Income details
                    pass
                elif ch == 

            else:
                print("Login Failed")
                print("Wrong username or password")
                print("Enter again")

        elif choice == 2:
            signUp()
        elif choice == 3:
            print("Thank you for using Expense Tracker")
            break
        else:
            print("Invalid choice")
            print("Enter a valid option (1, 2, 3)")

if __name__ == '__main__':
    main()