from models.parking_lot import ParkingLot
from strategies.commands import Command


def main():
    command = Command()
    parking_lot = command.create_parking_lot(6)
    command.park("KA-01-HH-1234", "White")
    command.park("KA-01-HH-9999", "White")
    command.park("KA-01-BB-0001", "Black")
    command.park("KA-01-HH-7777", "Red")
    command.park("KA-01-HH-2701", "Blue")
    command.park("KA-01-HH-3141", "Black")
    command.leave(4)
    command.status()
    command.park("KA-01-P-333", "White")
    command.park("DL-12-AA-9999", "White")
    breakpoint()


if __name__ == "__main__":
    main()
