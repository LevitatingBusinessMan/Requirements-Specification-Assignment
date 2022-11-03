import PySimpleGUI as sg
import processing

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
                transaction_succesfull_ui(uid, result)
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