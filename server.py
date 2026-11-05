import socket
from AlphaBot import AlphaBot

HOST = "0.0.0.0"
PORTA = 5000
BUFFER_SIZE = 1024

robot = AlphaBot(speed=50)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((HOST, PORTA))
s.listen(1)
print(f"Server AlphaBot attivo sulla porta {PORTA}...")

connessione, indirizzo_client = s.accept()
print(f"Connessione stabilita con: {indirizzo_client}")

while True:
    dati = connessione.recv(BUFFER_SIZE)
    if not dati:
        break

    comando = dati.decode('utf-8').strip().lower()
    print(f"Comando ricevuto: {comando}")

    if comando == 'w':
        robot.forward()
    elif comando == 's':
        robot.backward()
    elif comando == 'a':
        robot.left()
    elif comando == 'd':
        robot.right()
    elif comando == ' ':
        robot.stop()
    elif comando == 'q':
        print("Chiusura connessione...")
        break

robot.cleanup()
s.close()