######################################
########                      ########
# https://github.com/halilumutyalcin #
########                      ########
######################################


import json
from random import randint

class System:
    def __init__(self):
        self.status = True
        self.data = self.getData()

    def run(self):
        self.showMenu()
        selection = self.menuChoose()

        if selection == 1:
            self.login()

        if selection == 2:
            self.register()

        if selection == 3:
            self.forgetPassword()

        if selection == 4:
            self.exit()

    def showMenu(self):
        print("""
1-Login.
2-Register.
3-Did you forget the password?
4-Exit.
        """)

    def menuChoose(self):
        while True:
            try:
                selection = int(input("Enter your choice:"))
                while selection < 1 or selection > 4:
                    selection = int(input("Please enter your choice between 1-4: "))

            except ValueError:
                print("Please enter number!\n")

            break
        return selection

    def getData(self):
        try:
            with open("users.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("users.json", "w") as file:
                file.write("{}")

            with open("users.json", "r") as file:
                data = json.load(file)

        return data

    def login(self):
        usernm = input("Enter your nickname: ")
        pswd = input("Enter your password: ")
        stts = self.check(usernm, pswd)

        if stts:
            self.trueLogin()
        else:
            self.failedLogin("Information incorrect ")

    def register(self):
        usernm = input("Enter your nickname: ")

        while True:
            pswd = input("Enter your password: ")
            pswdr = input("Re-enter your password: ")
            """
            We checked if their passwords match.
            """

            if pswd == pswdr:
                break
            else:
                print("The passwords you entered dont match, please re-renter your password: ")
        email = input("Enter your e-mail: ")

        sts = self.haveRegister(usernm, email)

        if sts:
            print("This user name or e-mail address is registered in the system.")
        else:
            code = self.sendCode()
            stscode = self.checkCode(code)

            if stscode:
                self.save(usernm, pswd, email)
            else:
                print("Activation code invalid!")

    def forgetPassword(self):
        email = input("Enter your e-mail:")
        if self.haveMail(email):
            with open("activationCode.txt", "w") as file:
                activation = str(randint(1000, 9999))
                file.write(activation)

            enterAc = input("Enter your activation code: ")

            if enterAc == activation:
                while True:
                    newPswd = input("Enter your new password: ")
                    newPswdr = input("Re-enter your new password: ")

                    if newPswd == newPswdr:
                        break
                    else:
                        print("The passwords you entered dont match, re-enter.")

            self.data = self.getData()

            for user in self.data["users"]:
                if user["email"] == email:
                    user["pswd"] = newPswd

            with open("users.json", "w") as file:
                json.dump(self.data, file)
                print("Password changed succesfully.")

        else:
            print("Such e-mail is not registered in our system.")

    def haveMail(self, email):
        self.data = self.getData()

        for user in self.data["users"]:
            if user["email"] == email:
                return True

        return False

    def exit(self):
        self.status = False
        print("See you later!")

    def check(self, usernm, pswd):
        self.data = self.getData()

        for user in self.data["users"]:
            if user["usernm"] == usernm and user["pswd"] == pswd:
                return True
        return False

    def failedLogin(self,reason):
        print(reason)

    def trueLogin(self):
        print("Welcome Home!")
        self.status = False

    def haveRegister(self, usernm, email):
        self.data = self.getData()
        try:
            for user in self.data["users"]:
                if user["usernm"] == usernm and user["email"] == email:
                    return True
                else:
                    return False
        except KeyError:
            return False

        return False

    def sendCode(self):
        with open("activationCode.txt", "w") as file:
            code = str(randint(1000, 9999))
            file.write(code)

        return code

    def checkCode(self, code):
        getCode = input("Enter your activation code: ")

        if code == getCode:
            return True
        else:
            return False

    def save(self, usernm, pswd, email):
        self.data = self.getData()

        try:
            self.data["users"].append({"usernm": usernm, "pswd": pswd, "email": email})
        except KeyError:
            self.data["users"] = []
            self.data["users"].append({"usernm": usernm, "pswd": pswd, "email": email})

        with open("users.json", "w") as file:
            json.dump(self.data, file)
            print("Your registration has been created successfully.")

system = System()

while system.status:
    system.run()

# import json
#
# with open("users.json","r") as file:
#     data = json.load(file)
# print(data)
# print(data["users"][0]["usernm"])