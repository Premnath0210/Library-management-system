# login.py
def authenticate(username, password):
    # Simple mock authentication
    if username == "admin" and password == "password123":
        return True
    return False

def login():
    print("=== Login System ===")
    user = input("Username: ")
    pwd = input("Password: ")
    
    if authenticate(user, pwd):
        print("Login successful!")
    else:
        print("Invalid credentials.")