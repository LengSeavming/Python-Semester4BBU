# from my_class import *
#
# if name == 'main':
#     objStudent = Student()
#     objStudent.show()

#day2
# from my_class import *
#
# if name == 'main':
#     objStudent = Student(pid=1, pname="bbu pp", pgender="Male", pphone="0123", paddress="PP")
#     objStudent.show()

#day2
#=== Inheritance ===
from myclass import *
#
# if name == 'main':
#     objStudent = Student(pid="PP001", pname="Sokha", pgender="Male", pweight="10", pheight="10", pdob="09-09-2025",
#                          pphone="0123", paddress="PP", pemail="sokha@gmail.com", pdegree="Bachelor",
#                          pschool="Build Bright University", pfield="Information Technology",
#                          ppromotion=24, pstage=1, pterm=4, pgroup="D1-IT")
#     objStudent.show()
#     pass


if __name__ == '__main__':
    objCar = Car()
    # print(objCar.model)
    # print(objCar.get_id())
    objCar.set_id(3)
    objCar.set_name("Toyota")
    objCar.set_model("Brand")
    objCar.set_year("2010")
    print(f"ID: {objCar.get_id()}"
          f"\nName: {objCar.get_name()}"
          f"\nModel: {objCar.get_model()}"
          f"\nYear: {objCar.get_year()}")