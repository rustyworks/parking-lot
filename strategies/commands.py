from models.car import Car
from models.parking_lot import ParkingLot
from models.ticket import Ticket


def print_all(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        print(result)
        return result
    return wrapper


class Command:

    def create_parking_lot(self, number_of_slots: int) -> ParkingLot:
        self.parking_lot = ParkingLot(number_of_slots)
        return self.parking_lot
        return f"Creating a parking lot with {number_of_slots} slots"

    @print_all
    def park(self, registration_number: str, color: str) -> str:
        car = Car(registration_number, color)
        slot = self.parking_lot.get_empty_slot()
        if slot:
            slot.register_car(car)
            ticket = Ticket(
                id=len(Ticket.tickets) + 1,
                registration_number=registration_number,
                color=color,
                slot=slot.id,
            )
            Ticket.tickets.append(ticket)
            return f"Allocate slot number: {slot.id}"
        else:
            return "Sorry, parking lot is full"

    @print_all
    def leave(self, slot_position: int) -> str:
        slot = self.parking_lot.get_slot(slot_position)
        slot.unregister_car()
        return "Sorry, parking lot is full"

    @print_all
    def status(self):
        slot_id_padding = 12
        car_registration_number_padding = 20
        car_color_padding = 10

        header = f'{"Slot No.":<{slot_id_padding}} {"Registration No":<{car_registration_number_padding}} {"Colour":<{car_color_padding}}'

        body = ""
        for slot in self.parking_lot.slots:
            if slot.car:
                body += "\n"
                body += f'{slot.id:<{slot_id_padding}} {slot.car.registration_number:<{car_registration_number_padding}} {slot.car.color:<{car_color_padding}}'

        return header + body

    @print_all
    def registration_numbers_for_cars_with_colour(self, color: str) -> str:
        return ", ".join([slot.car.registration_number for slot in self.parking_lot.slots if slot.car and slot.car.color == color])

    @print_all
    def slot_numbers_for_cars_with_colour(self, color: str) -> str:
        return ", ".join([str(slot.id) for slot in self.parking_lot.slots if slot.car and slot.car.color == color])

    @print_all
    def slot_number_for_registration_number(self, registration_number: str) -> str:
        slots = [slot.id for slot in self.parking_lot.slots if slot.car.registration_number == registration_number]
        if slots:
            return slots[0]
        else:
            return None
