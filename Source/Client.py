import logging
from pymodbus.client.sync import ModbusTcpClient
import Converter

# Unit ID for Huawei Converter is 1, >= 2 for STAs
CONVERTER = 1
# Set debug level
debug_level = logging.INFO

# Start logger
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(debug_level)

try:
    # Create client connection
    log.info("Connecting to Huawei Converter..")
    client = ModbusTcpClient('192.169.11.30')
    # Extract information from the device
    log.info("Getting Huawei Converter registers..")
    for reg in Converter.holding_registers:
        result = client.read_holding_registers(address=reg["address"], count=reg["nRegs"], unit=CONVERTER)
        print reg["name"] + ": " + reg["function"](result.registers)
        log.debug(result.registers)
    # Close client connection
    log.info("Closing connection..")
    client.close()
except:
    # Close client connection
    log.error("Huawei Converter not found")
