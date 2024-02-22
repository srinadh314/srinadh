import datetime

class Reservation:
    def __init__(self, reservation_id, customer_name, date, time, table_number):
        self.reservation_id = reservation_id
        self.customer_name = customer_name
        self.date = date
        self.time = time
        self.table_number = table_number

class ReservationSystem:
    def __init__(self):
        self.reservations = []

    def make_reservation(self, customer_name, date, time, table_number):
        reservation_id = len(self.reservations) + 1
        reservation = Reservation(reservation_id, customer_name, date, time, table_number)
        self.reservations.append(reservation)
        return reservation_id

    def check_availability(self, date, time):
        # For simplicity, assume tables are available if not reserved
        for reservation in self.reservations:
            if reservation.date == date and reservation.time == time:
                return False
        return True

# Example usage:
reservation_system = ReservationSystem()

# Make a reservation
reservation_id = reservation_system.make_reservation("John Doe", datetime.date(2024, 2, 20), "18:00", 1)
print("Reservation ID:", reservation_id)

# Check availability
print("Available:", reservation_system.check_availability(datetime.date(2024, 2, 20), "18:00"))  # False
print("Available:", reservation_system.check_availability(datetime.date(2024, 2, 21), "18:00"))  # True
