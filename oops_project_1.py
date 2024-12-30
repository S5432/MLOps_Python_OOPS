class chatter:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()
    
    def menu(self):
        user_input = input(""" Welcome to Chatter!! How would you like to proceed?
                           1. Press 1 to Signin
                           2. Press 2 to SignUp
                           3. Press 3 to write a Post
                           4. Press 4 to message your Friend
                           5 Press any other key to exit  """)
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()

        else:
            exit()
    
    def signup(self):
        email = input("Enter your email here -->")
        password = input("Setup your password here -->")
        self.username = email
        self.password = password
        print("You have signed up successfully!!!")
        print("\n")
        self.menu()
    
    def signin(self):
        if self.username == "" and self.password == "":
            print("Please Signup first by pressing 1 in the main menu")
        else:
            uname = input("Enter your email/username here ->")
            pwd = input("Enter your password here ->")
            if self.username ==uname and self.password ==pwd:
                print("You have signed in successfully!!")
                self.loggedin = True
            else:
                print("Please enter the correct credentials..")
        print("\n")
        self.menu()
    
    def my_post(self):
        if self.loggedin ==True:
            txt = input("Enter your message here ->")
            print(f"Following content has been posted ->{txt}")
        else:
            print("You need to signin first to post something.")
        print("\n")
        self.menu()
    
    def sendmsg(self):
        if self.loggedin ==True:
            txt = input("Enter the send msg ->")
            frnd = input("Whom to send this msg ->")
            print(f"Your message has been sent to {frnd} ")
        else:
            print("You need to signin first to message.")
        print("\n")
        self.menu()
obj = chatter()
        
       