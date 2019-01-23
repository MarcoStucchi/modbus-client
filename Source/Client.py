"""
Connects to the Huawei converter and extract information
---------------------------------------------------------
"""

__author__ = "Marco Stucchi"
__email__ = "marco.stucchi@gmail.com"

import logging

from pymodbus.client.sync import ModbusTcpClient
from pymodbus.factory import ClientDecoder

import Converter
import huawei_block_functions

# Unit ID for Huawei Converter is 1, >= 2 for STAs
CONVERTER = 1
debug_level = logging.DEBUG

# Start logger
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(debug_level)
logging.disable(debug_level)

try:
    # Create client connection
    log.info("Connecting to Huawei Converter..")
    client = ModbusTcpClient('192.169.11.30')
    # Extract information from the device
    log.info("Getting Huawei Converter registers..")
    for reg in Converter.holding_registers:
        result = client.read_holding_registers(address=reg["address"], count=reg["nRegs"], unit=CONVERTER)
        print(reg["name"] + ": " + reg["function"](result.registers))
        log.debug(result.registers)
    log.info("Getting Huawei Converter blocks..")
    ClientDecoder.register(client.framer.decoder, function=huawei_block_functions.ReadBlockRegistersResponse)
    for bl in Converter.blocks:
        request = huawei_block_functions.ReadBlockRegistersResponse(block=bl["block"], slice=0, unit=CONVERTER)
        result = client.execute(request)
        print(bl["name"] + ": " + result.data)
    # Close client connection
    log.info("Closing connection..")
    client.close()
except:
    # Close client connection
    log.error("Huawei Converter not found")
