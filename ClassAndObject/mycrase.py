class Student:
    # id = 1
    # name = "bbu pp"
    # gender = "Male"
    # address = "PP"
    # phone = "0123" #properties

    def __init__(self):
        self.id = 1
        self.name = "bbu"
        self.gender = "Male"
        self.phone = "0123"
        self.__address = "PP"

    def show(self):
        print("ID\t Name\t Gender \t Phone \t Address")
        print(f"{self.id} \t{self.name}\t\t{self.gender}")