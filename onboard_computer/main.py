from app.lib.loader_class import LoaderSystem
from app.lib.car_functions import CarFunctions

appSystem = LoaderSystem
appSystem.interface_options()
appStartSystem = CarFunctions
appStartSystem.turn_on(appStartSystem)
