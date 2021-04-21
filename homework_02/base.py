from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    started = False

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.fuel = fuel
        self.weight = weight
        self.fuel_consumption = fuel_consumption

    def start(self, started=False):
        if started:
            raise exceptions.LowFuelError
        else:
            started = True
        return started

    def move(self, fuel, distance, fuel_consumption):
        if fuel < fuel_consumption * distance:
            raise exceptions.NotEnoughFuel
        return fuel_consumption * distance


