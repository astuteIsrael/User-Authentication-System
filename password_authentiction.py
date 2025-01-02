import getpass
database = {"clcoding":"1234", "pythonclcoding":"2502"}
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")
for i in database.keys():
    if i == username:
        while password != database.get(i):
            password = getpass.getpass("Enter your password again: ")
            break
print("verified")
