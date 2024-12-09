import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power, enemy_count = 100):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemy_count = enemy_count

    def run(self):
        print(f'{self.name}, на нас напали!')
        day_count = 0
        while self.enemy_count > 0:
            self.enemy_count -= self.power
            day_count += 1
            print(f'{self.name} сражается {day_count} дней, осталось {self.enemy_count} войнов.')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {day_count} дней(дня)')

first_knight = Knight('Сир Ланцелот', 10)
second_knight = Knight('Сир Галахад', 20)
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")