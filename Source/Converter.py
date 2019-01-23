"""
Huawei Converter descriptor
---------------------------
"""

__author__ = "Marco Stucchi"
__email__ = "marco.stucchi@gmail.com"

# Custom module
import Visualization as Show

# File descriptor for Huawei Converter

# Modbus Registers declarations
Register_1 = {"name":"Silence Switch", "address":0x2c04, "nRegs":1, "function":Show.OnOff}
Register_2 = {"name":"Whitelist Switch", "address":0x2c05, "nRegs":1, "function":Show.OnOff}
Register_3 = {"name":"Converter MAC Address", "address":0x2c00, "nRegs":3, "function":Show.MacAddress}
Register_4 = {"name":"Converter network address & mask", "address":0x2400, "nRegs":4, "function":Show.IpAddressAndMac}
Register_5 = {"name":"Gateway", "address":0x2404, "nRegs":2, "function":Show.IpAddress}

# Modbus Block declarations
Block_1 = {"name":"Whitelist", "block":3}
Block_2 = {"name":"Maplist", "block":5}
Block_3 = {"name":"Network Nodes", "block":4}
Block_4 = {"name":"Join & Leave events", "block":6}

# Dictionary definition
holding_registers = [Register_1, Register_2, Register_3, Register_4, Register_5]
blocks = [Block_1, Block_2, Block_3, Block_4]
