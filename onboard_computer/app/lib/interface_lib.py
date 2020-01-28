import os


class OptionsGame:
    def __init__(self, select_interface_options):
        self.select_interface_options = select_interface_options

    def panel_the_game(self):
        print('[ 1 ] - Play\n[ 2 ] - Leave\n')
        self.select_interface_options = input('Me: ')
        if self.select_interface_options == '1':
            print('Working...')
        if self.select_interface_options == '2':
            pass

