import apicalls
from createTableView import CreateView


def nav_menu():
    print("=================================================")
    print("________Welcome to PyConnect Admin Portal________")
    print("=================================================")
    print("\n**Navigation Menu**\n")
    print("0) Exit")
    print("1) List All Users")
    print("2) Get User by Id")
    print("3) Get All Posts")
    print("4) Get Posts by UserId")


def take_user_input():
    while True:
        nav_menu_input = input("Enter your option here:\t")
        if nav_menu_input.isdigit():
            nav_menu_input = int(nav_menu_input)
            if nav_menu_input in (0, 1, 2, 3, 4):
                return nav_menu_input
            else:
                print("Enter a correct option (0, 1, or 2)")
        else:
            print("Enter a correct option (0, 1, or 2)")


def main():
    table = CreateView()
    nav_menu()
    nav_input = take_user_input()
    if nav_input == 1:
        headers = list(
            filter(
                lambda x: x not in ["company", "address"],
                list(apicalls.getAllUsers()[0].keys()),
            )
        )
        printable_users = table.createView(headers=headers, data=apicalls.getAllUsers())
        print(printable_users)
    if nav_input == 2:
        user_id_input = input("Enter User Id  here : ")
        printable_user = table.createSingleView(
            data=apicalls.getUserById(user_id_input)
        )
        print(printable_user)
    elif nav_input == 3:
        headers = list(apicalls.getAllPosts()[0].keys())
        printable_posts = table.createView(headers=headers, data=apicalls.getAllPosts())
        print(printable_posts)
    elif nav_input == 0:
        exit()


if __name__ == "__main__":
    while True:
        main()
