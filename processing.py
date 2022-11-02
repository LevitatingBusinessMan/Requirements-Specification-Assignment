import serial
import sqlite3
import bcrypt
from Crypto.Cipher import AES

verbose = False

AES_KEY = bytearray([0xd7, 0xe7, 0xeb, 0x9e, 0x4c, 0xce, 0x25, 0x43, 0x62, 0x91, 0x1b, 0xdd, 0x3d, 0xf2, 0x16, 0xb2])
aes = AES.new(AES_KEY, AES.MODE_ECB)

BCRYPT_SALT = b'$2b$12$' + bcrypt._bcrypt.encode_base64(b'peppereddeadbeef')

sql_con = sqlite3.connect("data.db")
sql_cursor = sql_con.cursor()
sql_cursor.execute("CREATE TABLE IF NOT EXISTS cards(hash PRIMARY KEY, credit)")

def blue(str): return f"\033[34m{str}\033[0m"
def red(str): return f"\033[31m{str}\033[0m"
def yellow(str): return f"\033[93m{str}\033[0m"
def gray(str): return f"\033[90m{str}\033[0m"
def green(str): return f"\033[32m{str}\033[0m"

def sql(query):
    global verbose
    if verbose: print(gray(query))
    res = sql_cursor.execute(query)
    sql_con.commit()
    return res

def get_rfid():
    ser = serial.Serial("/dev/ttyACM1", 9600)
    ser.reset_input_buffer()
    data = ser.read(16)
    if data:
        uid = aes.decrypt(data).split(b'\x00')[0]
        hash = bcrypt.hashpw(uid, BCRYPT_SALT)
        return hash.decode()

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

def read():
    uid = get_rfid()
    credit = getcredit(uid)
    return (uid, credit)

def add(amount):
    uid = get_rfid()
    credit = getcredit(uid)
    credit += amount
    setcredit(uid,credit)
    return (uid, credit)

# The credit will be returned as -1 if the balance
# is low enough
def pay(amount):
    uid = get_rfid()
    credit = getcredit(uid)
    if credit < amount:
        return (uid, -1)
    credit -= amount
    setcredit(uid,credit)
    return (uid, credit)

def main():
    #import readline
    #readline.set_auto_history(True)

    global verbose

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
                uid, credit = read()
                print(f"{uid}: {credit} credit")

            case "add":
                try: 
                    amount = int(args[0])
                except:
                    print(yellow("Not a valid amount"))
                    continue

                uid, credit = add(amount)
                print(f"New credit: {credit}")

            case "pay":
                try: 
                    amount = int(args[0])
                except:
                    print(yellow("Not a valid amount"))
                    continue

                uid, credit = pay(amount)
                if credit < 0:
                    print(yellow("Not enough credit"))
                    continue

                print(f"New credit: {credit}")

            case "debug":
                verbose = not verbose
                print(gray(f"Debuggin is {('on' if verbose else 'off')}"))

            case other:
                print("Unknown command")

if __name__=="__main__":
    main()
