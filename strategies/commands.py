from models.car import Car
from models.parking_lot import ParkingLot
from models.ticket import Ticket


class Command:
    tickets: list[Ticket] = []

    def create_parking_lot(self, number_of_slots: int) -> ParkingLot:
        self.parking_lot = ParkingLot(number_of_slots)
        return self.parking_lot
        return f"Creating a parking lot with {number_of_slots} slots"

    def park(self, registration_number: str, color: str) -> str:
        car = Car(registration_number, color)
        slot = self.parking_lot.get_empty_slot()
        if slot:
            slot.register_car(car)
            return "Allocate slot number: {slot.id}"
        else:
            return "Sorry, parking lot is full"

    def leave(self, slot_position: int) -> str:
        slot = self.parking_lot.get_slot(slot_position)
        slot.unregister_car()
        return "Sorry, parking lot is full"

    def status(self):
        pass

    def generate_ticket():
        pass
