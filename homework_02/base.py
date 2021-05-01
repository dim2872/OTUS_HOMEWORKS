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

    def start(self, started, fuel):
        if started == False and fuel > 0:
            started = True
            return started
        else:
            raise exceptions.LowFuelError

    def move(self, fuel, distance, fuel_consumption):
        if fuel < fuel_consumption * distance:
            raise exceptions.NotEnoughFuel
        return fuel_consumption * distance


