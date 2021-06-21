
"""
Создайте класс Passport (паспорт), который будет
содержать паспортную информацию о гражданине заданной страны.
С помощью механизма наследования, реализуйте
класс ForeignPassport (загран.паспорт) производный от
Passport.
Напомним, что заграничный паспорт содержит помимо паспортных данных, также данные о визах, номер
заграничного паспорта.

Каждый из классов должен содержать необходимые методы.
"""

import array
from random import *
from datetime import *
from time import *


class Passport:

    def __init__(self, name, surname, patronymic, gen: str, city, birth_date):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.gender = gen.upper()
        self.sity = city
        self.birth_date = strptime(birth_date, '%d.%m.%Y')

        self.authority = randint(1111, 9999)
        self.__number = randint(100000000, 999999999)
        self.create_date = datetime.today().strftime("%d-%m-%Y")

    def __str__(self):
        return f'Passport: {self.name} {self.surname}'

    def _print(self):
        print(f"Passport info:\n\
            \tName: {self.name}\n\
            \tSurname: {self.surname}\n\
            \tPatronymic: {self.patronymic}\n\
            \tGender: {self.gender}\n\
            \tCity: {self.sity}\n\
            \tBirth date: {self.birth_date[2]}-{self.birth_date[1]}-{self.birth_date[0]}\n\
            \tAuthority: {self.authority}\n\
            \tNumber : {self.__number}\n\
            \tDate: {self.create_date}")

    def _printBirthdate(self):
        print(f'\tBirth date: {self.birth_date[2]}-{self.birth_date[1]}-{self.birth_date[0]}\n\
')


class ForeignPassport(Passport):

    def __init__(self, name, surname, patronymic, gen: str, city, birth_date):
        super().__init__(name, surname, patronymic, gen, city, birth_date)

        self.__number = randint(100000000, 999999999)
        self.visa = []

    def new_visa(self, country, end_time):
        end_time = strptime(end_time, '%d.%m.%Y')
        self.visa.append({country: end_time})

    def _print(self):
        print(f"Passport info:\n\
            \tName: {self.name}\n\
            \tSurname: {self.surname}\n\
            \tPatronymic: {self.patronymic}\n\
            \tGender: {self.gender}\n\
            \tCity: {self.sity}\n\
            \tBirth date: {self.birth_date[2]}-{self.birth_date[1]}-{self.birth_date[0]}\n\
            \tNumber : {self.__number}")
        print('Visa info:')
        for item in self.visa:
            print('\t', list(item.keys())[
                  0], ':', f'{list(item.values())[0][2]}-{list(item.values())[0][1]}-{list(item.values())[0][0]}')

    def countryVisaInfo(self):
        print('Visited Country Info:')
        for item in self.visa:
            print('\t', list(item.keys())[0])

    def timeVisa(self):
        print('Acting Visas info:')
        today = strptime(datetime.today().strftime('%d-%m-%Y'), '%d-%m-%Y')
        for item in self.visa:
            if list(item.values())[0][0] >= today[0]:
                if list(item.values())[0][1] > today[1]:
                    print('\t', list(item.keys())[
                        0], ':', f'{list(item.values())[0][2]}-{list(item.values())[0][1]}-{list(item.values())[0][0]}')
                elif list(item.values())[0][1] == today[1]:
                    if list(item.values())[0][2] > today[2]:
                        print('\t', list(item.keys())[
                            0], ':', f'{list(item.values())[0][2]}-{list(item.values())[0][1]}-{list(item.values())[0][0]}')


Bob = Passport('Bob', 'Bobick', 'Bobovich', 'm', 'London', '25.06.2016')
print(Bob.birth_date)

Bob._print()
Bob._printBirthdate()
Bill = ForeignPassport('Bill', 'Bobick', 'Bobovich',
                       'm', 'London', '25.06.2016')
Bill.new_visa('Poland', '21.05.2021')
Bill.new_visa('Ukraine', '01.09.2021')
Bill.new_visa('Russia', '01.09.2021')


Bill._print()
Bill.countryVisaInfo()
Bill.timeVisa()
# print(Bob.authority, Bob.number)


#  Робота з датою (25-12-2000) +
#  Метод вивведення дати народження у текстовому форматі (25-12-2000) +

# ForeignPassport
# Методи:
#   Вивести всі відвідані країни +
#   Відобразити інформацію про незакінчені візи +
