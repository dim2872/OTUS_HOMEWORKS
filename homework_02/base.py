from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    started = False
    weight = 0
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started == False and self.fuel > 0:
            self.started = True
            return self.started
        else:
            raise exceptions.LowFuelError

    def move(self, distance):
        if self.fuel < self.fuel_consumption * distance:
            raise exceptions.NotEnoughFuel
        else:
            total_fuel = self.fuel_consumption * distance
        return total_fuel


