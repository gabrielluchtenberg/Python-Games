from settings_game import SettingsGame
from play_game import Play


settings = SettingsGame()
settings.chama_tudo()
matrix = settings.generating_matrix()

matrix1 = settings.matrix
vessel1 = settings.vessels
jogador1 = settings.jogador

settings = SettingsGame()
settings.chama_tudo()

matrix2 = settings.matrix
vessel2 = settings.vessels
jogador2 = settings.jogador

play = Play(matrix, vessel1, vessel2, matrix1, matrix2, jogador1, jogador2)
play.execute_game()

if play.execute_game() == jogador1:
    print(f'{jogador1} Venceu!!')

elif play.execute_game() == jogador2:
    print(f'{jogador2} Venceu!!')
