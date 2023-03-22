
class Mechanism:
    mass = 0
    status_work = 'Заведена'
    status_stop = 'Остановлена'
    current_status = status_stop
    fuel_level = 0  # ЛИТРЫ

    def __init__(self, work_type, fuel_type, fuel_tank):
        self.work_type = work_type
        self.fuel_type = fuel_type
        self.fuel_tank = fuel_tank


    def start(self):
        if self.fuel_level > 0:
            if self.check_status():
                print('Не могу завести машину она работает')
                return
            else:
                self.current_status = self.status_work
                self.fuel_level = self.fuel_level - 5
            print('Машина заведена')
            return
        else:
            print('Нет топлива используйте комманду add_fuel')
            return

    def stop(self):
        if self.check_status():
            self.current_status = self.status_stop
            print(f'Машина остановлена, текущий уровень топлива - {self.fuel_level}')
            return
        print('Машина уже остановлена')
        return

    def check_fuel_level(self, fuel_quantity):
        return  self.fuel_level + fuel_quantity <= self.fuel_tank

    def add_fuel(self, fuel_type, fuel_quantity):
        if fuel_type != self.fuel_type:
            print('Этот тип топлива не подходит')
            return
        if not self.check_fuel_level(fuel_quantity):
            print(f'Много топлива, Текущий уровень  - {self.fuel_level} Максимальный - {self.fuel_tank}')
            return
        self.fuel_level = self.fuel_level + fuel_quantity
        print(f'Бак заправлен, сейчас есть {self.fuel_level}')
        return

    def check_status(self):
        return self.current_status == self.status_work


    def get_status(self):
        print(f'Машина {self.work_type} сейчас - {self.current_status}, Уровень топлива - {self.fuel_level}')
        return

fixture = [
            {
                'name': 'сеялка',
                'fuel': 'бензин',
                'fuel_tank': 50
            },
            {
                'name': 'генератор',
                'fuel': 'газ',
                'fuel_tank': 100
            }
    ]
data = []
for item in fixture:
    name, fuel, fuel_tank = item.values()
    data.append(Mechanism(name, fuel, fuel_tank))

# date = []
# for i in range(4):
#     date.append(Mechanism('сеялка', 'бензин', 100 ))


mechanism_1 = Mechanism('сеялка', 'бензин', 100)
mechanism_1.add_fuel('бензин', 50)
mechanism_1.start()
mechanism_1.get_status()
mechanism_1.stop()
mechanism_1.start()
mechanism_1.get_status()
mechanism_1.stop()

mechanism_2 = Mechanism('генератор', 'газ', 200)
mechanism_2.add_fuel('газ', 100)
mechanism_2.start()
mechanism_2.get_status()
mechanism_2.stop()
mechanism_2.start()
mechanism_2.get_status()
mechanism_2.stop()



