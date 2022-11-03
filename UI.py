import PySimpleGUI as sg
import processing

# async def ui():
#     A = 1
#     B = 0



#     Management_layout = [[sg.Text("Managemant Terminal")], [sg.Button("Register")], [sg.Button("Quit")]]
#     Client_layout = [[sg.Text("Client Terminal")], [sg.Button("Transaction")], [sg.Button("Show Balance")],[sg.Button("Quit")]]
#     Startup_layout = [[sg.Text("Select")], [sg.Button("Management")], [sg.Button("Client")], [sg.Button("Quit")]]

#     # Create the window
#     window = sg.Window("UT-Pay", Startup_layout , margins = (400,200))
#     while A == 1:
#         event, values = window.read()
#         if event == "Management":
#             window.close()
#             window = sg.Window("UT-Pay", Management_layout , margins = (400,200))
#             B = 1
#             break
#         if event == "Client": 
#             window.close()
#             window = sg.Window("UT-Pay", Client_layout , margins = (400,200))
#             B = 1
#             break
#         if event == sg.WIN_CLOSED or event == "Quit":
#             A = 0
#             window.close()


#     while B == 1:
 
#         event, values = window.read()
#         # End program if user closes window or
#         # presses the OK button
#         if event == "Transaction":
#             res = await WebsocketInterface.Transaction('Milk',20,'Dirk','oooo')
#             print(json.dumps(res, indent=4))
#         if event == "Show Balance":
#             res = await WebsocketInterface.Balance('Dirk')
#             print(res['result'])
#         if event == "Register":
#             res = await WebsocketInterface.Register('Weersink')
            
#         if event == sg.WIN_CLOSED or event == "Quit":
#             B = 0
#     window.close()

## asyncio.run(ui())

# def start_up_ui():
#     layout = [[sg.Image(filename = "campus_payment_brighter_1.png", size = (600, 200), background_color= '#ffffff')],[sg.Text("Select from the buttons below:", text_color='#000000', justification = 'center', background_color = '#ffffff', font='bold')], [sg.Button(button_text="Management", button_color = '#000000', mouseover_colors = '#303030')], [sg.Button("Client", button_color = '#000000', mouseover_colors = '#303030')], [sg.VPush(background_color='#ffffff')],[sg.Push(background_color='#ffffff'), sg.Button("Quit", button_color = '#000000', mouseover_colors = '#303030')]]
#     window = sg.Window("UT-Pay", layout , size = (800,400), background_color = "#ffffff", element_justification= 'center')
#     while True:
#         event, values = window.read()
#         if event == "Management":
#             window.close()
#             log_in_ui()
#             break
#         if event == "Client": 
#             window.close()
#             client_ui()
#             break
#         if event == sg.WIN_CLOSED or event == "Quit":
#             window.close()
#             break
# def log_in_ui():
#     layout = [[sg.Image(filename = "campus_payment_brighter_1.png", size = (600, 200), background_color= '#ffffff')],[sg.Text("Please log in first:", text_color='#000000', justification = 'center', background_color = '#ffffff', font='bold')], [sg.Input()], [sg.Button("Enter", button_color = '#000000', mouseover_colors = '#303030')], [sg.VPush(background_color='#ffffff')],[sg.Button("Back", button_color = '#000000', mouseover_colors = '#303030'), sg.Push(background_color='#ffffff'), sg.Button("Quit", button_color = '#000000', mouseover_colors = '#303030')]]
#     window = sg.Window("UT-Pay", layout , size = (800,400), background_color = "#ffffff", element_justification= 'center')
#     while True:
#         event, values = window.read()
#         if event == "Enter":
#             password = str(values)
#             password = password[5:-2]
#             if password == 'TEST':
#                 window.close()
#                 management_ui()
#                 break
#         if event == "Back":
#             window.close()
#             start_up_ui()
#             break
#         if event == "Quit" or event == sg.WIN_CLOSED:
#             window.close()
#             break
# def management_ui():
#     layout = [[sg.Image(filename = "campus_payment_brighter_1.png", size = (600, 200), background_color= '#ffffff')],[sg.Text("Management Terminal", text_color='#000000', justification = 'center', background_color = '#ffffff', font='bold')], [sg.Button("Register", button_color = '#000000', mouseover_colors = '#303030')],[sg.VPush(background_color='#ffffff')], [sg.Button("Back", button_color = '#000000', mouseover_colors = '#303030'), sg.Push(background_color='#ffffff'), sg.Button("Quit", button_color = '#000000', mouseover_colors = '#303030')]]
#     window = sg.Window("UT-Pay", layout , size = (800,400), background_color = "#ffffff", element_justification= 'center')
#     while True:
#         event, values = window.read()
#         if event == "Register":
#             window.close()
#             register_ui()
#             break
#         if event == "Back":
#             window.close()
#             start_up_ui()
#             break
#         if event == "Quit" or event == sg.WIN_CLOSED:
#             window.close()
#             break

def client_ui():
    layout = [[sg.Image(filename = "campus_payment_brighter_1.png", size = (600, 200), background_color= '#ffffff')],[sg.Text("Client Terminal", text_color='#000000', justification = 'center', background_color = '#ffffff', font='bold')], [sg.Button("Transaction", button_color = '#000000', mouseover_colors = '#303030')], [sg.Button("Register / Read", button_color = '#000000', mouseover_colors = '#303030')], [sg.VPush(background_color='#ffffff')], [sg.Push(background_color='#ffffff'), sg.Button("Quit", button_color = '#000000', mouseover_colors = '#303030')]]
    window = sg.Window("UT-Pay", layout , size = (800,400), background_color = "#ffffff", element_justification= 'center')
    while True:
        event, values = window.read()
        if event == "Transaction":
            window.close()
            transaction_ui()
            break
        if event == "Register / Read":
            window.close()
            scan_balance_ui()
            break
        if event == "Quit" or event == sg.WIN_CLOSED:
            window.close()
            break

# def register_ui():
#     layout = [[sg.Image(filename = "campus_payment_brighter_1.png", size = (600, 200), background_color= '#ffffff')],[sg.Text("Please Register Here:", text_color='#000000', justification = 'center', background_color = '#ffffff', font='bold')], [sg.Button("Scan", button_color = '#000000', mouseover_colors = '#303030')], [sg.VPush(background_color='#ffffff')],[sg.Button("Back", button_color = '#000000', mouseover_colors = '#303030'),sg.Push(background_color='#ffffff'), sg.Button("Quit", button_color = '#000000', mouseover_colors = '#303030')] ]
#     window = sg.Window("UT-Pay", layout , size = (800,400), background_color = "#ffffff", element_justification= 'center')
#     while True:
#         event, values = window.read()
#         if event == "Scan":
#             uid = processing.get_rfid()
#             processing.register(uid)
#             success_register_ui(uid)
#             window.close()
#             break
#         if event == "Back":
#             client_ui()
#             window.close()
#             break
#         if event == sg.WIN_CLOSED or event == "Quit":
#             window.close()
#             break 

# def success_register_ui(uid):
#     layout = [[sg.Image(filename = "campus_payment_brighter_1.png", size = (600, 200), background_color= '#ffffff')],[sg.Text(f"Registred successfully: {uid}", text_color='#000000', justification = 'center', background_color = '#ffffff', font='bold')], [sg.VPush(background_color='#ffffff')],[sg.Button("Home", button_color = '#000000', mouseover_colors = '#303030'),sg.Push(background_color='#ffffff'), sg.Button("Quit", button_color = '#000000', mouseover_colors = '#303030')] ]
#     window = sg.Window("UT-Pay", layout , size = (800,400), background_color = "#ffffff", element_justification= 'center')
#     while True:
#         event, values = window.read()
#         if event == "Home":
#             client_ui()
#             window.close()
#             break
#         if event == "Quit" or event == sg.WIN_CLOSED:
#             window.close()
#             break


def transaction_ui():
    layout = [[sg.Image(filename = "campus_payment_brighter_1.png", size = (600, 200), background_color= '#ffffff')],[sg.Text("Set the transaction amount", text_color='#000000', justification = 'center', background_color = '#ffffff', font='bold')], [sg.Input()], [sg.Button("Scan", button_color = '#000000', mouseover_colors = '#303030')], [sg.VPush(background_color='#ffffff')], [sg.Button("Back", button_color = '#000000', mouseover_colors = '#303030'), sg.Push(background_color='#ffffff'), sg.Button("Quit", button_color = '#000000', mouseover_colors = '#303030')]]
    window = sg.Window("UT-Pay", layout , size = (800,400), background_color = "#ffffff", element_justification= 'center')
    while True:
        event, values = window.read()
# {0: 'Test'}
        if event == "Scan":
            amount = str(values)
            amount = amount[5:-2]
            # amount = values[0]
            print(amount)
            uid, result = processing.pay(int(amount))
            if result >= 0:
                window.close()
                transaction_succesfull_uir(uid, result)
                break
            elif result < 0:
                window.close()
                credit = processing.getcredit(uid)
                transaction_failed_ui(uid, credit)
                break
        if event == "Back":
            window.close()
            client_ui()
            break
        if event == "Quit" or event == sg.WIN_CLOSED:
            window.close()
            break


def scan_balance_ui():
    layout = [[sg.Image(filename = "campus_payment_brighter_1.png", size = (600, 200), background_color= '#ffffff')],[sg.Text("Scan to check your balance", text_color='#000000', justification = 'center', background_color = '#ffffff', font='bold')], [sg.Button("Scan", button_color = '#000000', mouseover_colors = '#303030')], [sg.VPush(background_color='#ffffff')], [sg.Button("Back", button_color = '#000000', mouseover_colors = '#303030'), sg.Push(background_color='#ffffff'), sg.Button("Quit", button_color = '#000000', mouseover_colors = '#303030')]]
    window = sg.Window("UT-Pay", layout , size = (800,400), background_color = "#ffffff", element_justification= 'center')
    while True:
        event, values = window.read()
        if event == "Scan":
            uid, credit = processing.read()
            window.close()
            show_balance_ui(uid, credit)
            break
        if event == "Back":
            window.close()
            client_ui()
            break
        if event == "Quit" or event == sg.WIN_CLOSED:
            window.close()
            break
        
            
def show_balance_ui(uid, amount):
    layout = [[sg.Image(filename = "campus_payment_brighter_1.png", size = (600, 200), background_color= '#ffffff')], [sg.Text(f"UID: {uid}", text_color='#000000', justification = 'center', background_color = '#ffffff', font='bold')], [sg.Text(f"Balance: {amount}", text_color='#000000', justification = 'center', background_color = '#ffffff', font='bold')], [sg.VPush(background_color='#ffffff')], [sg.Button("Home", button_color = '#000000', mouseover_colors = '#303030'), sg.Push(background_color='#ffffff'), sg.Button("Quit", button_color = '#000000', mouseover_colors = '#303030')]]
    window = sg.Window("UT-Pay", layout , size = (800,400), background_color = "#ffffff", element_justification= 'center')
    while True:
        event, values = window.read()
        if event == "Home":
            window.close()
            client_ui()
            break
        if event == "Quit" or event == sg.WIN_CLOSED:
            window.close()
            break


def transaction_succesfull_ui(uid, amount):
    layout = [[sg.Image(filename = "campus_payment_brighter_1.png", size = (600, 200), background_color= '#ffffff')], [sg.Text("Transaction Succesfull", text_color='#000000', justification = 'center', background_color = '#ffffff', font='bold')], [sg.Text(f"UID: {uid}", text_color='#000000', justification = 'center', background_color = '#ffffff', font='bold')], [sg.Text(f"Balance: {amount}", text_color='#000000', justification = 'center', background_color = '#ffffff', font='bold')], [sg.Button("Okay", button_color = '#000000', mouseover_colors = '#303030')]] 
    window = sg.Window("UT-Pay", layout , size = (800,400), background_color = "#ffffff", element_justification= 'center')
    while True:
        event, values = window.read()
        if event == "Okay":
            window.close()
            transaction_ui()
            break
        if event == sg.WIN_CLOSED:
            window.close()
            break


def transaction_failed_ui(uid, amount):
    layout = [[sg.Image(filename = "campus_payment_brighter_1.png", size = (600, 200), background_color= '#ffffff')],[sg.Text("Transaction Failed", text_color='#000000', justification = 'center', background_color = '#ffffff', font='bold')], [sg.Text(f"UID: {uid}", text_color='#000000', justification = 'center', background_color = '#ffffff', font='bold')], [sg.Text(f"Balance: {amount}", text_color='#000000', justification = 'center', background_color = '#ffffff', font='bold')], [sg.Button("Okay", button_color = '#000000', mouseover_colors = '#303030')]] 
    window = sg.Window("UT-Pay", layout , size = (800,400), background_color = "#ffffff", element_justification= 'center')
    while True:
        event, values = window.read()
        if event == "Okay":
            window.close()
            transaction_ui()
            break
        if event == sg.WIN_CLOSED:
            window.close()
            break
        

client_ui()