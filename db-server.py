#!/usr/bin/env python

import os
from dotenv import dotenv_values

import json
import asyncio
import websockets
import sqlite3
from time import time

from colorama import init, Fore, Back, Style

# Websocket
URI = "0.0.0.0"
PORT = 8765
# Database
DB_FILE = "dev.db"
DB = None
CURSOR = None

async def error(websocket, code, message):
    response = {
        "type" : "error",
        "code" : code,
        "message" : message
    }
    await websocket.send(json.dumps(response))
    await websocket.close()
    print("> Connection closed; Invalid Formatting")

async def handler(websocket):

# Nice print function

    print(
        f'\nIncoming connection; {str(websocket.id)}'
        )

    validated = False

    async for message in websocket:
        
# Load JSON

        try:
            request = json.loads(message)
            type = request['type']
        except:
            await error(websocket, 1, "Invalid Formatting")
            return

        print(json.dumps(request, indent=2))
        
# Client validation

        if type == 'validation':
            env = dotenv_values(".env")
            if env[request['client']] == request['key']:
                validated = True
            else:
                await error(websocket, 69, "Validation key invalid")
            continue
        elif validated == False:
            await error(websocket, 70, "Not validated")
            continue

# Balance

        elif type == 'balance':
            try:
                result = {"balance" : get_balance(request['card'])}
            except:
                result = False

# Execute Transactions

        elif type == 'transaction':

            amount = request['transaction']['amount']
            
            # Get balance of card by 'request['card']'
            balance = get_balance(request['card'])

            if amount <= balance:
                try:
                    CURSOR.execute(f"""
                        UPDATE cards
                        SET
                            balance = {balance - amount}
                        WHERE 
                            key='{request['card']}' 
                    """)
                    CURSOR.execute(f"""
                        INSERT INTO transactions
                        VALUES (
                            '{request['card']}', 
                            {request['transaction']['amount']}, 
                            '{request['transaction']['info']}', 
                            '{request['transaction']['client']}', 
                            {time()}
                            )
                    """)
                    DB.commit()
                    result = True
                except:
                    result = False
            else:
                result = False

# Read Transactions

        elif type == 'read-transactions':
            try:
                res = CURSOR.execute(f"SELECT * FROM transactions WHERE card='{request['card']}'")
                trans = res.fetchall()
                result = trans[:10]
            except:
                error(websocket, 22, "Card Not Registered")

# Register card

        elif type == 'register':
            try:
                CURSOR.execute(f"INSERT INTO cards VALUES ('{request['card']}', 0.0, {time()})")
                result = True
            except:
                error(websocket, 22, "Card Already Registered")

# Get the whole cards database

        elif type == 'getall':
            try:
                res = CURSOR.execute("SELECT * FROM cards")
                result = res.fetchall()
            except:
                result = False

# Send invalid type error

        else:
            error(websocket, 2, "Invalid Type")
            return

# Send response

        response = {
            "type" : "result",
            "request" : request['request'],
            "result" : result
        }

        await websocket.send(json.dumps(response))

# End of connection

    print(f'Connection closed; result, {result}')

def get_balance(key):
    try:
        res = CURSOR.execute(f"SELECT balance FROM cards WHERE key='{key}' ")
        balance = res.fetchone()
        return balance[0]
    except:
        return False

def init(db, cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS 
        cards(
            key, 
            balance, 
            registred,
            PRIMARY KEY (key)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS 
        transactions(
            card, 
            amount,
            info,
            client,
            timestamp,
            PRIMARY KEY (card, amount, client, timestamp)
        )
    """)
    db.commit()

def db_test(db, cursor):
    cursor.execute("INSERT INTO cards VALUES ('Ion', 10.0, 'today')")
    cursor.execute("INSERT INTO cards VALUES ('Dragoș', 10.0, 'today')")
    cursor.execute("INSERT INTO cards VALUES ('Dirk', 10.0, 'today')")
    cursor.execute("INSERT INTO cards VALUES ('Jordy', 10.0, 'today')")
    cursor.execute("INSERT INTO cards VALUES ('Rein', 10.0, 'today')")
    cursor.execute("INSERT INTO cards VALUES ('Vlad', 10.0, 'today')")
    db.commit()

    res = cursor.execute("SELECT * FROM cards")
    return res.fetchall()

async def main():

    print(
        Fore.RED + 
        "\nGroup 46 presents..."
        "\n",
        " ____ ______________     __________               \n",
        "|    |   \__    ___/     \______   \_____  .__.__.\n",
        "|    |   | |    |  ______ |     ___/\__  \ |  |  |\n",
        "|    |   | |    | /_____/ |    |     / __ \|___  |\n",
        "|________| |____|         |____|    (____  / ____|\n",
        "                                         \/\/     \n",
        Fore.RESET
    )

    global DB
    global CURSOR
    DB = sqlite3.connect("dev3.db")
    CURSOR = DB.cursor()
    print(" > Dev Database has been loaded")

    init(DB, CURSOR)
    try:
        res = db_test(DB, CURSOR)
        print(res)
    except:
        print(f"   - Test values already exist in {DB_FILE}")

    # Start websocket
    async with websockets.serve(handler, URI, PORT):
        print(f' > Started websocket server on port; {PORT}')
        await asyncio.Future()  # run forever

asyncio.run(main())