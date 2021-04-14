"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02 import exceptions


class Plane(Vehicle):
    def __init__(self, cargo, max_cargo, weight, started, fuel, fuel_consumption):
        self.max_cargo = max_cargo
        self.cargo = cargo
        super().__init__(self, weight, started, fuel, fuel_consumption)

    def load_cargo(self, add_cargo):
        if self.max_cargo <= self.cargo + add_cargo:
            self.cargo += add_cargo
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self, add_cargo):
        cargo_before = self.cargo
        self.cargo = 0.0
        return cargo_before