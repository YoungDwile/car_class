class Car:
    def __init__(self, year, country, brand):
        self.year = year
        self.country = country
        self.brand = brand


class EngineeringMachine(Car):
    def __init__(self, year, country, brand, carrying_capacity, specialization):
        super().__init__(year, country, brand)
        self.carrying_capacity = carrying_capacity
        self.specialization = specialization


ordinary_cars = {}
engineering_machines = {}
car_id = 1
engineering_machine_id = 1

while True:
    print("Выберите тип машины для добавления: ")
    print("1. Обычное авто")
    print("2. Инженерная машина")
    choice = int(input("Введите свой выбор (1 или 2): "))

    if choice == 1:
        year = input("Укажите год выпуска: ")
        country = input("Укажите страну выпуска:")
        brand = input("Марка автомобиля: ")

        car = Car(year, country, brand)
        ordinary_cars[car_id] = car
        car_id += 1

    elif choice == 2:
        year = input("Укажите год выпуска: ")
        country = input("Укажите страну выпуска: ")
        brand = input("Марка автомобиля: ")
        carrying_capacity = input("Введите грузоподъемность авто: ")
        specialization = input("Введите специализацию: ")

        eng_machine = EngineeringMachine(year, country, brand, carrying_capacity, specialization)
        engineering_machines[engineering_machine_id] = eng_machine
        engineering_machine_id += 1

    else:
        print("Неверный выбор. Пожалуйста, попробуйте снова.")

    view_choice = input("Хотите просмотреть количество добавленных машин, уникальные бренды и специализации? (да или нет): ")
    if view_choice.lower() == "да":
        break

# Отображение количества добавленных машин
print("-----------------------------------------------------")
print(f"Добавлено количество обычных автомобилей: {len(ordinary_cars)}")
print(f"Количество добавленных инженерных машин: {len(engineering_machines)}")


# Отображение уникальных брендов и специализаций
unique_brands = set([car.brand for car in ordinary_cars.values()])
unique_specializations = set([machine.specialization for machine in engineering_machines.values()])

print("-----------------------------------------------------")
print("Уникальные марки обычных автомобилей:")
for brand in unique_brands:
    print(brand)
print("-----------------------------------------------------")

print("-----------------------------------------------------")
print("Уникальные специализации инженерных автомобилей:")
for specialization in unique_specializations:
    print(specialization)
print("-----------------------------------------------------")