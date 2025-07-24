from app.db.database import Base, engine
from app.models.user import User
from app.utils.user_actions import create_user, login_user


def main_menu():
    while True:
        print("\n=== Digital Wallet ===")
        print("1. Create a new account")
        print("2. Login")
        print("3. Exit")

        choice = input("Please choose what to do: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            create_user(username, password)
        elif choice == "2":
            username = input("Username ")
            password = input("Password: ")
            user = login_user(username, password)
            if user:
                print(f"Welcome back, {user.username}! Your balance is: ${user.balance_usd}")
        elif choice == "3":
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main_menu()

