import random as rnd


class Game:

   def __init__(self, width=5, height=5, num_mines=3):
       self.width = width
       self.height = height
       self.board = [[0 for j in range(height)]for i in range(width)]
       # установка мин
       for i in range(num_mines):
           self.board[rnd.randrange(0, width)][rnd.randrange(0, height)] = 'X'

   def paint(self):
        for i in range(self.width):
            print(i, end=' ')










my_game = Game()
my_game.paint()