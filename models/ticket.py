from dataclasses import dataclass

from .slot import Slot

@dataclass
class Ticket:
    id: int
    registration_number: str
    color: str
    slot: Slot
