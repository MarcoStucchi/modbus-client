# Custom module
import Visualization as Show

# File descriptor for Huawei Converter

# Modbus Registers declarations
Register_1 = {"name":"Silence Switch", "address":0x2c04, "nRegs":1, "function":Show.OnOff}
Register_2 = {"name":"Whitelist Switch", "address":0x2c05, "nRegs":1, "function":Show.OnOff}
Register_3 = {"name":"Converter MAC Address", "address":0x2c00, "nRegs":3, "function":Show.MacAddress}
Register_4 = {"name":"Converter network address & mask", "address":0x2400, "nRegs":4, "function":Show.IpAddressAndMac}
Register_5 = {"name":"Gateway", "address":0x2404, "nRegs":2, "function":Show.IpAddress}

# Dictionary definition
holding_registers = [Register_1, Register_2, Register_3, Register_4, Register_5]
