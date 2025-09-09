class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

car1 = Car("Mazda", "RX7", 2020, "Red")
print(f"Car: {car1.brand} {car1.model}, Year: {car1.year}, Color: {car1.color}")
