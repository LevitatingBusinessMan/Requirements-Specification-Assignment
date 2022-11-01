import serial
import sqlite3
#import pyreadline3

#readline.set_auto_history(True)
verbose = False

print(
    "Group 46 presents..."
    "\n",
    " ____ ______________     __________               \n",
    "|    |   \__    ___/     \______   \_____  .__.__.\n",
    "|    |   | |    |  ______ |     ___/\__  \ |  |  |\n",
    "|    |   | |    | /_____/ |    |     / __ \|___  |\n",
    "|________| |____|         |____|    (____  / ____|\n",
    "                                         \/\/     ",
)

sql_con = sqlite3.connect("data.db")
sql_cursor = sql_con.cursor()
sql_cursor.execute("CREATE TABLE IF NOT EXISTS cards(hash PRIMARY KEY, credit)")

def blue(str): return f"\033[34m{str}\033[0m"
def red(str): return f"\033[31m{str}\033[0m"
def yellow(str): return f"\033[93m{str}\033[0m"
def gray(str): return f"\033[90m{str}\033[0m"
def green(str): return f"\033[32m{str}\033[0m"

def sql(query):
    if verbose: print(gray(query))
    res = sql_cursor.execute(query)
    sql_con.commit()
    return res

def get_rfid():
    ser = serial.Serial("/dev/ttyACM0", 9600)
    ser.reset_input_buffer()
    data = ser.readline()
    if data:
        data = data.decode()
        data = data.strip()
        return data

def register(uid):
    sql(f"INSERT INTO cards VALUES ('{uid}', 0)")
    print(f"Registered {uid}")

def getcredit(uid):
    res = sql(f"SELECT credit FROM cards WHERE hash = '{uid}'").fetchone()
    if res is None:
        register(uid)
        return 0
    else:
        return res[0]

def setcredit(uid,credit):
    res = sql(f"UPDATE cards SET credit = {credit} WHERE hash='{uid}'")    

while True:
    print(blue("> "), end='')
    
    rawinput = input().split()
    if len(rawinput) < 1:
        print()
        continue

    cmd = rawinput.pop(0)

    args = rawinput

    match cmd:
        case "read":
            uid = get_rfid()
            credit = getcredit(uid)
            print(f"{uid}: {credit} credit")

        case "add":
            try: 
                amount = int(args[0])
            except:
                print(yellow("Not a valid amount"))
                continue

            uid = get_rfid()
            credit = getcredit(uid)
            credit += amount
            setcredit(uid,credit)
            print(f"New credit: {credit}")

        case "pay":
            try: 
                amount = int(args[0])
            except:
                print(yellow("Not a valid amount"))
                continue

            uid = get_rfid()
            credit = getcredit(uid)
            if credit < amount:
                print(yellow("Not enough credit"))
                continue
            credit -= amount
            setcredit(uid,credit)
            print(f"New credit: {credit}")

        case "debug":
            verbose = not verbose
            print(gray(f"Debuggin is {('on' if verbose else 'off')}"))

        case other:
            print("Unknown command")
