from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Ticket:
    id: int
    registration_number: str
    color: str
    slot_id: int
    tickets: ClassVar[list['Ticket']] = []
