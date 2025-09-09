from dataclasses import dataclass, field
from typing import ClassVar

from .slot import Slot

@dataclass
class Ticket:
    id: int
    registration_number: str
    color: str
    slot: Slot
    tickets: ClassVar[list['Ticket']] = []
