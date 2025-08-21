import json

def create_new_file():
    """Creates a new JSON file named student.json if it doesn't exist."""
    with open('student.json', 'w') as file:
        json.dump([], file)

def write_file_mode_a(student_list):
    """Appends student data to student.json in append mode."""
    with open('student.json', 'r+') as file:
        data = json.load(file)
        data.extend(student_list)
        file.seek(0)
        json.dump(data, file, indent=4)

def write_file_mode_w(student_list):
    """Overwrites student.json with new student data."""
    with open('student.json', 'w') as file:
        json.dump(student_list, file, indent=4)

def read_text():
    """Reads and prints the student.json content."""
    with open('student.json', 'r') as file:
        data = json.load(file)
        for student in data:
            print(student)

def read_texts():
    """Reads and returns the content of student.json as a list."""
    with open('student.json', 'r') as file:
        return json.load(file)

# Create the JSON file
create_new_file()

# Define student dictionary
student_dic = {
    "id": "001",
    "name": "John Doe",
    "gender": "Male",
    "phone": "123456789",
    "address": "123 Main St",
    "dob": "2000-01-01"
}

# Create student list with 56 students
student_list = []  

for _ in range(56):
    new_student = {}  
    new_student.update(student_dic)  # Copy values into a new dictionary
    student_list.append(new_student)


# Append list to JSON file
write_file_mode_a(student_list)

# Read and print data
read_text()
