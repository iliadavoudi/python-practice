data = ["ilia", "ali", "davoudi", "mohamadi", "kolagar", 2012, 5424, 1391]


def main():
    name = input("Enter your name: ")
    last_name = input("Enter your last name: ")
    password = int(input("Enter your password: "))

    result = account(name, last_name, password)
    print(result)


def account(name, last_name, password):

    if name in data and last_name in data and password in data:
        return "Welcome!! you can enter"

    else:
        ask = input(
            "Oh you do not have any account!! "
            "(if you want create account enter yes): "
        )

    if ask == "yes":
        name = input("Enter your name: ")
        data.append(name)

        last_name = input("Enter your last name: ")
        data.append(last_name)

        password = int(input("Enter your password: "))
        data.append(password)

        return name, last_name, password

    else:
        return "goodbye"


main()
