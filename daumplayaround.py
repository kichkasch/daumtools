import struct 
import time
from blessings import Terminal
from config import *
from daumcommands import *
from daumlib import *

def runEndless(ser, cockpitAddress):
	while True:
		runData = getRunDaten(ser, cockpitAddress)
		print "Programm: " + str(runData[C_RUN_PROGRAM]) + "| Person: " + C_PERSONS[runData[C_RUN_PERSON]] +  " | Umdrehungen: " + str(runData[C_RUN_RPM])
		time.sleep(1)


ser = initConnection()
print(ser.name)         # check which port was really used

address = sGetAddress(ser)
print "" + str(address[0]) + ":" + str(address[1])
time.sleep(1)

ver = getVersion(ser, cockpitAddress)
print "Seriennummer: ", ver[2:10] 
print "Cockpit Type: ", ver[10]
time.sleep(1)

# setGear(ser, 28, cockpitAddress)
runData = getRunDaten(ser, cockpitAddress)
print "Programm: " + str(runData[C_RUN_PROGRAM]) + "| Person: " + C_PERSONS[runData[C_RUN_PERSON]] 

#runEndless(ser, cockpitAddress)
ser.close()  
