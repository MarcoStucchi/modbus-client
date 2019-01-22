"""
Read Block Registers as implemented in Huawei Modbus TCP to Power Line converter
----------------------------------------------------------------------------------
"""

__author__ = "Marco Stucchi <marco.stucchi@gmail.com>"

import struct
import logging

from pymodbus.pdu import ModbusRequest
from pymodbus.pdu import ModbusResponse
from pymodbus.pdu import ModbusExceptions
from pymodbus.compat import int2byte, byte2int
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.factory import ClientDecoder

# --------------------------------------------------------------------------- #
# configure the client logging
# --------------------------------------------------------------------------- #
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.NOTSET)

# --------------------------------------------------------------------------- #
# create your custom message
# --------------------------------------------------------------------------- #
# The following is simply a read coil request that always reads 16 coils.
# Since the function code is already registered with the decoder factory,
# this will be decoded as a read coil response. If you implement a new
# method that is not currently implemented, you must register the request
# and response with a ClientDecoder factory.
# --------------------------------------------------------------------------- #

class ReadBlockRegistersRequest(ModbusRequest):
    # Read registers block has function code 0x6C
    function_code = 0x6C

    def __init__(self, **kwargs):
        ModbusResponse.__init__(self, **kwargs)
        self.block = kwargs.get('block', 0)
        self.slice = kwargs.get('slice', 0)

    def encode(self):
        return struct.pack('>BBHH', 5, 4, self.block, self.slice)

    def decode(self, data):
        self.block, self.slice = struct.unpack('>HH', data)

    def execute(self, context):
        #if not (1 <= self.count <= 0x7d0):
        #    return self.doException(ModbusExceptions.IllegalValue)
        #if not context.validate(self.function_code, self.address, self.count):
        #    return self.doException(ModbusExceptions.IllegalAddress)
        values = context.getValues(self.function_code, self.address,
                                   self.count)
        return ReadBlockRegistersResponse(values)

class ReadBlockRegistersResponse(ModbusResponse):

    # Read registers block has function code 0x6C
    function_code = 0x6C

    def __init__(self, **kwargs):
        ModbusResponse.__init__(self, **kwargs)
        self.block = kwargs.get('block', 0)
        self.slice = kwargs.get('slice', 0)
        # Init response fields
        self.frame_length = 0
        self.state = 0
        self.block_subfunction = 0
        self.slice_number = 0
        self.slice_amount = 0
        self.block_length = 0
        self.header_crc = 0
        self.slice_length = 0
        self.data = 0

    def encode(self):
        return struct.pack('>BBHH', 5, 4, self.block, self.slice)

    def decode(self, data):
        #self.block, self.slice = struct.unpack('>HH', data[0:4])
        self.frame_length, \
        self.state, \
        self.block_subfunction, \
        self.slice_number, \
        self.slice_amount, \
        self.block_length, \
        self.header_crc, \
        self.slice_length = struct.unpack('>BBHHHIHH', data[0:16])
        self.data = data[16:16+self.block_length]

    def execute(self, context):
        #if not (1 <= self.count <= 0x7d0):
        #    return self.doException(ModbusExceptions.IllegalValue)
        #if not context.validate(self.function_code, self.address, self.count):
        #    return self.doException(ModbusExceptions.IllegalAddress)
        values = context.getValues(self.function_code, self.address,
                                   self.count)
        return ReadBlockRegistersResponse(values)

# --------------------------------------------------------------------------- #
# execute the request with your client
# --------------------------------------------------------------------------- #
# using the with context, the client will automatically be connected
# and closed when it leaves the current scope.
# --------------------------------------------------------------------------- #

if __name__ == "__main__":

    with ModbusClient('192.169.11.30') as client:
        #decoder = ClientDecoder()
        ClientDecoder.register(client.framer.decoder, function=ReadBlockRegistersResponse)
        request = ReadBlockRegistersResponse(block=3, slice=0, unit=1)
        result = client.execute(request)
        print(result)