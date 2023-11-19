# app.py file handles the user input and calls a function accordingly
import random
import hashlib

from TravelManage.user import login
from TravelManage.userdb import get_all_trips_of_user, getuser, adduser, get_trip, add_trip, cancel_trip


def app_login():
    user = input('Enter UserID: ')
    password = input('Enter Password: ')
    return login(user, password)


def get_unique_user_id(c=0):
    inp = input("Enter New User Id: ") if c == 0 else input("Enter New User Id (Previous Already Taken): ")

    if not list(getuser(inp)) == []:
        get_unique_user_id(c + 1)

    return inp


def app_add_user():
    user = get_unique_user_id()
    passwd = input("Enter Secure Password: ")

    return adduser(userid=user, hashed_password=hashlib.sha1(passwd.encode()).hexdigest())


def app_add_new_trip(user):
    destination = input("Enter Trip Destination -> ")
    source = input("Enter Trip Source -> ")
    start_date = input("Start Date in YYYY-MM-DD HH:MI:SS -> ")
    end_date = input("End Date in YYYY-MM-DD HH:MI:SS -> ")

    return add_trip(random.choice(range(100000, 1000000)), source, destination, start_date, end_date, user.userid)


def app_get_all_trips(user):
    for i in get_all_trips_of_user(user.userid):
        print(i)


def app_cancel(user):
    tripid = input("Enter Trip ID: ")
    password = input(f"Enter Password for {user.userid}: ")
    cancel_trip(tripid, password)



def run():
    c_user = None
    no_exit = True
    help_text = """
                ------------------TravelManage-----------------
                 Command 	     Description
                    h       Show this help command
                    n	    Add new Trip (Opens New Trip)
                    l	    Login to user (Opens Login)
                    r       Register user (Opens Register Form)
                    c       Cancels existing trip
                    s       Shows Existing trip details
                    e       Exit
                -----------------------------------------------"""
    while no_exit:
        action = input('enter action (h for help): ')

        if action == 'e':
            return

        elif action == 'h':
            print(help_text)

        elif action == 'l':
            print("registering new user")
            c_user = app_login()

        elif action == 'r':
            print("registering new user")
            c_user = app_add_user()

        elif action == 'c':
            app_cancel(c_user)

        elif action == 'n':
            if c_user is not None:
                app_add_new_trip(c_user)
            else:
                print("retry after logging in")
                c_user = app_login()

        elif action == 's':
            if c_user is not None:
                app_get_all_trips(c_user)
            else:
                print("retry after logging in")
                c_user = app_login()


run()
