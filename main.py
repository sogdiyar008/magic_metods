# # class Point:
# #     def __new__(cls, *args, **kwargs):
# #         print('method new')
# #         return super().__new__(cls)
# #
# #     def __init__(self,x,y):
# #         self.x=x
# #         self.y=y
# #
# #
# # p=Point(2,8)
# # print(p.x)
# import random
# # class DataBase:
# #     __instance=None
# #
# #     def __new__(cls, *args, **kwargs):
# #         if cls.__instance is None:
# #             cls.__instance=super().__new__(cls)
# #         return cls.__instance
# #     def __init__(self, user, password, port):
# #         self.user=user
# #         self.password=password
# #         self.port=port
# #
# #     def __del__(self):
# #         print('rasorvano')
# #         DataBase.__instance
# #
# #     def connect(self):
# #         print(f'соединение c БД: {self.user}, {self.password}, {self.port}')
# #
# #     def close(self):
# #         print('закрытик соединения с БД')
# #
# #     def read(self):
# #         print('чтения данных')
# #
# #     def write(self,data):
# #         print(f'записываем данны {self.data}')
# #
# #
# # bd=DataBase('user1','psw1', 8000)
# # bd2=DataBase('user2','psw2', 82000)
# # print(bd)
# # print(bd2)
# #
# #
# # class Test:
# #
# #
# #     def __str__(self):
# #         return 'test str'
# #
# #
# #
# # t=Test()
# # p=Test
# # r=Test
# # print(t)
# # print(p)
# # print(r)
# #
# #
# # class Clock:
# #     __DAY = 86400
# #
# #     def __init__(self,seconds:int):
# #         if not isinstance(seconds, int):
# #             raise TypeError(' ВВОД ЦЕЛОЕ ЧИСЛО ПРИДУРОК :)')
# #         self.seconds=seconds%self.__DAY
# #
# #
# #     def get_time(self):
# #         s=self.seconds%60
# #         m=self.seconds//60%60
# #         h=self.seconds//(60*60)
# #         return f'{h}:{m}:{s}'
# #
# #     def __eq__(self, other):
# #         if not isinstance(other, (int,Clock)):
# #             raise TypeError('Оператор с права должен иметь тип инт или Клок')
# #         # if isinstance(other, int):
# #         #     other=other
# #         # else:
# #         #     other=self.seconds
# #         sc=other if isinstance(other, int) else other.seconds
# #         return self.seconds==sc
# #
# #     def __lt__(self, other):
# #         if not isinstance(other, (int, Clock)):
# #             raise TypeError("NYPEEEE ERERRRRROOOOOOORRRRRRR")
# #         sc=other if isinstance(other, int) else other.seconds
# #         return self.seconds<sc
# #
# #     def __le__(self, other):
# #         if not isinstance(other, (int, Clock)):
# #             raise TypeError("NYPEEEE ERERRRRROOOOOOORRRRRRR")
# #         sc=other if isinstance(other, int) else other.seconds
# #         return self.seconds<=sc
# #
# #     def __add__(self, other):
# #         if not isinstance(other, (int, Clock)):
# #             raise ArithmeticError('не можем сложить')
# #         sc=other if isinstance(other, int) else other.seconds
# #         return Clock(self.seconds+sc)
# #
# #
# #
# #
# # cl=Clock(899)
# # cl2=Clock(99)
# # cl3=Clock(86)
# #
# # print(cl.get_time())
# # cl=cl+cl2+cl3
# # print(cl.get_time())
# #
# # ##################################################
# # 1111111111111111111111111111111111111111111111111#
# # ##################################################
# # class Pasport:
# #     def __init__(self, first_name,last_name, country, date_of_birth, num_of_passport):
# #         self.first_name=first_name
# #         self.country=country
# #         self.last_name=last_name
# #         self.date_of_birth=date_of_birth
# #         self.num_of_passport=num_of_passport
# #
# #     def print_info(self):
# #         print(f'''
# # Имя: {self.first_name}
# # Фамилие: {self.last_name}
# # Страна: {self.country}
# # ДР: {self.date_of_birth}
# # Номер паспорта: {self.num_of_passport}''')
# #
# #     def __repr__(self):
# #         return (f'name {self.first_name} {self.last_name}, Passport: {self.num_of_passport}')
# #
# #
# # class ForeignPassport(Pasport):
# #     def __init__(self, first_name,last_name, country, date_of_birth, num_of_passport, visa):
# #         super().__init__(first_name,last_name, country, date_of_birth, num_of_passport)
# #         self.visa=visa
# #
# #     def print_info(self):
# #         super().print_info()
# #         print('visa:', self.visa)
# #
# #
# #
# #
# # MFC=[]
# # p=Pasport('Sogdi', 'Bahtiyarov', 'kyrgyzstan', '04,07,2007', '4322 3422')
# # fp=ForeignPassport('Sogdi', 'Bahtiyarov', 'kyrgyzstan', '04,07,2007', '4322 3422', 'russia')
# # MFC.append(p)
# # MFC.append(fp)
# # print(MFC)
# # for item in MFC:
# #     item.print_info()
# #
# #
# # #########################################
# # 2222222222222222222222222222222222222222#
# # #########################################
# #
# # class Equipment:
# #     def __init__(self, name, make, year):
# #         self.name=name
# #         self.make=make
# #         self.year=year
# #
# #     def action(self):
# #         return 'Не определено'
# #
# #     def __str__(self):
# #         return f'{self.name}, {self.make}, {self.year}, can \'{self.action()}\''
# #
# #
# #     def __le__(self, other):
# #         if not isinstance(other, Equipment):
# #             raise TypeError
# #         return self.year<=other.year
# #
# #     def __le__(self, other):
# #         if not isinstance(other, Equipment):
# #             raise TypeError
# #         return self.year<=other.year
# #
# #
# # class Printer(Equipment):
# #     def __init__(self, series, name, make, year):
# #         super().__init__(name, make, year)
# #         self.series=series
# #
# #     def action(self):
# #         return 'печатает с компа на листочек'
# #
# #     def __str__(self):
# #         return f'{self.series}, {self.name}, {self.make}, {self.year}, can \'{self.action()}\''
# #
# # class Scaner(Equipment):
# #     def __init__(self, name, make, year):
# #         super().__init__(name, make, year)
# #
# #     def action(self):
# #         return 'Сканирует в комп'
# #
# # class Xerox(Equipment):
# #     def __init__(self, name, make, year):
# #         super().__init__(name, make, year)
# #
# #     def action(self):
# #         return 'Копирует и печатает'
# #
# #
# #
# # sklad=[]
# # e=Equipment('noname', 'X', 2000)
# # s=Printer('series1','noname1','x1', 2001)
# # x=Xerox('noname', 'X', 2001)
# # sklad.append(e)
# # sklad.append(s)
# # sklad.append(x)
# # e=Equipment('noname', 'X', 2000)
# # s=Printer('series1','noname1','x1', 2001)
# # x=Xerox('noname', 'X', 2001)
# # sklad.append(e)
# # sklad.append(s)
# # sklad.append(x)
# #
# # for item in sklad:
# #     print(item)
#
#
# ####################################
# #3333333333333333333333333333333333#
# ####################################
#
#
# from random import randint
# class Soldier:
#     def __init__(self,name='Noname',health=100):
#         self.name=name
#         self.health=health
#
#     def set_name(self, name):
#         self.name = name
#
#     def make_kick(self, enemy):
#         enemy.health -= randint(10,20)
#         if enemy.health < 0:
#             enemy.health = 0
#         self.health+=randint(5,10)
#         print(f'{self.name} бьет {enemy.name}')
#         print('%s = %d' % (enemy.name, enemy.health))
#         print('за это ',self.name, ' восстановил здоровье до: ', self.health, '\n')
#
# class Battle:
#     def __init__(self,u1,u2):
#         self.u1=u1
#         self.u2=u2
#         self.result = "Сражения не было"
#
#     def battle(self):
#         while self.u1.health > 0 and self.u2.health > 0:
#             n = randint(1, 2)
#             if n == 1:
#                 self.u1.make_kick(self.u2)
#             else:
#                 self.u2.make_kick(self.u1)
#
#         if self.u1.health > self.u2.health:
#             self.result = self.u1.name + " ПОБЕДИЛ"
#         elif self.u2.health > self.u1.health:
#             self.result = self.u2.name + " ПОБЕДИЛ"
#
#     def who_win(self):
#         print(self.result)
#
# first = Soldier('Mr. First',140)
# second = Soldier()
# second.set_name('Mr. Second')
# b = Battle(first,second)
# b.battle()
# b.who_win()

################################
#444444444444444444444444444444#
################################
#Класс «Колода карт»


# import time
# import random
# class Card():
#     NumsList = ["Джокер",'2','3','4','5','6','7','8','9','10',
# 			 "Валет","Дама","Король","Туз"]
#     MastList = ["пик","крестей","бубей","червей"]
#     def __init__(self, i, j):
#         self.Mastb = self.MastList[i-1];
#         self.Num = self.NumsList[j-1];
#
# class DeckOfCards():
#     def __init__(self):
#         self.deck = [None] * 56;
#         k = 0;
#         for i in range(1, 4 + 1):
#             for j in range(1, 14 + 1):
#                 self.deck[k] = Card(i, j);
#                 k += 1;
#
#     def shuffle(self):
#         random.shuffle(self.deck);
#
#     def get(self, i):
#         if 0 <= i <= 55:
#             answer = self.deck[i].Num;
#             answer += " ";
#             answer += self.deck[i].Mastb;
#         else:
#             answer = "В колоде только 56 карт"
#         return answer;
#
# deck = DeckOfCards()
# deck.shuffle()
# while True:
#     n=int(input('Выберите карту из колоды в 56 карт: '))
#     if n<=56 :
#         card = deck.get(n-1)
#         print('Вы взяли карту: ', card, end='.\n')
#     else :
#         print("В колоде только 56 карт")


##################
#5555555555555555#
##################

# class Vector3D:
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def display(self):
#         print(f"({self.x}, {self.y}, {self.z})")
#
#     def read(self):
#         self.x = float(input("Введите x: "))
#         self.y = float(input("Введите y: "))
#         self.z = float(input("Введите z: "))
#
#     def __add__(self, other):
#         return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
#
#     def __sub__(self, other):
#         return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
#
#     def __mul__(self, other):
#         if isinstance(other, Vector3D):
#             # Скалярное произведение
#             return self.x * other.x + self.y * other.y + self.z * other.z
#         else:
#             # Умножение на скаляр
#             return Vector3D(self.x * other, self.y * other, self.z * other)
#
#     def __matmul__(self, other):
#         # Векторное произведение
#         x = self.y * other.z - self.z * other.y
#         y = self.z * other.x - self.x * other.z
#         z = self.x * other.y - self.y * other.x
#         return Vector3D(x, y, z)
#
# # Пример использования
# v1 = Vector3D(4, 1, 2)
# v1.display()
#
# v2 = Vector3D()
# v2.read()
#
# v3 = Vector3D(1, 2, 3)
#
# v4 = v1 + v2
# v4.display()
#
# a = v4 * v3
# print(a)
#
# v4 = v1 * 10
# v4.display()
#
# v4 = v1 @ v3
# v4.display()

##############################################
#66666666666666666666666666666666666666666666#
##############################################



# import math
# class RightTriangle:
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#
#     def increase_side(self, percentage):
#         self.base *= (1 + percentage / 100)
#         self.height *= (1 + percentage / 100)
#
#     def decrease_side(self, percentage):
#         self.base *= (1 - percentage / 100)
#         self.height *= (1 - percentage / 100)
#
#     def calculate_circumcircle_radius(self):
#         hypotenuse = math.sqrt(self.base ** 2 + self.height ** 2)
#         return hypotenuse / 2
#
#     def calculate_perimeter(self):
#         hypotenuse = math.sqrt(self.base ** 2 + self.height ** 2)
#         return self.base + self.height + hypotenuse
#
#     def calculate_angles(self):
#         alpha = math.degrees(math.atan(self.height / self.base))
#         beta = 90 - alpha
#         return 90, alpha, beta
#
# triangle = RightTriangle(3, 4)
# print("основа: ", triangle.base)
# print("высота:", triangle.height)
#
# triangle.increase_side(10)
# print("Увеличенные борта:")
# print("основа: ", triangle.base)
# print("высота:", triangle.height)
#
# circumcircle_radius = triangle.calculate_circumcircle_radius()
# print("Радиус окружности:", circumcircle_radius)
#
# perimeter = triangle.calculate_perimeter()
# print("Периметр:", perimeter)
#
# angles = triangle.calculate_angles()
# print("Углы (градусы):")
# print("90 градусов (прямой угол)")
# print("Альфа:", angles[1])
# print("Бета:", angles[2])




############################
#77777777777777777777777777#
############################


# class Bus:
#     def __init__(self, max_speed, capacity):
#         self.speed = 0
#         self.capacity = capacity
#         self.max_speed = max_speed
#         self.passengers = []
#         self.hasEmptySeats = True
#         self.seats = {i: None for i in range(1, capacity + 1)}
#
#     def board_passengers(self, passenger_names):
#         if not self.hasEmptySeats:
#             print("Автобус уже полон.")
#             return
#         for passenger_name in passenger_names:
#             if len(self.passengers) < self.capacity:
#                 self.passengers.append(passenger_name)
#                 for seat, occupant in self.seats.items():
#                     if occupant is None:
#                         self.seats[seat] = passenger_name
#                         break
#             else:
#                 print(f"Больше нет свободных мест на {passenger_name}. автобус заполнен.")
#         self.update_empty_seats()
#
#     def disembark_passengers(self, passenger_names):
#         for passenger_name in passenger_names:
#             if passenger_name in self.passengers:
#                 self.passengers.remove(passenger_name)
#                 for seat, occupant in self.seats.items():
#                     if occupant == passenger_name:
#                         self.seats[seat] = None
#         self.update_empty_seats()
#
#     def increase_speed(self, value):
#         if self.speed + value <= self.max_speed:
#             self.speed += value
#         else:
#             print("Нельзя превышать максимальную скорость.")
#
#     def decrease_speed(self, value):
#         if self.speed - value >= 0:
#             self.speed -= value
#         else:
#             print("Скорость не может опускаться ниже 0.")
#
#     def update_empty_seats(self):
#         self.hasEmptySeats = len(self.passengers) < self.capacity
#
#     def __contains__(self, passenger_name):
#         return passenger_name in self.passengers
#
#     def __iadd__(self, passenger_name):
#         self.board_passengers([passenger_name])
#         return self
#
#     def __isub__(self, passenger_name):
#         self.disembark_passengers([passenger_name])
#         return self
#
# bus = Bus(max_speed=60, capacity=50)
#
# bus.board_passengers(["Кирил", "Согдияр", "Саша","Кира","Браус","Клара","Анна","Наташа"])
# bus += "Слава"
#
# print("Пассажиры:", bus.passengers)
# print("сидящие: ", bus.seats)
# print("Есть свободные места: ", bus.hasEmptySeats)
#
# bus.disembark_passengers(["Alice"])
# bus -= "Bob"
#
# print("Пассажиры:", bus.passengers)
# print("сидящие:", bus.seats)
# print("Есть свободные места: ", bus.hasEmptySeats)
#
# bus.increase_speed(20)
# print("Текущая скорость:", bus.speed)
#
# bus.decrease_speed(10)
# print("Текущая скорость:", bus.speed)
