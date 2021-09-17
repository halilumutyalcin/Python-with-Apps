import sqlite3
import colorama
import getpass
import datetime
import random


class Tweeter:
    def __init__(self):
        self.status = True
        self.connect_database()
        self.create_table()
        self.get_data()

    def connect_database(self):
        self.db = sqlite3.connect("data.db")
        self.cursor = self.db.cursor()

    def create_table(self):
        get_user = "CREATE TABLE IF NOT EXISTS users (id INTEGER, username, password)"
        get_tweets = "CREATE TABLE IF NOT EXISTS tweets (username, text, dtime)"

        self.cursor.execute(get_user)
        self.cursor.execute(get_tweets)

    def get_data(self):
        self.cursor.execute("SELECT * FROM users")
        self.user_data = self.cursor.fetchall()
        self.cursor.execute("SELECT * FROM tweets")
        self.tweets_data = self.cursor.fetchall()

    def get_id(self):
        ids = list(range(100000, 999999))
        idm = random.choice(ids)
        ids.remove(idm)
        return idm

    def menu(self):
        print(f"""
--! Welcome to Tweeter - {datetime.datetime.now()}
[1] - Login.
[2] - Register.
[3] - Forgot Password.
[4] - Exit.        
""")

    def choose(self):
        global selection
        while True:
            try:
                selection = int(input("Enter your choice:"))
                while selection < 1 or selection > 4:
                    selection = int(input("Please enter your choice between 1-4: "))

            except ValueError:
                print("Please enter number!\n")
            break

        return selection

    def run(self):
        self.menu()
        self.selection = self.choose()

        if self.selection == 1:
            self.login()
        if self.selection == 2:
            self.register()
        if self.selection == 3:
            self.forgot_password()
        if self.selection == 4:
            self.exit()

    def login(self):
        global username
        username = input("Enter username: ")
        pswd = input("Enter password: ")
        entry_1 = (username, pswd)
        self.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", entry_1)
        a = self.cursor.fetchone()

        admin = (555, "admin", "admin")

        self.cursor.execute("SELECT * FROM users WHERE id = ? OR username = ? OR password = ?;", admin)
        _admin = self.cursor.fetchone()

        try:
            inf = []
            inf.append(a[1])
            inf.append(a[2])
        except TypeError:
            print("WRONG INFORMATION.")

        try:

            if entry_1[0] == inf[0] and entry_1[1] == inf[1]:
                if a == _admin:
                    self.admin_run()
                else:
                    self.user_run()
            else:
                print("WRONG INFORMATION.")
        except IndexError:
            pass

    def register(self):
        username = input("Enter username: ")
        pswd = input("Enter password: ")
        rpswd = input("Enter re-password again: ")

        idm = self.get_id()

        entry_2 = (idm, username, pswd)

        if pswd == rpswd:
            try:
                self.cursor.execute("INSERT INTO users VALUES (?,?,?)", entry_2)
                self.db.commit()
                print("Successfully registered")
                print(f"Your ID: {idm}")
                print("Please dont forget ID.")
            except:
                print("THIS ACCOUNT ALREADY EXISTS.")
        else:
            print("WRONG INFORMATION.")

# --! Admin

    def admin_page(self):
        print(f"""
--! Welcome to Tweeter - {datetime.datetime.now()}
[1] - Look at data.
[2] - Delete user.
[3] - Search users data with username.
[4] - Exit.
""")

    def admin_choose(self):
        global admin_selection
        while True:
            try:
                admin_selection = int(input("Enter your choice:"))
                while admin_selection < 1 or admin_selection > 4:
                    admin_selection = int(input("Please enter your choice between 1-3: "))

            except ValueError:
                print("Please enter number!\n")
            break
        return admin_selection

    def admin_run(self):
        self.admin_page()
        self.admin_selection = self.admin_choose()

        if self.admin_selection == 1:
            self.look_data()
            self.admin_run()
        if self.admin_selection == 2:
            self.delete_user()
            self.admin_run()
        if self.admin_selection == 3:
            self.search_data()
            self.admin_run()
        if self.admin_selection == 4:
            self.exit()

    def look_data(self):
        print(f"Number of users: {self.cursor.execute('SELECT Count() FROM users').fetchone()[0]}")
        print(f"Number of tweets: {self.cursor.execute('SELECT Count() FROM tweets').fetchone()[0]}")
        self.admin_run()

    def delete_user(self):
        user = input("Enter the username who want you delete: ")
        self.cursor.execute("SELECT * FROM users WHERE username = ?", user)
        _x = self.cursor.fetchone()
        if _x == None:
            print("WRONG INFORMATION")
        else:
            self.cursor.execute("DELETE FROM users WHERE username = ?", user)
            self.cursor.execute("DELETE FROM tweets WHERE username = ?", user)
            self.db.commit()
            print(f"User deleted: {user}")

    def search_data(self):
        _user = input("Enter the username: ")
        self.cursor.execute("SELECT * FROM users WHERE username = ?", _user)
        total_inf = self.cursor.fetchone()
        self.cursor.execute("SELECT * FROM tweets WHERE username = ?", _user)
        total_tweets = self.cursor.fetchall()
        self.cursor.execute("SELECT Count() FROM tweets WHERE username = ?", _user)
        _count = self.cursor.fetchone()
        print(f"""
ID: {total_inf[0]}
Username: {total_inf[1]}     
Password: {total_inf[2]}        
""")
        for i in range(_count[0]):
            print(f"Tweet: {total_tweets[i][1]}")

# --! User

    def user_page(self):
        print(f"""
--! Welcome to Tweeter - {datetime.datetime.now()}
[1] - Tweet.
[2] - Look at timeline.
[3] - Exit. 
        """)

    def user_choose(self):
        global user_selection
        while True:
            try:
                user_selection = int(input("Enter your choice:"))
                while user_selection < 1 or user_selection > 3:
                    user_selection = int(input("Please enter your choice between 1-3: "))

            except ValueError:
                print("Please enter number!\n")
            break
        return user_selection

    def user_run(self):
        self.user_page()
        self.user_selection = self.user_choose()

        if self.user_selection == 1:
            self.tweet()
            self.user_run()
        if self.user_selection == 2:
            self.timeline()
            self.user_run()
        if self.user_selection == 3:
            self.exit()

    def forgot_password(self):
        id = input("Enter your ID: ")
        name = input("Enter your name: ")
        self.cursor.execute("SELECT * FROM users WHERE id = ? AND username = ?", (id,name))
        inf = self.cursor.fetchone()
        print(inf)
        print(inf[0])
        print(inf[1])
        a = inf[0]
        b = inf[1]

        if id == a and name == b:
            print("eşleşti")
        else:
            print("olmadı")

    def tweet(self):
        dtime = datetime.datetime.now()
        twt = input("Tweet it: ")
        entry_3 = (username, twt, dtime)

        self.cursor.execute("INSERT INTO tweets VALUES (?,?,?);", entry_3)
        self.db.commit()
        print("Tweet was send.")

    def timeline(self):
        self.cursor.execute("SELECT * FROM tweets")
        database = self.cursor.fetchall()
        tweet_data = []

        for i in range(len(database)):
            tweet_data.append(database[i][0:2])
        tweet_data.reverse()

        print("Press g for go, press q for exit timeline.")

        count = 0

        while 1:
            click = input("")
            if click == "g":
                count += 1
                see = tweet_data[count - 1]

                print(see[0])
                print("*" * len(see[0]))
                print(see[1] + "\n")

            if click == "q":
                self.user_run()
                break

    def exit(self):
        self.status = False
        self.db.close()


twitter = Tweeter()
while twitter.status:
    twitter.run()