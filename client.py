import socket
from pynput import keyboard

SERVER_IP = "192.168.0.130"
SERVER_PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_IP, SERVER_PORT))

tasto_premuto = None

print("=== CONTROLLO ALPHABOT ===")
print("W = Avanti")
print("S = Indietro")
print("A = Sinistra")
print("D = Destra")
print("Rilascio tasto = Stop")
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

    if nuovo_tasto in ['w', 's', 'a', 'd']:
        if nuovo_tasto != tasto_premuto:
            tasto_premuto = nuovo_tasto
            invia(nuovo_tasto)

def on_release(key):
    global tasto_premuto

    try:
        tasto = key.char.lower()
    except AttributeError:
        tasto = None

    if tasto == tasto_premuto:
        tasto_premuto = None
        invia('x')

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()

s.close()
print("Connessione chiusa.")
