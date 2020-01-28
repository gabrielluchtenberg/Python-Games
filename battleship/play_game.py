class Play:
    def __init__(self, matrix, vessel1, vessel2, matrix1, matrix2, jogador1, jogador2):
        self.vessel1 = vessel1
        self.vessel2 = vessel2
        self.matrix1 = matrix1
        self.matrix2 = matrix2
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.matrix = matrix

    def jogadas_player1(self):
        condicao = True
        while condicao:
            jogada = input(f'Jogada {self.jogador1}\n >> ')
            for i in self.vessel2:
                if jogada in i:
                    for l in range(9):
                        for c in range(9):
                            # print('i:', i, '         l:', l, '          c:', c)
                            if jogada in self.matrix[l][c][0]:
                                self.matrix2[l][c] = ['Explodiu']
                condicao = False

    def jogadas_player2(self):
        condicao = True
        while condicao:
            jogada = input(f'Jogada {self.jogador2}\n >> ')
            for i in self.vessel2:
                if jogada in i:
                    for l in range(9):
                        for c in range(9):
                            if jogada in self.matrix[l][c][0]:
                                self.matrix2[l][c] = ['Explodiu']
                condicao = False

    def execute_game(self):
        while True:
            self.jogadas_player1()
            for each in self.matrix2:
                print(each)
            if self.vessel2 == 0:
                return self.jogador1
            self.jogadas_player2()
            for each in self.matrix1:
                print(each)
            if self.vessel1 == 0:
                return self.jogador2
