import socket 

IP_PORTA = ("192.168.1.116", 22)
BUFFER = 4096

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(IP_PORTA)
    print("Server in ascolto...")
    s.listen()
    connessione, _ = s.accept()

    while True:
        dati = connessione.recv(BUFFER)
        print(f"Ricevuto: {dati.decode()}")

        if dati.decode().lower() == "exit":
            break

    connessione.close()

if __name__ == "__main__":
    main()