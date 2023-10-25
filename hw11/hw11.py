# Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак",
# "Корабель", наслідувані від "Транспортний засіб".
# Наповніть класи атрибутами та методами на свій розсуд.
# Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".
# Виведіть на екран значення атрибутів обʼєктів
class Vehicle:
    def __init__(self, brand, model, year, weight):
        self.brand = brand
        self.model = model
        self.year = year
        self.weight = weight

    def display_info(self):
        return (f'{self.brand} {self.model}. '
                f'Year: {self.year}, Weight: {self.weight}kg')


class Car(Vehicle):
    def __init__(self, brand, model, year, weight, engine_type):
        Vehicle.__init__(self, brand, model, year, weight)
        self.engine_type = engine_type

    def display_info(self):
        info = Vehicle.display_info(self)
        return info + f', Type engine: {self.engine_type}.'


class Airplane(Vehicle):
    def __init__(self, brand, model, year, weight, wingspan):
        Vehicle.__init__(self, brand, model, year, weight)
        self.wingspan = wingspan

    def display_info(self):
        info = Vehicle.display_info(self)
        return info + f', wingspan: {self.wingspan}m.'


class Ship(Vehicle):
    def __init__(self, brand, model, year, weight, capacity):
        Vehicle.__init__(self, brand, model, year, weight)
        self.capacity = capacity

    def display_info(self):
        info = Vehicle.display_info(self)
        return info + f', capacity: {self.capacity}TEU.'


my_car = Car("Toyota", "Camry", 2020,
             1500, "Petrol")
print(my_car.display_info())

my_plane = Airplane("Boeing", "747", 2000,
                    183500, 64.44)
print(my_plane.display_info())

my_ship = Ship("Maersk", "Triple E", 2015,
               200000000, 20000)
print(my_ship.display_info())
