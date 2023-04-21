from GameTable import Board
from SaveGame import SaveGame
import sys

# path = os.getcwd()
# html_file=os.path.join("file:///", path,"index.html" )
# print(html_file)

# louncher = webbrowser.get()
# print(louncher)
# louncher.open(html_file, 1, True)


class Main:
    activity = ["1) Let's play!", "2) Revious game results", "3)Load last game", "E) EXIT"]

    def __init__(self) -> None:
        self.choose_task()
        pass

    def choose_task(self):
        user_input = ""
        while user_input != "E":
            print(">>", *Main.activity)
            user_input = input().upper()
            match (user_input):
                case "1":
                    print("<--Tic Tac Toe starts-->")
                    Board()
                case "2":
                    print("<--Previous games results-->")
                case "3":
                    print("<--Load last game-->")
                    self.load_last_game()
                case "E":
                    print("<--Exit game-->")
                    sys.exit(0)

    def load_last_game(self):
        # TODO: initialize players on Board!
        try:
            load_last_game_state = SaveGame.load()
            last_state = load_last_game_state[-1]
            Board(last_state)
        except IndexError as err:
            print("There is no earlier game!")


if __name__ == "__main__":
    Main()
