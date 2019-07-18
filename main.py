import random as rnd


class Game:
   def __init__(self, width=5, height=5, num_mines=3):
       self.board = [[0 for j in range(height)]for i in range(width)]
       # установка мин
       for i in range(num_mines):
           self.board[rnd.randrange(width, height)] = 'X'












my_game = Game()