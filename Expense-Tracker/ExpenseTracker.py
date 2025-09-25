
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

    with open("UserInfo") as userInfo:
        for i in userInfo.readlines():
            l = i.split(",")
            if s == l[0] and password == l[1]:
                return True, s, password

    return False, "", ""

def SignUp():
    s = str(input("Enter your username: "))
    password = str(input("Enter your password: "))
    email = str(input("Enter your email: "))

    userInfo = open("UserInfo.txt", "a")
    userInfo.write(f"{s},{password},{email},{0},{0}\n")
    userInfo.close()

def main():
    usersInfo = open("UserInfo.txt", "r")
    usersInfo.close()

    print("Welcome to Expense Tracker")
    while True:
        welcomeMenu()
        choice = input("Please select your option:")
        if choice == "1":
            b, username, password = Login()

            if b:
                print("logined successfully")
                menu()
                ch = 0
                while True:
                    if ch not in range(1, 5):
                        continue
                    else:
                        break

                

            else:
                print("Login Failed")
                print("Wrong username or password")
                print("Enter again")

        elif choice == "2":
            pass
        elif choice == "3":
            print("Thank you for using Expense Tracker")
            break
        else:
            print("Invalid choice")
            print("Enter a valid option (1, 2, 3)")

if __name__ == '__main__':
    main()