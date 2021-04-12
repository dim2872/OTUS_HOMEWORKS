"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
import exceptions


class Plane(Vehicle):
    def __init__(self, cargo, max_cargo):
        self.max_cargo = max_cargo
        self.cargo = cargo

    def load_cargo(self, add_cargo):
        if self.max_cargo <= self.cargo + add_cargo:
            self.cargo += add_cargo
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self, add_cargo):
        cargo_before = self.cargo
        self.cargo = 0.0
        return cargo_before
