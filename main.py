import curses
from AlphaBot import AlphaBot

robot = AlphaBot(speed=50)

def main(stdscr):
    stdscr.addstr("W = Avanti\n")
    stdscr.addstr("S = Indietro\n")
    stdscr.addstr("A = Sinistra\n")
    stdscr.addstr("D = Destra\n")
    stdscr.addstr("SPAZIO = Stop\n")
    stdscr.addstr("Q = Esci\n")

    while True:
        tasto = stdscr.getch()

        if tasto == ord('w'):
            robot.forward()
        elif tasto == ord('s'):
            robot.backward()
        elif tasto == ord('a'):
            robot.left()
        elif tasto == ord('d'):
            robot.right()
        elif tasto == ord(' '):
            robot.stop()
        elif tasto == ord('q'):
            break

    robot.cleanup()

curses.wrapper(main)