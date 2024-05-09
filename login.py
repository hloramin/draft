username = ""
password = ""
def login():
  while login:
    username = str(input("What is your username?: "))
    password = str(input("What is your password? "))
    if username == "admin" and password == "admin":
      print("Welcome Aleks")
      break
    else:
      print("The incorrect username or password. Try again!")
      continue
    
print("LOGIN SYSTEM")
login()