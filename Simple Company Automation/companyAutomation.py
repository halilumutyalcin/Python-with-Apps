class Company():
    def __init__(self):
        self.status = True

    def program(self):
        selection = self.menu()

        if selection == 1:
            self.add()
        if selection == 2:
            self.remove()
        if selection == 3:
            chooseTime = input("Would you like to do it on a yearly basis? [Y / N]")
            if chooseTime == "Y":
                self.showSalary(calculating="Y")
            else:
                self.showSalary()
        if selection == 4:
            self.giveSalary()

    def menu(self):

        print(
            "**** Welcome Automation **** \n \n1-Add employees. \n2-Remove employees. \n3-Show salaries to be paid. \n4-Give salaries. \n")
        selection = int(input("Enter your selection: "))
        while selection < 1 or selection > 4:
            selection = int(input("Please enter value between 1 and 4:  "))
        return selection

    def add(self):
        id = 1
        name = input("Enter the employee's name: ")
        surname = input("Enter the employee's surname: ")
        age = input("Enter the employee's age: ")
        gender = input("Enter the employee's gender: ")
        salary = input("Enter the employee's salary: ")

        with open("personnel.txt", "r") as file:
            personnelList = file.readlines()

        if len(personnelList) == 0:
            id = 1
        else:
            with open("personnel.txt", "r") as file:
                id = int(file.readlines()[-1].split(")")[0]) + 1

        with open("personnel.txt", "a+", encoding="utf-8") as file:
            file.write("{}) {} - {} - {} - {} - {} \n".format(id, name, surname, age, gender, salary))

    def remove(self):
        with open("personnel.txt", "r") as dosya:
            employees = dosya.readlines()
        newPersonnels = []

        for humans in employees:
            newPersonnels.append(" ".join(humans[:-1].split("-")))

        for humans in newPersonnels:
            print(humans)

        selection2 = int(
            input("Please enter the number of the employee you want to remove [1- {}]: ".format(len(newPersonnels))))

        while selection2 < 0 or selection2 > len(newPersonnels):
            selection2 = int(input("Please enter a value between 1- {}:".format(len(newPersonnels))))

        employees.pop(selection2 - 1)

        count = 1

        newEmployees = []

        for humans in employees:
            newEmployees.append(str(count) + ")" + humans.split(")")[1])
            count += 1

        with open("personnel.txt", "w") as dosya:
            dosya.writelines(newEmployees)

    def showSalary(self, calculating="Y"):

        with open("personnel.txt", "r") as file:
            employees = file.readlines()

        salaries = []

        for humans in employees:
            salaries.append(int(humans.split("-")[-1]))
        if calculating == "Y":
            print("Salary you have to pay this month: {}".format(sum(salaries)))
        else:
            print("Salary you have to pay this year: {}".format(sum(salaries) * 12))

    def giveSalary(self):
        with open("personnel.txt", "r") as file:
            humans = file.readlines()

        salaries = []

        for humans in humans:
            salaries.append(int(humans.split("-")[-1]))

        totalsalary = sum(salaries)

        with open("budget.txt", "r") as file:
            budget = int(file.readlines()[-1])

        budget = budget - totalsalary

        with open("budget.txt", "w") as file:
            file.write(str(budget))


home = Company()

while home.status:
    home.program()
