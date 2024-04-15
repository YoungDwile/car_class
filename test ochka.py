import openpyxl 

# создание класса 
class Car:
    def __init__(self, car_id, year, country, brand):
        self.car_id = car_id
        self.year = year
        self.country = country
        self.brand = brand

class EngineeringCar(Car):
    def __init__(self, car_id, year, country, brand, payload_capacity, specialization):
        super().__init__(car_id, year, country, brand)
        self.payload_capacity = payload_capacity
        self.specialization = specialization

# функция сохранения в эксель 
def save_to_excel(car_list, file_name):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["ID", "Year", "Country", "Brand", "Payload Capacity", "Specialization"])

    for car in car_list:
        ws.append([car.car_id, car.year, car.country, car.brand, car.payload_capacity, car.specialization])

    wb.save(file_name)
    print(f"Данные успешно сохранены в файл {file_name}")

def add_car(car_id):
    year = input("Введите год выпуска машины: ")
    country = input("Введите страну производства: ")
    brand = input("Введите марку машины: ")
    payload_capacity = input("Введите грузоподъемность: ")
    specialization = input("Введите специализацию: ")

    car = EngineeringCar(car_id, year, country, brand, payload_capacity, specialization)
    return car

# найти по id 
def find_car_by_id(car_list, car_id):
    for car in car_list:
        if car.car_id == car_id:
            return car

    return None

# Пример использования
car_list = []
next_id = 1

while True:
    user_input = input("Хотите добавить новую машину? (да/нет): ")
    if user_input.lower() != 'да':
        break

    new_car = add_car(next_id)
    car_list.append(new_car)
    next_id += 1

save_to_excel(car_list, "user_cars_data.xlsx")

# Поиск машины по ID
search_id = int(input("Введите ID машины для поиска: "))
found_car = find_car_by_id(car_list, search_id)

if found_car:
    print(f"Машина найдена - Марка: {found_car.brand}, Год выпуска: {found_car.year}")
else:
    print("Машина не найдена.")