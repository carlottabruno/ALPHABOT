from AlphaBot import AlphaBot

robot = AlphaBot(speed=50)

print("w = Avanti | s = Indietro | a = Sinistra | d = Destra")
print("spazio = Stop | q = Esci")

while True:
    comando = input("Inserisci comando: ").strip().lower()

    if comando == 'w':
        robot.forward()
    elif comando == 's':
        robot.backward()
    elif comando == 'a':
        robot.left()
    elif comando == 'd':
        robot.right()
    elif comando == '' or comando == ' ':
        robot.stop()
    elif comando == 'q':
        robot.stop()
        break
    else:
        print("Comando non valido!")

robot.cleanup()