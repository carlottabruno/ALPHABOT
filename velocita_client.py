import socket
from pynput import keyboard

SERVER_IP = "192.168.0.130"
SERVER_PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_IP, SERVER_PORT))

tasto_premuto = None

print("=== CONTROLLO ALPHABOT ===")
print("W = Avanti | S = Indietro | A = Sinistra | D = Destra")
print("E = Aumenta velocità (+10)")
print("R = Riduci velocità (-10)")
print("Rilascio tasto direzione = Stop")
print("ESC = Esci")

def invia(comando):
    try:
        s.sendall(comando.encode("utf-8"))
    except:
        pass

def on_press(key):
    global tasto_premuto

    try:
        nuovo_tasto = key.char.lower()
    except AttributeError:
        nuovo_tasto = None

    if key == keyboard.Key.esc:
        invia('q')
        return False

    # Aggiunti 'e' ed 'r'
    if nuovo_tasto in ['w', 's', 'a', 'd', 'e', 'r']:
        if nuovo_tasto != tasto_premuto:
            tasto_premuto = nuovo_tasto
            invia(nuovo_tasto)

def on_release(key):
    global tasto_premuto

    try:
        tasto = key.char.lower()
    except AttributeError:
        tasto = None

    # Applichiamo lo stop automatico solo ai tasti di movimento
    if tasto in ['w', 's', 'a', 'd'] and tasto == tasto_premuto:
        tasto_premuto = None
        invia('x')
    elif tasto in ['e', 'r']:
        tasto_premuto = None

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()

s.close()
print("Connessione chiusa.")