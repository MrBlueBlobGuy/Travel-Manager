import hashlib

import mysql.connector as mysql

user = input('enter mysql user: ')
password = input('Enter mysql password: ')

cnx = mysql.connect(user=user if not user == "" else "root",
                    password=password if not password == "" else "1234",
                    host='localhost')
cursor = cnx.cursor(buffered=True)

# Create the database
cursor.execute('CREATE DATABASE IF NOT EXISTS travelmanage;')
# Create the user table
cursor.execute(
    'CREATE TABLE IF NOT EXISTS travelmanage.user (userid VARCHAR(256) PRIMARY KEY UNIQUE, hashedpassword VARCHAR(256));')
# Create the trip table
cursor.execute(
    'CREATE TABLE IF NOT EXISTS travelmanage.trip (tripid INT UNIQUE NOT NULL PRIMARY KEY, destination VARCHAR(256) NOT NULL, source VARCHAR(256) NOT NULL, start_date DATETIME NOT NULL, end_date DATETIME NOT NULL, user_id VARCHAR(256) NOT NULL, FOREIGN KEY (user_id) REFERENCES travelmanage.user(userid));')


# Function to Add A Trip
def add_trip(trip_id, source, destination, start_date, end_date, userid):
    try:
        cursor.execute(
            'INSERT INTO travelmanage.trip(tripid, destination, source, start_date, end_date, user_id) VALUES (%s, %s, %s, %s, %s, %s);',
            (trip_id, destination, source, start_date, end_date, userid))
        cnx.commit()
        return True
    except mysql.errors.IntegrityError:
        return False


# Function To Get All Active Trips of user
def get_all_trips_of_user(userid):
    try:
        cursor.execute(
            'SELECT tripid, destination, source, start_date, end_date from travelmanage.trip where user_id = %s;',
            (userid,))
        return cursor.fetchall()
    except mysql.errors.Error:
        return []


def get_trip(trip_id, user_id):
    try:
        cursor.execute(
            'SELECT tripid, destination, source, start_date, end_date from travelmanage.trip where tripid = %s AND user_id = %s;',
            (trip_id, user_id))
    except mysql.errors.Error:
        return ()


def adduser(userid, hashed_password):
    try:
        cursor.execute('INSERT INTO travelmanage.user(userid, hashedpassword) VALUES (%s, %s);',
                       (userid, hashed_password))
        cnx.commit()
        return True
    except mysql.errors.IntegrityError:
        return False


def getuser(userid):
    cursor.execute('SELECT userid, hashedpassword FROM travelmanage.user WHERE userid = %s;', (userid,))
    return cursor.fetchall()


def get_user_hashed_password(userid):
    cursor.execute('SELECT hashedpassword FROM travelmanage.user WHERE userid = %s', (userid,))
    return cursor.fetchone()


def cancel_trip(tripid, user_pw: str):
    cursor.execute('SELECT user_id FROM travelmanage.trip WHERE tripid = %s;', (tripid,))
    uid = cursor.fetchone()[0]
    cursor.execute('SELECT hashedpassword FROM travelmanage.user WHERE userid = %s;', (uid,))
    if user_pw == hashlib.sha1(user_pw.encode()).hexdigest():
        cursor.execute('DELETE FROM travelmanage.trip WHERE tripid=%s;', (tripid,))
    cnx.commit()
