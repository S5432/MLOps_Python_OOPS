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
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass

        else:
            exit()
    
    def signup(self):
        email = input("Enter your email here -->")
        password = input("Setup your password here -->")

obj = chatter()
        
       