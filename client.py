import socket

SERVER_IP = "192.168.1.116"
SERVER_PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_IP, SERVER_PORT))

print(" w + Invio : Avanti")
print(" s + Invio : Indietro")
print(" a + Invio : Sinistra")
print(" d + Invio : Destra")
print(" SPAZIO + Invio : Stop")
print(" q + Invio : Esci")

while True:
    comando = input("Inserisci comando: ").strip().lower()

    if comando in ['w', 's', 'a', 'd', ' ', 'q']:
        s.sendall(comando.encode('utf-8'))
        if comando == 'q':
            break
    else:
        print("Comando non valido!")

s.close()
print("Connessione chiusa.")