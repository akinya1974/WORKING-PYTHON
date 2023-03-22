
# НАСЛЕДОВАНИЕ
# ИНКАПСУЛЯЦИЯ
# ПОЛИМОРФИЗМ

from random import randint


class MechanismOptions:
    def beep(self):
        print('Звуковой сигнал - ААААААА')


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
            if self._check_status():
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
        if self._check_status():
            self.current_status = self.status_stop
            print(f'Машина остановлена, текущий уровень топлива - {self.fuel_level}')
            return
        print('Машина уже остановлена')
        return

    def _check_fuel_level(self, fuel_quantity):
        return  self.fuel_level + fuel_quantity <= self.fuel_tank

    def add_fuel(self, fuel_type, fuel_quantity):
        if fuel_type != self.fuel_type:
            print('Этот тип топлива не подходит')
            return
        if not self._check_fuel_level(fuel_quantity):
            print(f'Много топлива, Текущий уровень  - {self.fuel_level} Максимальный - {self.fuel_tank}')
            return
        self.fuel_level = self.fuel_level + fuel_quantity
        print(f'Бак заправлен, сейчас есть {self.fuel_level}')
        return

    def _check_status(self):
        return self.current_status == self.status_work


    def get_status(self):
        print(f'Машина {self.work_type} сейчас - {self.current_status}, Уровень топлива - {self.fuel_level}')
        return


class NewMechanism(Mechanism, MechanismOptions):
    def start(self):
        # super().start()
        # self.beep()
        if self.fuel_level > 0:
            if self._check_status():
                print('Не могу завести машину она работает')
                return
            else:
                self.current_status = self.status_work
                self.fuel_level = self.fuel_level - 5
            print('Машина заведена')
            self.beep()
            return
        else:
            print('Нет топлива используйте комманду add_fuel')
            return

    def get_status(self):
            print('Нет данных')
            return

    def __str__(self):
        return f'{self.work_type}'


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
    data.append(NewMechanism(name, fuel, fuel_tank))

for i in data:
    i.add_fuel(i.fuel_type, randint(1, 10))

# for i in data:
#     print(i.fuel_level)

def calk(data_list: list):
    if not data_list:
        return 0
    quantity = len(data_list)
    fuel = 0
    for i in data_list:
        fuel += i.fuel_level

    result = fuel / quantity
    return result

print(calk(data))



# for i in data:
#     i.add_fuel(i.fuel_type, 30)

# for i in data:
#     i.start()
#     i.get_status()
#     i.stop()
#     i.get_status()
#
# for i in data:
#     print(i)


