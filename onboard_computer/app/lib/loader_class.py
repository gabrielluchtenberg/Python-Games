from app.lib.car_functions import CarFunctions


class LoaderSystem:
    def __init__(self, interface_options, options_if_the_car_is_on, options_from_interface):
        self.interface_options = interface_options
        self.options_if_the_car_is_on = options_if_the_car_is_on
        self.options_from_interface = options_from_interface

    def interface_options(self):
        print('1 - Dirigir')
        self.options_from_interface = int(1)
        self.options_from_interface = input('-->  ')
        if self.options_from_interface == '1':
            pass

    def options_if_the_car_is_on(self):
        pass
