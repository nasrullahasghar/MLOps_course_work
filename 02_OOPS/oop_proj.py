class ChatBook:
    __user_id = 1

    def __init__(self):
        self.id = ChatBook.__user_id
        ChatBook.__user_id =+ 1
        self.__name = "sam"    # <---- Encapsulation
        self.username = ""
        self.password = ""
        self.loggedin = False
        # self.menu()


    # Getters
    def get_name(self):
        return self.__name

    @staticmethod
    def get_id():
        return ChatBook.__user_id

    # Setter
    def set_name(self,new_val):
        self.__name = new_val

    @staticmethod
    def set_id(new_id):
        ChatBook.__user_id = new_id

    def menu(self):
        user_input = input("""
                            Welcomr to ChatBook! How would you like to proceed?
                            Press 1 to Signup.
                            Press 2 to Login.
                            Press 3 to Write a post.
                            Press 4 to message a friend.
                            Press any other key to exit.
                        """)

        if user_input =="1":
            self.signup()
        if user_input =="2":
            self.signin()
        if user_input =="3":
            self.mypost()
        if user_input =="4":
            self.sentmessage()
        else:
            exit()

    def signup(self):
        email = input("enter your email here ->")
        pswd = input("setup your password here ->")
        self.username = email
        self.password = pswd
        print("You have signed up successfully!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == "" and self.password =="":
            print("Please Signup first by pressing 1 in main menu")
        else:
            uname = input("enter your email/username here ->")
            pswd = input("Enter your password here ->")
            if self.username == uname and self.password == pswd:
                print("You have signed in successfully!")
                self.loggedin = True
            else:
                print("Please input the correct credentials..")
        print("\n")
        self.menu()


    def mypost(self):
        if self.loggedin == True:
            txt = input("Enter your message here")
            print(f"Folowing content has been posted -> {txt}")
        else:
            print("You need to signin by pressing 2 to post something...")
        print("\n")
        self.menu()


    def sentmessage(self):
        if self.loggedin == True:
            msg = input('Enter your messsage here')
            frnd = input("Whom to send the message?")
            print(f"Your message have been sent to {frnd}")
        else:
            print("You need to signin by pressing 2 to send a message...")
        print("\n")
        self.menu()

obj = ChatBook()
