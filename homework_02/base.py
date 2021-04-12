from abc import ABC
import exceptions


class Vehicle(ABC):

    def __init__(self, weight=0.0, started=False, fuel=0.0, fuel_consumption=0.0):
        self.fuel = fuel
        self.weight = weight
        self.fuel_consumption = fuel_consumption

    def start(self, started):
        if started:
            raise exceptions.LowFuelError
        else:
            started = True
        return started

    def move(self, fuel, distance, fuel_consumption):
        if fuel < fuel_consumption * distance:
            raise exceptions.NotEnoughFuel
        return fuel_consumption * distance


