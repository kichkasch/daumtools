import serial
import struct 
from config import *
from daumcommands import *

def _packByte(rawByte):
	return struct.pack('!B',rawByte)

def _packBytes(rawBytes):
	ret = []
	for x in rawBytes:
		ret.append(_packByte(x))
	return ret

def _unpackByte(packedByte):
	return struct.unpack('!B', packedByte)[0]

def _unpackBytes(packedBytes):
	ret = []
	for x in packedBytes:
		ret.append(_unpackByte(x))
	return ret

def initConnection():
	ser = serial.Serial()  # open serial port
	ser.port = SERIAL_PORT
	ser.baudrate = 9600
	ser.open()
	return ser

def sGetAddress(ser):
	ser.write(_packByte(CMDgetAddress))     
	ch = ser.read(2)
	return _unpackByte(ch[0]), _unpackByte(ch[1])

def getRunDaten(ser, cockpitAddress):
	ser.write(_packBytes([CMDrunDaten, cockpitAddress]))
	ch = ser.read(19)
	return _unpackBytes(ch)

def setGear(ser, gear, cockpitAddress):
	ser.write(_packBytes([CMDsetGear, cockpitAddress, gear]))
	ch = ser.read(3)

def getVersion(ser, cockpitAddress):
	ser.write(_packBytes([CMDgetVersion, cockpitAddress]))
	ch = ser.read(11)
	return _unpackBytes(ch)

def setProgram(ser, cockpitAddress, program):
	ser.write(_packBytes([CMDsetProgram, cockpitAddress, program]))
	ch = ser.read(4)

def setPerson(ser, cockpitAddress, number, personArray):
	param = [CMDsetPerson, cockpitAddress, number, personArray[0], personArray[1], personArray[2], personArray[3], 0, 0, 0, 0, 0, 0, 0, 0]
	ser.write(_packBytes(param))
	ch = ser.read(16)