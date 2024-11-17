import json

class Person:
    def __init__(self, first_name, last_name, contact_number):
        self.first_name = first_name
        self.last_name = last_name
        self.contact_number = contact_number

    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name}, Contact: {self.contact_number}")

class User(Person):  # Inheritance
    def __init__(self, first_name, last_name, contact_number):
        super().__init__(first_name, last_name, contact_number)  # Calls the constructor of the base class
        self.reserved_seats = []

    def add_reservation(self, seat):
        self.reserved_seats.append(seat)

    def view_reservations(self, system):  
        if not system.seats:
            print("No reserved seats.")
            return
        print("Reserved Seats:")
        for seat in system.seats:
            if not seat.is_available:  # Check if the seat is reserved
                print(f"Seat ID: {seat.seat_id}, Match ID: {seat.match_id}, Price: ₱{seat.price}, Reserved By: {seat.reserved_by}")

class Match:
    def __init__(self, match_id, teams, date, location):
        self.match_id = match_id
        self.teams = teams
        self.date = date
        self.location = location

    def display_match_details(self):  # Encapsulation (hides internal representation)
        print(f"Match ID: {self.match_id}, Teams: {self.teams}, Date: {self.date}, Location: {self.location}")

class Seat:
    def __init__(self, seat_id, match_id, price):
        self.seat_id = seat_id
        self.match_id = match_id
        self.price = price
        self.is_available = True
        self.reserved_by = None

    def reserve(self, user):
        if self.is_available:
            self.is_available = False
            self.reserved_by = f"{user.first_name} {user.last_name}"
            user.add_reservation(self)
            return True
        return False

    def __str__(self):  # Polymorphism (different behavior for str representation)
        return f"Seat {self.seat_id} (Match {self.match_id}) - {'Available' if self.is_available else 'Reserved'}"

class ReservationSystem:
    def __init__(self):
        self.matches = []
        self.seats = []

    def add_match(self):
        self.matches.append(Match(1, "Creamline Cool Smashers vs Petro Gazz Angels", "2024-12-15", "Araneta Coliseum"))
        self.matches.append(Match(2, "Chery Tiggo Crossovers vs F2 Logistics Cargo Movers", "2024-12-16", "PhilSports Arena"))
        self.matches.append(Match(3, "PLDT High Speed Hitters vs Akari Chargers", "2024-12-17", "Ynares Center Antipolo"))
        self.matches.append(Match(4, "Cignal HD Spikers vs Kakai Beach Resort", "2024-12-18", "Mall of Asia Arena"))
        self.matches.append(Match(5, "Choco Mucho Flying Titans vs UAI-Army Lady Troopers", "2024-12-19", "PhilSports Arena"))
        self.matches.append(Match(6, "Farm Fresh Foxies vs Nxled Chamelions", "2024-12-20", "Ynares Center Antipolo"))
        self.matches.append(Match(7, "Zus Coffee Thunderbelles vs Galeries Towers Highrisers", "2024-12-21", "Mall of Asia Arena"))
        self.matches.append(Match(8, "Capital1 Solar Spikers vs Dela Salle University", "2024-12-22", "PhilSports Arena"))
        self.matches.append(Match(9, "Ateneo Blue Eagles vs NU Lady Bulldogs", "2024-12-23", "Araneta Coliseum"))
        self.matches.append(Match(10, "FEU Lady Tamaraws vs UST Golden Tigresess", "2024-12-24", "Ynares Center Antipolo"))

    def add_seat(self, match_id, num_seats):
        for i in range(1, num_seats + 1):
            self.seats.append(Seat(i, match_id, 100)) 

    def display_matches(self):
        for match in self.matches:
            match.display_match_details()

    def display_seats(self, match_id):
        seats = [seat for seat in self.seats if seat.match_id == match_id and seat.is_available]
        if not seats:
            print("No available seats.")
            return
        for seat in seats:
            print(f"Seat Number: {seat.seat_id}, Price: ₱{seat.price}")

    def reserve_seat(self, user, match_id, seat_id):
        for seat in self.seats:
            if seat.match_id == match_id and seat.seat_id == seat_id:
                if seat.reserve(user):
                    print("-------------------------------------------------------")
                    print(f"Seat {seat_id} reserved successfully by {user.first_name} {user.last_name}!")
                    print("-------------------------------------------------------")
                    return
                else:
                    print("Seat already reserved.")
                    return
        print("Seat not found.")

    def export_to_json(self, file_path="data.json"):
        data = {
            "matches": [
                {
                    "match_id": match.match_id,
                    "teams": match.teams,
                    "date": match.date,
                    "location": match.location
                }
                for match in self.matches
            ],
            "seats": [
                {
                    "seat_id": seat.seat_id,
                    "match_id": seat.match_id,
                    "price": seat.price,
                    "is_available": seat.is_available,
                    "reserved_by": seat.reserved_by
                }
                for seat in self.seats
            ]
        }
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print("Processing.")

# Main
if __name__ == "__main__":
    try:
        system = ReservationSystem()
        system.add_match()  #10 matches

        # 50 seats for each match
        for match in system.matches:
            system.add_seat(match.match_id, 50)

        while True:
            print("\n----------------------------------------------------------------------")
            print("  Welcome to VolleySeats Reservation System! Reserve in just one tap.")
            print("----------------------------------------------------------------------")
            first_name = input("\nEnter your first name: ")
            last_name = input("Enter your last name: ")
            contact_number = input("Enter your contact number: ")
            user = User(first_name, last_name, contact_number)

            while True:
                print("\nOptions:")
                print("1. View available matches")
                print("2. View reserved seats and matches")
                print("3. Reserve a seat")
                print("4. Confirm Reservation")
                print("5. Quit")  
                try:
                    option = int(input("\nChoose an option: "))
                    if option == 1:
                        system.display_matches()
                        try:
                            match_id = int(input("\nEnter Match ID to view available seats: "))
                            system.display_seats(match_id)
                        except ValueError:
                            print("Invalid input for Match ID. Please enter a valid number.")
                    elif option == 2:
                        user.view_reservations(system)  
                    elif option == 3:
                        try:
                            match_id = int(input("\nEnter Match ID to reserve a seat: "))
                            system.display_seats(match_id)
                            seat_id = int(input("\nEnter Seat ID to reserve: "))
                            system.reserve_seat(user, match_id, seat_id)
                        except ValueError:
                            print("Invalid input for Match ID or Seat ID. Please enter valid numbers.")
                    elif option == 4:
                        system.export_to_json()  #confirming reservations
                        print("Reservation confirmed and data exported.")
                        break  # Exit
                    elif option == 5:
                        print("--------------------------------------------")
                        print("Thank you for using the reservation system!")
                        print("--------------------------------------------")
                        exit()  # Exit the program
                    else:
                        print("Invalid option. Please try again.")
                except ValueError:
                    print("Invalid input for option. Please enter a number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
