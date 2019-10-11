class Game():

    class Player(Game):
        def __init__(self, name, gamepiece):
            self.name = name
            self.gamepiece = gamepiece

    class Board(Game, Player):
        def __init__(self):

        

    class Move(Board)