# Создание класса
class Car:
    def __init__(self, year, country, brand):
        self.year = year
        self.country = country
        self.brand = brand

class EngineeringCar(Car):
    def __init__(self, year, country, brand, payload_capacity, specialization):
        super().__init__(year, country, brand)
        self.payload_capacity = payload_capacity
        self.specialization = specialization