class TransportMode:
    def __init__(self, name):
        self.name = name

    def calculate_fare(self, distance):
        raise NotImplementedError("Subclass must implement calculate_fare().")


class Bus(TransportMode):
    def __init__(self):
        super().__init__("Bus")

    def calculate_fare(self, distance):
        return 2 + (distance * 0.2)


class Taxi(TransportMode):
    def __init__(self):
        super().__init__("Taxi")

    def calculate_fare(self, distance):
        return 5 + (distance * 1)


class Metro(TransportMode):
    def __init__(self):
        super().__init__("Metro")

    def calculate_fare(self, distance):
        return 2.5 + (distance * 0.15)