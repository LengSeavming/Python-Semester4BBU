


dic_item = {
    "id": 1,
    "name": "vital",
    "price": 1,
    "Expire_date": "09-09-2025",
}

dic_student = {
    "student_info":{
        "id":1,
        "name":"Dara",
        "phone":1234567,
        "address":"PP",
        "parent": [
            {"id":1, "father's name": "FaFa", "mother's name": "MoMo"},
            {"id":2, "father's name": "TaTa", "mother's name": "MaMa"}
        ]
    },
    "academic_info":{
        "degree": "Bachelor",
        "school": "Science and Technology",
        "field": "Information Technology",
        "promotion": 24,
        "stage": 1,
        "term": 4,
    }
}

if __name__ == '__main__':
    # print(dic_item["name"])
    # print(dic_student["academic_info"])
    # print(dic_student["student_info"]["parent"])
    # for parent in dic_student["student_info"]["parent"]:
        # print("My father name is ", parent["father's name"])
    print("ID\t\tFather Name\t\tMother Name")
    for p in dic_student["student_info"]["parent"]:
        print(f"{p["id"]}\t\t{p["father's name"]}\t\t\t{p["mother's name"]}")


