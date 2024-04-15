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

# Создание хэш-таблиц для обычных и инженерных машин
normal_cars = {}
engineering_cars = {}

car_id = 1

#Цикл добавления машин
while True:
    car_type = input("Выберите тип машины (обычная / инженерная): ")
    if car_type.lower() == 'обычная':
        year = input("Введите год выпуска: ")
        country = input("Введите страну выпуска: ")
        brand = input("Введите марку: ")
        car = Car(year, country, brand)
        normal_cars[car_id] = car
    elif car_type.lower() == 'инженерная':
        year = input("Введите год выпуска: ")
        country = input("Введите страну выпуска: ")
        brand = input("Введите марку: ")
        payload_capacity = input("Введите грузоподъемность: ")
        specialization = input("Введите специализацию: ")
        engineering_car = EngineeringCar(year, country, brand, payload_capacity, specialization)
        engineering_cars[car_id] = engineering_car
    else:
        print("Неверный тип машины. Попробуйте снова.")

# хочет ли пользователь посмотреть кол-во машин
    view_choice = input(
        "Хотите просмотреть количество добавленных машин, уникальные бренды и специализации? (да или нет): ")
    if view_choice.lower() == "да":
        break

    continue
    car_id += 1



# Вывод кол-ва машин
total_cars = len(normal_cars) + len(engineering_cars)
unique_brands = set([car.brand for car in normal_cars.values()] + [car.brand for car in engineering_cars.values()])
unique_specializations = set([car.specialization for car in engineering_cars.values()])
print("-----------------------------------------------------")
print(f"Общее количество добавленных машин: {total_cars} ")
print("-----------------------------------------------------")
print(f"Уникальные марки машин: {', '.join(unique_brands)} ")
print("-----------------------------------------------------")
print(f"Уникальные специализации инженерных машин: {', '.join(unique_specializations)} ")
print("-----------------------------------------------------")
