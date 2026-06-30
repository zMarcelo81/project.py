from abc import ABC, abstractmethod


class SmartService(ABC):
    @abstractmethod
    def activate_service(self):
        pass


class EmergencyService(ABC):
    @abstractmethod
    def send_alert(self):
        pass


class SmartParkingService(SmartService):
    def activate_service(self):
        return "Smart parking service activated for Dorset College."


class FireService(EmergencyService):
    def send_alert(self):
        return "Fire emergency alert sent."