class CarModels:
    def __init__(self, model, year, color, exchange, turbo: bool):
        self.model = model
        self.year = year
        self.color = color
        self.exchange = exchange
        self.turbo = turbo

    def __repr__(self):
        return f"{[self.model, self.year, self.color, self.exchange, self.turbo]}"

    def savetxt(self, x):
        with open("cars.txt", "a") as arquivo:
            arquivo.write(x)


tetse = CarModels(2, 3, 4, 5, False)
tetse.savetxt("oi")
