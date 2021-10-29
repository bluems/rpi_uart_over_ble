from BLE.Const import UART_SERVICE_UUID
from BLE.RxCharacteristic import RxCharacteristic
from BLE.Service import Service
from BLE.TxCharacteristic import TxCharacteristic


class UartService(Service):
    device = None
    def __init__(self, bus, index):
        Service.__init__(self, bus, index, UART_SERVICE_UUID, True)
        self.add_characteristic(TxCharacteristic(bus, 0, self))
        self.add_characteristic(RxCharacteristic(bus, 1, self))
