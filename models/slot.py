from dataclasses import dataclass, field

from .car import Car


@dataclass
class Slot:
    id: int
    car: Car | None = field(default=None, init=False)

    def register_car(self, car: Car):
        self.car = car

    def unregister_car(self):
        self.car = None
