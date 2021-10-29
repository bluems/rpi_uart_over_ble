from BLE.Application import Application
from BLE.UartService import UartService


class UartApplication(Application):
    def __init__(self, bus):
        Application.__init__(self, bus)
        self.add_service(UartService(bus, 0))