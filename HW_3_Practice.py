import random
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age, money, home):
        self.name = name
        self.age = age
        self.money = money
        self.home = home

    @abstractmethod
    def info_person(self):
        raise NotImplementedError('This method was not implemented')

    @abstractmethod
    def make_money(self):
        raise NotImplementedError('This method was not implemented')

    @abstractmethod
    def by_house(self, house):
        raise NotImplementedError('This method was not implemented')


class Human(Person):
    def __init__(self, name, age, home, money):
        super().__init__(name, age, home, money)

    def info_person(self):
        print(f"Hello, my name is {self.name},I'm {self.age} .")

    def make_money(self):
        self.money = self.money + 1000
        print(f'I have UAN {self.money}.')

    def by_house(self, house):
        if self.money >= house.cost:
            print(f'I can buy this house.')
        else:
            print(f'You do not have enough money to buy this house.')


class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def info_house(self):
        print(f'This house is {self.area} square meters and costs {self.cost} euros.')

    def discount(self):
        if self.area >= 100:
            print('I can appy a 10% discount on this house!')
            self.cost = self.cost * 0.9
        if self.area >= 150:
            print('I can appy a 20% discount on this house!')
            self.cost = self.cost * 0.8
            if self.area <= 100:
                print('This house has no discounts')
                self.cost = self.cost


class SmallHouse(House):
    def __init__(self, name, area, cost):
        super().__init__(area, cost)
        if self.area <= 40:
            self.__class__ = House
        self.name = name


class RealtorMeta(type):
    _instances = {}

    def __call_(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):
    def __init__(self, name_realtor, house, discount):
        self.name_realtor = name_realtor
        self.house = house
        self.discount = discount

    def info_realtor(self):
        print(f'Hello my name {self.name_realtor} ,Im your realtor and i can you a discount if you buy from me.  ')

    def provide_info(self):
        for i in self.house:
            i.info_house()

    def hand_discount(self):
        if self.discount is True:
            self.house.discount()

    def steal_money(self, human):
        if random.randint(1, 10) == 10:
            human.money = 0
            print(f'Realtor is thief!!!)')
        else:
            pass


p1 = Human('Kim', 40, 25000, 0)
p1.info_person()
p1.make_money()
h1 = House(250, 250000)
h2 = House(45, 18000)
h1.discount()
h1.info_house()
r1 = Realtor('Olga', [h1], '18%')
r2 = Realtor('Olga', [h2], '10%')
r1.info_realtor()
r1.hand_discount()
r1.provide_info()
r2.provide_info()
r2.hand_discount()
r3 = Realtor('Olga', [h1], '1%')
r3.steal_money("l")
