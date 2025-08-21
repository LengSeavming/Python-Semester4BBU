# class Student:
#     def init(self):
#         self.id = 168
#         self.name = "Seavminh"
#         self.gender = "M"
#         self.address = "PP"
#         self.phone = "0967650501" + "016340652"
#
#     def show(self):
#         print("ID\tName\tGender\tAddress\tPhone")
#         print(f"{self.id}\t{self.name}\t{self.gender}\t\t{self.address}\t\t{self.phone}")

#day 2
#=== Inheritance ===
# class Person:
#     def init(self, pid, pname, pgender, pweight, pheight, pdob):
#         self.id     = pid
#         self.name   = pname
#         self.gender = pgender
#         self.weight = pweight
#         self.height = pheight
#         self.dob    = pdob
#     pass
# #day 2
# class Student(Person):
#     def init(self, pid, pname, pgender, pweight, pheight, pdob,
#                  pphone, paddress, pemail, pdegree, pschool, pfield,
#                  ppromotion, pstage, pterm, pgroup):
#         super().init(pid, pname, pgender,pweight,pheight,pdob) #style 1
#         # Person.init(self, pid, pname, pgender, pweight, pheight,pdob) #style 2
#         self.phone = pphone
#         self.address = paddress
#         self.email = pemail
#         self.degree = pdegree
#         self.school = pschool
#         self.field  = pfield
#         self.promotion = ppromotion
#         self.stage = pstage
#         self.term = pterm
#         self.group = pgroup
#     def show(self):
#         print(f"ID = {self.id}"
#               f"\nName ={self.name}"
#               f"\nGender = {self.gender}"
#               f"\nWeight = {self.weight}"
#               f"\nHeight = {self.height}"
#               f"\nDOB = {self.dob}"
#               f"\nPhone = {self.phone}"
#               f"\nAddress = {self.address}"
#               f"\nEmail = {self.email}"
#               f"\nDegree = {self.degree}"
#               f"\nSchool = {self.school}"
#               f"\nField = {self.field}"
#               f"\nPromotion = {self.promotion}"
#               f"\nStage = {self.stage}"
#               f"\nTerm = {self.term}"
#               f"\nGroup = {self.group}")

# === Polymorphism ===

# Encapsulation

class Car:
    def __init__(self):
        self.__id = 0
        self.__name = ""
        self.__model = ""
        self.__year = ""
    def get_id(self):
        return self.__id
    def set_id(self,pid):
        self.__id=pid
    def get_name(self):
        return self.__name
    def set_name(self, pname):
        self.__name = pname
    def get_model(self):
        return self.__model
    def set_model(self, pmodel):
        self.__model = pmodel
    def get_year(self):
        return self.__year
    def set_year(self, pyear):
        self.__year = pyear

    def car_info(self):
        print(f"ID: ")


