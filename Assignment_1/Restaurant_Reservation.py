# Restaurant Reservation System

import sqlite3

con = sqlite3.connect("registrations.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS registration (Email TEXT, First Name TEXT, Last Name TEXT, Password TEXT,"
            "Date Of Birth TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS reservation (Email TEXT, Password TEXT, Number_of_Days TEXT, Start_Date TEXT,"
               "End_Date TEXT, Number_of_Persons TEXT, Number_of_Rooms TEXT)")


def main_menu():
    print(f"Welcome to our Reservation System")
    print(f"a. Register/Signup \nb. Login \nc. Exit")
    user_in = input("Please enter the letter associated with the action stated above. Ex: a/A for Register/Signup")
    if user_in == "a" or user_in == "A":
        p1 = Registration()
        p1.registration()
    elif user_in == "b" or user_in == "B":
        p2 = reservation()
        p2.login()
        p2.login_menu()
    elif user_in == "c" or user_in == "C":
        print(f"Thank you for using our reservation system.")
        exit()
    else:
        print("Sorry we didn't understand. Please try again.")
        main_menu()


class Registration:

    def __init__(self):
        self.Email = ""
        self.FirstName = ""
        self.LastName = ""
        self.Password = ""
        self.DateOfBirth = ""
        self.fields = {"Email": self.Email, "First Name": self.FirstName, "Last Name": self.LastName,
                  "Password": self.Password, "Date of Birth": self.DateOfBirth}

    def registration(self):
        print(f"Registration In-Process, please fill all the data for registration. Enter 'exit' to cancel registration")

        registration_complete = False
        while registration_complete == False:
            for field in self.fields:
                while self.fields[field] == "":
                    self.fields[field] = input(f"Please enter your {field}:")
                    try:
                        int(self.fields[field])
                        print(f"Please enter a string for {field}.")
                        self.fields[field] = ""
                    except ValueError:
                         pass
                    if self.fields[field] == "exit":
                        main_menu()

            cur.execute("INSERT INTO registration VALUES(?,?,?,?,?)", (self.fields["Email"], self.fields["First Name"],
                        self.fields["Last Name"], self.fields["Password"], self.fields["Date of Birth"]))
            con.commit()

            registration_complete = True
            print(f"Registration Complete.")

            main_menu()


class reservation:

    def __init__(self):
        self.username = ""
        self.password = ""
        self.number_of_days = ""
        self.start_date = ""
        self.end_date = ""
        self.number_of_persons = ""
        self.number_of_rooms = ""

    def login(self):
        logged_in = False
        while logged_in == False:
            print("Type 'exit' to go back to the main menu at any time.")

            self.username = input(f"Enter your Email: ")
            if self.username == "exit":
                main_menu()

            self.password = input(f"Enter your Password: ")
            if self.password == "exit":
                main_menu()

            cur.execute(f"SELECT Email, Password FROM registration WHERE Email = '{self.username}'"
                        f"AND Password = '{self.password}'")
            data = cur.fetchall()
            print(data)

            if data != []:
                logged_in = True
            else:
                print("Credentials not correct please try again")

    def login_menu(self):
        login_menu_complete = False
        while login_menu_complete == False:
            print("Reservation Menu:\na. View Reservation \nb. Make Reservation \nc. Modify Reservation"
                  "\nd. Cancel Reservation \ne. Logout")

            user_inp = input(f"Please enter the corresponding letter with the action above. Ex: 'a' to View Registration.")

            if user_inp == "a":
                cur.execute(f"SELECT * FROM reservation WHERE Email = '{self.username}' AND Password = '{self.password}'")
                data = cur.fetchall()
                if data != []:
                    print(data)
                else:
                    print("No reservation found")

            elif user_inp == "b":

                print("Type 'exit' at any point to go back to the main menu.")

                while self.number_of_days == "":
                    try:
                        self.number_of_days = int(input(f"Number of days: "))
                    except:
                        print("Please enter a number for number of days.")
                        self.number_of_days = ""
                    if self.number_of_days == "exit":
                        main_menu

                while self.start_date == "":
                    self.start_date = input(f"Start Date: ")
                    try:
                        int(self.start_date)
                        print(f"Please enter a start date.")
                        self.start_date = ""
                    except:
                        pass
                    if self.start_date == "exit":
                        main_menu

                while self.end_date == "":
                    self.end_date = (input(f"End Date: "))
                    try:
                        int(self.end_date)
                        print(f"Please enter a end date.")
                        self.end_date = ""
                    except:
                        pass
                    if self.end_date == "exit":
                        main_menu

                while self.number_of_persons == "":
                    try:
                        self.number_of_persons = int(input(f"Number of persons: "))
                    except:
                        print("Please enter a number for number of persons.")
                        self.number_of_persons = ""
                    if self.number_of_persons == "exit":
                        main_menu

                while self.number_of_rooms == "":
                    try:
                        self.number_of_rooms = int(input(f"Number of rooms: "))
                    except:
                        print("Please enter a number for number of rooms.")
                        self.number_of_rooms = ""
                    if self.number_of_rooms == "exit":
                        main_menu

                cur.execute("INSERT INTO reservation VALUES(?,?,?,?,?,?,?)",
                               (self.username, self.password, self.number_of_days, self.start_date, self.end_date,
                                self.number_of_persons, self.number_of_rooms))
                con.commit()

            elif user_inp == "c":
                print("What would you like to change about your reservation? \na. Number of Days \nb. Start date"
                      "\nc. End Date \nd. Number of Persons \ne. Number of Rooms")
                modify_res = input("Enter the letter that you would like to change about your reservation.")

                if modify_res == "a":
                    self.number_of_days = ""
                    while self.number_of_days == "":
                        try:
                            self.number_of_days = int(input(f"What would you like to change this to? "))
                        except:
                            print("Please enter a number for number of days.")
                            self.number_of_days = ""
                    cur.execute(f"UPDATE reservation SET Number_of_Days ='{self.number_of_days}' WHERE Email = '{self.username}'")
                    con.commit()

                if modify_res == "b":
                    self.start_date = ""
                    while self.start_date == "":
                        try:
                            self.start_date = input(f"What would you like to change this to?")
                            int(self.start_date)
                            print(f"Please enter a start date.")
                            self.start_date = ""
                        except:
                            pass
                    cur.execute(
                        f"UPDATE reservation SET Start_Date ='{self.start_date}' WHERE Email = '{self.username}'")
                    con.commit()

                if modify_res == "c":
                    self.end_date = ""
                    while self.end_date == "":
                        try:
                            self.end_date = input(f"End Date: ")
                            int(self.end_date)
                            print(f"Please enter a end date.")
                            self.end_date = ""
                        except:
                            pass
                    cur.execute(
                        f"UPDATE reservation SET End_Date ='{self.end_date}' WHERE Email = '{self.username}'")
                    con.commit()

                if modify_res == "d":
                    self.number_of_persons = ""
                    while self.number_of_persons == "":
                        try:
                            self.number_of_persons = int(input(f"Number of persons: "))
                        except:
                            print("Please enter a number for number of persons.")
                            self.number_of_persons = ""
                    cur.execute(
                        f"UPDATE reservation SET Number_of_Persons ='{self.number_of_persons}' WHERE Email = '{self.username}'")
                    con.commit()

                if modify_res == "e":
                    self.number_of_rooms = ""
                    while self.number_of_rooms == "":
                        try:
                            self.number_of_rooms = int(input(f"Number of rooms: "))
                        except:
                            print("Please enter a number for number of rooms.")
                            self.number_of_rooms = ""
                    cur.execute(
                        f"UPDATE reservation SET Number_of_Rooms ='{self.number_of_rooms}' WHERE Email = '{self.username}'")
                    con.commit()


            elif user_inp == "d":
                cur.execute(f"DELETE FROM reservation WHERE Email='{self.username}'")
                con.commit()
                print("Record Successfully Deleted")

            elif user_inp == "e":
                login_menu_complete = True

        main_menu()

main_menu()

