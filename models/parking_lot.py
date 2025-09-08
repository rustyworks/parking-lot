from dataclasses import dataclass, field
from .slot import Slot


@dataclass
class ParkingLot:
    number_of_slots: int
    slots: list[Slot] = field(default_factory=list, init=False)

    def __post_init__(self):
        for number in range(1, self.number_of_slots + 1):
            slot = Slot(id=number)
            self.slots.append(slot)

    def get_empty_slot(self) -> Slot | None:
        empty_slots = [slot for slot in self.slots if not slot.car]
        nearest_slot = empty_slots[0] if empty_slots else None
        return nearest_slot

    def get_slot(self, position):
        return self.slots[position]
