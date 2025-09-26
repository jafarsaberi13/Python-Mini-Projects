import datetime
from fileinput import filename


def menu():
    print("1: Your details")
    print("2: Expense details")
    print("3: Income details")
    print("4: Total")
    print("5: Add Income")
    print("6: Add Expense")
    print("7: Exit")

def welcomeMenu():
    print("1: Login")
    print("2: SignUp")
    print("3: Exit")

def Login():
    s = str(input("Enter your username: "))
    password = input("Enter your password: ")

    with open("Files/UsersInfo/UserInfo.txt") as userInfo:
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

    userInfo = open("Files/UsersInfo/UserInfo.txt", "a")
    userInfo.write(f"{s},{password},{firstName},{lastName},{email}\n")
    userInfo.close()
    print("==================================")
    print("Signed up successfully!")
    print("==================================")
def readFile(userName, password):
    with open("Files/UsersInfo/UserInfo.txt") as userInfo:
        for i in userInfo.readlines():
            l = i.split(",")
            if l[0] == userName and l[1] == password:
                return l

    return None

def addIncomeOrExpense(userName, select):
    l = []
    file_name = ""
    if select == 1:
        file_name  = f"Files/Income/{userName}Income.txt"

    elif select == 2:
        file_name = f"Files/expense/{userName}expense.txt"

    return addToFile(file_name)

def addToFile(fileName):
    l = []
    lebal = "Income" if "Income" in fileName else "expense"

    with open(fileName, "a") as file:
        while True:
            userInput = str(input(f"Enter your {lebal} (# for exit): "))
            if userInput == "#":
                break
            file.write(f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")},{userInput}\n")
            l.append(userInput)

    return l

def calcaluteTotal(userame):
    income = calcalute(f"Files/Income/{userame}Income.txt")
    expense = calcalute(f"Files/expense/{userame}expense.txt")

    return income - expense

def calcalute(path):
    total = 0
    with open(f"{path}") as file:
        for i in file.readlines():
            total = total + int(i.split(",")[1])
    return total

def printIncomeOrExpenseDetails(path, select):
    if select == 1:
        print("Your Incomes: ")
    else:
        print("Your expenses")

    with open(f"{path}") as file:
        for i in file.readlines():
            l = i.split(",")
            print(l[0], "\t==>>", f"\"{l[1][:len(l[1])-1]}\"")

def main():
    usersInfo = open("Files/UsersInfo/UserInfo.txt", "a")
    usersInfo.close()

    print("Welcome to Expense Tracker")
    while True:
        welcomeMenu()
        print("==================================")
        try:
            choice = int(input("Please select your option: "))
        except:
            print("Please enter a valid option.")
            continue
            print("==================================")
        if choice == 1:
            b, username, password = Login()

            if b:
                print("logined successfully")
                print("==================================")

                # transfar them to sign up
                incomeFile = open(f"Files/Income/{username}Income.txt", "a")
                expenseFile = open(f"Files/expense/{username}expense.txt", "a")
                incomeFile.close()
                expenseFile.close()
                while True:
                    menu()
                    print("==================================")
                    ch = 0
                    while True:
                        ch = int(input("Select your option: "))
                        if ch in range(1, 8):
                            break
                        else:
                            print("Enter a valid option (1, 2, 3, 4)")

                    if ch == 1: # showing details
                        info = readFile(username, password)
                        print("Your Details")
                        print(f"User name: {info[0]}\nPassword: {info[1]}\nFirst Name: {info[2]}\nLast Name: {info[3]}\nEmail: {info[4]}\n")
                        print("=====================================")
                    elif ch == 2: #expense details
                        printIncomeOrExpenseDetails(f"Files/expense/{username}expense.txt", 2)
                        print("=====================================")
                    elif ch == 3: # Income details
                        printIncomeOrExpenseDetails(f"Files/Income/{username}Income.txt", 1)
                        print("=====================================")
                    elif ch == 4: # total
                        total = calcaluteTotal(username)
                        print(f"Total: {total}")
                        print("=====================================")
                    elif ch == 5: # Add income
                        print(addIncomeOrExpense(username, 1))
                        print("=====================================")
                    elif ch == 6: # Add expense
                        print(addIncomeOrExpense(username, 2))
                        print("=====================================")
                    elif ch == 7: # exit
                        break
                    else:
                        print("Invalid Input (1 - 7)")
                        print("Enter Again")

            else:
                print("Login Failed")
                print("Wrong username or password")
                print("Enter again")
                print("==================================")

        elif choice == 2:
            signUp()
        elif choice == 3:
            print("Thank you for using Expense Tracker")
            break
        else:
            print("Invalid choice")
            print("Enter a valid option (1, 2, 3)")
            print("==================================")

if __name__ == '__main__':
    main()