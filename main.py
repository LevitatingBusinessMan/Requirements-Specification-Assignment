import serial
import sqlite3

sql_con = sqlite3.connect("data.db")
sql_cursor = sql_con.cursor()
sql_cursor.execute("CREATE TABLE IF NOT EXISTS cards(hash PRIMARY KEY, credit)")


def sql(query):
    #print(query)
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
    print("> ", end='')
    rawinput = input().split()

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
                print("No valid amount")
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
                print("No valid amount")
                continue

            uid = get_rfid()
            credit = getcredit(uid)
            if credit < amount:
                print("Not enough credit")
                continue
            credit -= amount
            setcredit(uid,credit)
            print(f"New credit: {credit}")
