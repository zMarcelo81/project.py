from encapsulation.employees import CityEmployee, ITStaff
from inheritance.citizens import Citizen, StudentCitizen
from polymorphism.transport import Bus, Taxi, Metro
from abstraction.services import SmartParkingService, FireService


def main():
    try:
        employee1 = CityEmployee("E01", "Marcelo", 30000)
        employee2 = ITStaff("E02", "Ana", 40000)

        citizen1 = Citizen("C01", "Marcelo", 25)
        citizen2 = StudentCitizen("C02", "Dorset Student", 20)

        transports = [Bus(), Taxi(), Metro()]

        parking = SmartParkingService()
        fire = FireService()

        print("SMART CITY SYSTEM - DORSET COLLEGE")

        print("\n--- ENCAPSULATION ---")
        print(employee1.get_name(), "- Bonus:", employee1.calculate_bonus())
        print(employee2.get_name(), "- Bonus:", employee2.calculate_bonus())

        print("\n--- INHERITANCE ---")
        print(citizen1.name, "-", citizen1.calculate_city_benefits())
        print(citizen2.name, "-", citizen2.calculate_city_benefits())

        print("\n--- POLYMORPHISM ---")
        for transport in transports:
            print(transport.name, "fare for 10 km:", transport.calculate_fare(10))

        print("\n--- ABSTRACTION ---")
        print(parking.activate_service())
        print(fire.send_alert())

    except ValueError as error:
        print("Validation Error:", error)


if __name__ == "__main__":
    main()