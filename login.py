import time

home = False
back = ""
name = ""
names = ["Admin","Bot"]
usernames = ["test", "username"]
passwords = ["test", "password"]
username = ""
password = ""
user = {
  "name": name,
  "username": username,
  "password": password
}  

def clock():
  print("\n~ Clock ~")
  print(f"\nYour time is : {time.asctime()}")
  input("\nEnter to go back : ")
  print("\n~ Going Back ~")
  time.sleep(1)
  tools()
  
def stopwatch() :

  #Use threading for this
  elapsedTime = 0
  print("\n~ Stopwatch ~")
  input("\nEnter to start the stopwatch")
  for elapsedTime in range(10000):
    if elapsedTime == 0:
      print("Enter to stop the stopwatch:")  
    print(f"Seconds elapsed: {elapsedTime}", end='\r')
    time.sleep(1)
    elapsedTime += 1
  
  print(f"The stopwatch ran for {round(elapsedTime, 2)} seconds")
  input("\nEnter to go back : ")
  print("\n~ Going Back ~")
  time.sleep(1)
  tools()

def tools() :
  tool = input("\nWhat tool do you want to use? \nStopwatch | Clock | Go Back\n\nLocation: ")
  if tool.lower().replace(" ","") == "stopwatch":
    stopwatch()
  elif tool.lower().replace(" ","") == "clock":
    clock()  
  elif tool.lower().replace(" ","") == "goback":
    print("\n~ Sending you back ~")
    time.sleep(1)
    homepage()
  else : 
    print("Not a location")
    tools()
  
def account() :
    global name 
    global names
    global usernames
    global passwords
    global username
    global password
    global home   
    global user 

    print(f"\n~ Account ~\nCurrent Name : {user['name']}")
    print(f"Current Username : {user['username']}")
    print(f"Current Password : {user['password']}")
    if username == "test":
        print("\n~ You are an Admin! ~")
    else : 
        print("\n~ You are not an Admin! ~")

    input("\nEnter to go back : ")
    print("\n~ Going Back ~")
    time.sleep(1)
    homepage()

def admin() : 
    global name 
    global names
    global usernames
    global passwords
    global username
    global password
    global home   
    global user 

    print(f"\n~ Admin ~\nAll Names : {names}")
    print(f"\nAll Usernames : {usernames}")
    print(f"\nAll Passwords : {passwords}")


    def find():
        global name 
        global names
        global usernames
        global passwords
        global username
        global password
        global home   
        global user

        getUser = input("\nWhich Username do you want the information to? : ").replace(" ","")
        if getUser in usernames:
            if usernames.index(getUser) != 0 :
                arrayNum = usernames.index(getUser)  
                print(f"\nName : {names[arrayNum]}\nUsername : {usernames[arrayNum]}\nPassword : {passwords[arrayNum]}\n")
                delete = input("Would you like to delete this user? y/n : ")
                if delete.lower().replace(" ","") == "y":
                    print(f"Deleting User {usernames.index(getUser) + 1}")
                    usernames.pop(arrayNum)
                    passwords.pop(arrayNum)
                    names.pop(arrayNum)
                    time.sleep(1)

                elif delete.lower().replace(" ","") == "n":
                    print("Okay!")
                    time.sleep(1)
                else :
                    print("This not a correct answer!")
                    time.sleep(1)
                    find() 
            else :
                print("You can't delete yourself dumb admin!")
                find()
        elif getUser.lower().replace(" ","") == "none":
            print("\n~ Sending to Homepage!")
            time.sleep(1)
            homepage()
        else :
            print("\nIs not a user")
            find()
    find()


    input("\nEnter to go back : ")
    print("\n~ Going Back ~")
    time.sleep(1)
    homepage()

def homepage() :

    global name 
    global names
    global usernames
    global passwords
    global username
    global password
    global home   
    global user 

    user["name"] = names[usernames.index(username)]  
    user["username"] = usernames[usernames.index(username)]
    user["password"] = passwords[usernames.index(username)]

    if home == False : 
        home = True
        print(f"\n~ Logged In ~\n\nWelcome {user['name']}!")
    else : 
        print("\n~ Welcome Back to the Homepage ~")

    location = input("\nWhere would you like to go?\nAccount | Admin | Tools | Log Out\n\nLocation: ")
    if location.lower().replace(" ","") == "account":
        account()
    elif location.lower().replace(" ","") == "admin":
        if usernames.index(username) == 0 :
          admin()  
        else :
            print("\nYou do not have access!\nSending you back home")
            time.sleep(1)
            homepage()
    elif location.lower().replace(" ","") == "tools":
      print("\n~ Sending you to Tools ~")
      time.sleep(1)
      tools()
    elif location.lower().replace(" ","") == "logout":
        home = False
        print("\n~ Logging Out ~")
        time.sleep(1)
        startup()
    else : 
      print("Not a location")
      homepage()
      
def startup() :

    global name
    global names
    global usernames
    global passwords
    global username
    global password

    def login() :
        global name
        global names
        global usernames
        global passwords  
        global username
        global password 

        username = input("\nEnter Username : ")


        if username in usernames:
                print("Is a Username\n")
                password = input("Enter Password : ")
                if password in passwords[usernames.index(username)]: 
                    print("~ Logging In ~")
                    time.sleep(1)
                    homepage()
                else : 
                    print("Is not the correct password \nTry Again!")
                    time.sleep(1)
                    startup()
        else : 
                print("Is not a Username \nTry Again!")
                time.sleep(1)
                startup()

    def signUp() :
        global name
        global names
        global usernames
        global passwords
        global username
        global password 

        print("\n~ Sign Up Screen ~")

        name = input("\nWhat is your name? ") 
        names.append(name)

        username = input("\nWhat do you want your username to be? : ")
        if username in usernames :
            print("That is already a Username\n\n~ Sending to Start ~\n")
            time.sleep(1)
            startup()
        else : 
            usernames.append(username)

        password = input("\nWhat do you want your password to be? : ")
        passwords.append(password)
        print(f"Your password is : {password}\n\n~ Sending you to Log In ~")
        time.sleep(1)
        print("\n~ Log In Screen ~")
        login()

    print("\n~ Start Up Page ~")          
    signIn = input("Login or Sign Up? : ")
    if signIn.lower().replace(" ","") == "signup":
        print("~ Opening ~")
        time.sleep(1)
        signUp()
    else: 
        if signIn.lower().replace(" ","") == "login": 
            print("~ Opening ~")
            time.sleep(1)
            login()
        else :
            print("That is not an option")
            time.sleep(1)
            startup()


startup()

