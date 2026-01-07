# library.py
# Added login module
from login import login
login()
print("Library Management System")
# New: Student Registration Module
def register_student(name, student_id):
    return f"Student {name} (ID: {student_id}) registered."

# Test the function
if __name__ == "__main__":
    print(register_student("Alice", "S001"))
