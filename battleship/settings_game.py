from string import ascii_uppercase


class SettingsGame:
    def __init__(self):
        self.matrix = []
        self.vessels = []
        self.jogador = input('Digite seu nome: ')

    def generating_matrix(self):
        column = []
        row = []
        for x in range(10):
            for y in range(10):
                row.append(['🌊 ' + ascii_uppercase[x] + str(y + 1) + ' 🌊'])
            column.append(row.copy())
            row.clear()
        self.matrix = column.copy()
        return self.matrix

    def exibe_matrix(self):
        for each in self.matrix:
            print(each)

    def option_embarcacoes(self):
        available_vessels = ['Aircraft Carrier', 'Battleship', 'Cruiser',
                             'Destroyer', 'Destroyer', 'Submarines', 'Submarines']
        option_vessels = ['1', 'Aircraft Carrier', 5], ['2', 'Battleship', 4], \
                         ['3', 'Cruiser', 3], ['4', 'Destroyer', 2], ['5', 'Submarines', 1]

        while len(available_vessels) > 0:
            vessel = input('[ 1 ] - Aircraft Carrier\n'
                           '[ 2 ] - Battleship\n'
                           '[ 3 ] - Cruiser\n'
                           '[ 4 ] - Destroyer\n'
                           '[ 5 ] - Submarines\n'
                           'Digite o numero da embarcação desejada: ')

            position = input('Posição da embarcação: ').upper()
            for i in range(len(option_vessels)):
                if vessel in option_vessels[i]:
                    lista = [option_vessels[i][1]]
                    lista.append(position)
                    lista.append(option_vessels[i][2])
                    self.vessels.append(lista)
                    option = option_vessels[i][1]
                    available_vessels.remove(option)

    def posiciona_embarcacoes(self):
        for l in range(9):
            for c in range(9):
                for i in self.vessels:
                    if i[1] in self.matrix[l][c][0]:
                        for p in range(i[2]):
                            self.matrix[l][c + p] = [i[0]]

    def chama_tudo(self):
        self.generating_matrix()
        self.exibe_matrix()
        self.option_embarcacoes()
        self.posiciona_embarcacoes()
        self.exibe_matrix()
