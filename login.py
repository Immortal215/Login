import time
import pickle
import pprint


home = False
back = ""
name = ""
username = ""
password = ""
names = []
usernames = []
passwords = []
balances = []
balance = 0
userWins = 0 
userLosses = 0 

class user:
    def __init__(self):
        self.userData = { "users" : { "names": [] , "usernames" : [], "passwords": [], "balances" : [], "allWins" : [], "allLosses" : []} }

def pickleAll():
    with open('data.pickle', 'wb') as file:
        try:
            my_data = user.userData
        except :
            my_data = { "users" : { "names": ["Admin"] , "usernames" : ["test"], "passwords": ["test"], "balances" : [99999], "allWins" : [9999], "allLosses" : [0] } }
        pickle.dump(my_data, file)

# Shows data.pickle in readable text
    obj = pickle.load(open("data.pickle", "rb"))

    with open("data.pickle", "a") as f:
        f.write("\n\n||          ||\nvv Readable vv\n~~~~~~~~~~~~~~~\n")
        pprint.pprint(obj, stream=f)

def unPickle():
    global names
    global usernames
    global passwords
    global balances
    
    with open('data.pickle', 'rb') as f:
        try : 
         loaded_data = pickle.load(f)
   
         user.userData = loaded_data
         names = user.userData["users"]["names"]
         usernames = user.userData["users"]["usernames"]
         passwords = user.userData["users"]["passwords"]
         balances = user.userData["users"]["balances"]
        except : 
          print("\n\n~ Error Loading Data ~\n\n")
        

# def deleteFile():
#   with open("data.pickle", 'w') as database:
#       database.write('')


def games():
    global name
    global username
    global password
    global balance 
    global home
    global names
    global usernames
    global passwords
    global balances
    
    unPickle()

    name = names[usernames.index(username)]
    username = usernames[usernames.index(username)]
    password = passwords[usernames.index(username)]
    balance = balances[usernames.index(username)]
    
    def loan():
        print("~ Welcome to Loans! ~")
        
    def blackjack():
        print("~ Welcome to Blackjack! ~")
        
    def slots():
        print("~ Welcome to Slots! ~")
        
    def leaderboards():
        print("~ Welcome to the Leaderboards! ~")
        
    print(f"\n~ Welcome to GAMES! ~\nYou currently have ${balance}!")
    location = input(f"\nWhat game would you like to play?\nLoan |{' BlackJack (b) | Slots (s) | Local Leaderboards (l) |' if balance > 0 else ''} Back (e)\n\nLocation: ")
    
    if location.lower().replace(" ","") == "loan":
      print("\n~ Sending you to Loans ~")
      time.sleep(1)
      loan()
    elif location.lower().replace(" ","") == "b":
      print("\n~ Sending you to BlackJack ~")
      time.sleep(1)
      blackjack()
    elif location.lower().replace(" ","") == "s":
      print("\n~ Sending you to Slots ~")
      time.sleep(1)
      slots()
    elif location.lower().replace(" ","") == "l":
      print("\n~ Sending you to Leaderboards ~")
      time.sleep(1)
      leaderboards()
    elif location.lower().replace(" ","") == "e":
        home = True
        print("\n~ Back to Home ~")
        time.sleep(1)
        homepage()
    else :
      print("Not a location")
      homepage()

def clock():
  print("\n~ Clock ~")
  print(f"\nYour time is : {time.asctime()}")
  input("\nEnter to go back : ")
  print("\n~ Going Back ~")
  time.sleep(1)
  tools()

def stopwatch() :

  def exit():
      input("Enter to stop the stopwatch")

  elapsedTime = 0
  print("\n~ Stopwatch ~")
  input("\nEnter to start the stopwatch")
#   x = threading.Thread(target=exit)
#   x.start()
  for elapsedTime in range(10000):
    if elapsedTime == 0:
      print("Enter to stop the stopwatch:")
    print(f"Seconds elapsed: {elapsedTime}", end='\r')
    time.sleep(1)



  print(f"The stopwatch ran for {round(elapsedTime, 2)} seconds")
  input("\nEnter to go back : ")
  print("\n~ Going Back ~")
  time.sleep(1)
  tools()

def tools() :

    tool = input("\nWhat tool do you want to use? \nStopwatch (s) | Clock (c) | Go Back (b)\n\nLocation: ")
    if tool.lower().replace(" ","") == "s":
        # x = threading.Thread(target=stopwatch)
        # watchInUse = True
        # x.start()
        stopwatch()
    elif tool.lower().replace(" ","") == "c":
        clock()
    elif tool.lower().replace(" ","") == "b":
        print("\n~ Sending you back ~")
        time.sleep(1)
        homepage()
    else :
        print("Not a location")
        tools()

def account() :

    global name
    global username
    global password
    global balances
    global names
    global passwords
    global usernames
    global home
    
    unPickle()


    name = names[usernames.index(username)]
    username = usernames[usernames.index(username)]
    password = passwords[usernames.index(username)]
    balance = balances[usernames.index(username)]

    print(f"\n~ Account ~\nName : {name}\nUsername : {username}\nPassword : {password}\nBalance : ${balance}")
    
    if usernames.index(username) == 0 :
        print("\n~ You are an Admin! ~")
    else :
        print("\n~ You are not an Admin! ~")

    input("Would you like to change anything within your account?")
    print("Work In Progress")
    input("\nEnter to go back : ")
    print("\n~ Going Back ~")
    time.sleep(1)
    homepage()

def admin() :
    global name
    global username
    global password
    global names
    global balances
    global passwords
    global usernames
    global home 
    
    unPickle()

    name = names[usernames.index(username)]
    username = usernames[usernames.index(username)]
    password = passwords[usernames.index(username)]


    for i in usernames :
        print(f"\n~ Admin ~\nUser : {i}, Name : {names[usernames.index(i)]}, Password : {passwords[usernames.index(i)]}, Balance : {balances[usernames.index(i)]}\n")

    def find():
        global name
        global username
        global password
        global home

        unPickle()

        names = user.userData["users"]["names"]
        usernames = user.userData["users"]["usernames"]
        passwords = user.userData["users"]["passwords"]
        balances = user.userData["users"]["balances"]


        name = names[usernames.index(username)]
        username = usernames[usernames.index(username)]
        password = passwords[usernames.index(username)]
        balance = balances[balances.index(username)]


        getUser = input("\nWhich Username do you want the information to? : ").replace(" ","")
        if getUser in usernames:
            if usernames.index(getUser) != 0 :
                arrayNum = usernames.index(getUser)
                print(f"\nName : {names[arrayNum]}\nUsername : {usernames[arrayNum]}\nPassword : {passwords[arrayNum]}\nBalance : {balances[arrayNum]}")
                delete = input("Would you like to delete this user? y/n : ")
                if delete.lower().replace(" ","") == "y":
                    print(f"Deleting User {usernames.index(getUser) + 1}")
                    usernames.pop(arrayNum)
                    passwords.pop(arrayNum)
                    names.pop(arrayNum)
                    balances.pop(arrayNum)

                    user.userData["users"]["names"] = names
                    user.userData["users"]["usernames"] = usernames
                    user.userData["users"]["passwords"] = passwords
                    user.userData["users"]["balances"] = balances


                    pickleAll()

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
    global username
    global password
    global names
    global passwords
    global usernames
    global home

    unPickle()

    name = names[usernames.index(username)]
    username = usernames[usernames.index(username)]
    password = passwords[usernames.index(username)]


    if home == False :
        home = True
        print(f"\n~ Logged In ~\n\nWelcome {name}!")
    else :
        print("\n~ Welcome Back to the Homepage ~")

    location = input(f"\nWhere would you like to go?\nAccount (a) | Games (g) | Tools (t)|{' Admin |' if usernames.index(username) == 0 else ''} Log Out (e)\n\nLocation: ")

    if location.lower().replace(" ","") == "a":
        account()
    elif location.lower().replace(" ","") == "admin":
        if usernames.index(username) == 0 :
          admin()
        else :
            print("\nYou do not have access!\n")
            homepage()
    elif location.lower().replace(" ","") == "g":
      print("\n~ Sending you to Games ~")
      time.sleep(1)
      games()
    elif location.lower().replace(" ","") == "t":
      print("\n~ Sending you to Tools ~")
      time.sleep(1)
      tools()
    elif location.lower().replace(" ","") == "e":
        home = False
        print("\n~ Logging Out ~")
        time.sleep(1)
        startup()
    else :
      print("Not a location")
      homepage()

def startup() :
    
    global name
    global username
    global password
    global balance
    global names
    global usernames
    global passwords
    
    try : 
        unPickle()

    except FileNotFoundError: 
        pickleAll()






    def login() :

        unPickle()

        global name
        global username
        global password
        global names
        global passwords
        global usernames

        username = input("\nEnter Username : ")

        if username in usernames:
                print("Is a Username\n")
                password = input("Enter Password : ")
                if password == passwords[usernames.index(username)]:
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
        
        unPickle()
        

        
        global name
        global username
        global password
        global names
        global passwords
        global usernames

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
        user.userData["users"]["names"].append(name)
        user.userData["users"]["usernames"].append(username)
        user.userData["users"]["passwords"].append(password)
        user.userData["users"]["balances"].append(0)


        pickleAll()

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

