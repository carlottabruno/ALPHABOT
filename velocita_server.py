# setSpeed no --> increaseSpeed

import socket
from AlphaBot import AlphaBot

HOST = "0.0.0.0"
PORTA = 5000
BUFFER_SIZE = 1024

speed = 50
robot = AlphaBot(speed=speed)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((HOST, PORTA))
s.listen(1)

print("Server AlphaBot attivo...")

connessione, indirizzo_client = s.accept()
print(f"Connesso a: {indirizzo_client}")

try:
    while True:
        dati = connessione.recv(BUFFER_SIZE)

        if not dati:
            break

        comando = dati.decode("utf-8")

        for c in comando:
            print("Comando:", c)

            if c == 'w':
                robot.forward()

            elif c == 's':
                robot.backward()

            elif c == 'a':
                robot.left()

            elif c == 'd':
                robot.right()

            elif c == 'e':
                # Aumenta la velocità di 10 fino a un massimo di 100
                speed = min(100, speed + 10)
                robot.setSpeed(speed)
                print(f"Nuova velocità: {speed}")

            elif c == 'r':
                # Riduce la velocità di 10 fino a un minimo di 0
                speed = max(0, speed - 10)
                robot.setSpeed(speed)
                print(f"Nuova velocità: {speed}")

            elif c == 'x':
                robot.stop()

            elif c == 'q':
                print("Chiusura...")
                break

        if 'q' in comando:
            break

finally:
    robot.stop()
    robot.cleanup()
    connessione.close()
    s.close()
    print("Server chiuso.")