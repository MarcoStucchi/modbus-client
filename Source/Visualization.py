__author__ = "Marco Stucchi"
__email__ = "marco.stucchi@gmail.com"

def OnOff(registers):
    if (registers[0] == 0):
        return "Off"
    else:
        return "On"

def IpAddressAndMac(registers):
    return("<" + str(registers[0]>>8) + "." + str(registers[0]&255) + "." + str(registers[1]>>8) + "." + str(registers[1]&255) + ">, " +
           "<" + str(registers[2]>>8) + "." + str(registers[2]&255) + "." + str(registers[3]>>8) + "." + str(registers[3]&255) + ">")

def IpAddress(registers):
    return("<" + str(registers[0]>>8) + "." + str(registers[0]&255) + "." + str(registers[1]>>8) + "." + str(registers[1]&255) + ">")

def MacAddress(registers):
    return("<" +
           "{:02x}".format(registers[0]>>8) + ":" + "{:02x}".format(registers[0]&255) + ":" +
           "{:02x}".format(registers[1]>>8) + ":" + "{:02x}".format(registers[1]&255) + ":" +
           "{:02x}".format(registers[2]>>8) + ":" + "{:02x}".format(registers[2]&255) + ">")

def String(registers):
    return(str(registers))
