import random as rnd


class Game:

    def __init__(self, width=5, height=5, num_mines=3):
        self.GameOver = False
        self.width = width
        self.height = height
        self.board = [[0 for j in range(height)]for i in range(width)]
        self.opened = []
        # установка мин
        for i in range(num_mines):
            self.board[rnd.randrange(0, width)][rnd.randrange(0, height)] = 'X'
        # пройтись по всем клеткам, установить цифры мин вокруг
        for i in range(self.height):
            for j in range(self.width):
                around_mines = 0
                if i > 0:
                    if self.board[i - 1][j] == 'X':
                        around_mines += 1
                if i < self.height - 1:
                    if self.board[i + 1][j] == 'X':
                        around_mines += 1
                if j > 0:
                    if self.board[i][j - 1] == 'X':
                        around_mines += 1
                if j < self.width - 1:
                    if self.board[i][j + 1] == 'X':
                        around_mines += 1
                if self.board[i][j] != 'X':
                    self.board[i][j] = around_mines


    def paint(self):
        for i in range(self.height):
            for j in range(self.width):
                # если клетки нет в открытых
                if (i, j) in self.opened:
                    print('[ ]', end=' ')
                else:
                    print(' {} '.format(self.board[i][j]), end=' ')
            # перевод строки
            print('')


    def play(self):
        # цикл продолжается пока не конец игры
        while self.GameOver is False:
            self.paint()
            # ввод команды
            inp = input('Что открыть? (e - выход): ')
            inp = inp.lower()  # к нижнему регистру
            if inp == 'e':
                self.GameOver = True










my_game = Game(10, 10, 6)
my_game.play()