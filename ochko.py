from class2 import Car, EngineeringCar

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

#Функция, которая принимает ID машины и выводит ее информацию.
    def show_car_info(car_id, car_dict):
        if car_id in car_dict:
           car = car_dict[car_id]
        if isinstance(car, Car):
             print(f"Общая информация о машине {car_id}:")
             print(f"Марка: {car.brand}")
             print(f"Год выпуска: {car.year}")
             print(f"Страна производства: {car.country}")
        elif isinstance(car, EngineeringCar):
             print(f"Инженерная машина {car_id}:")
             print(f"Марка: {car.brand}")
             print(f"Год выпуска: {car.year}")
             print(f"Страна производства: {car.country}")
             print(f"Грузоподъемность: {car.payload_capacity}")
             print(f"Специализация: {car.specialization}")
        else:
          print("Машина с таким ID не найдена.")

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

# Вызов функции для просмотра id машины
car_id_to_show = int(input("Введите ID машины, чтобы посмотреть информацию: "))
show_car_info(car_id_to_show, normal_cars)
show_car_info(car_id_to_show, engineering_cars)