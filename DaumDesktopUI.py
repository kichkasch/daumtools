# DaumDesktopUI
#
# Program connects to your Daum ergo_lyps 8080 TRS pro home trainer through serial port; 
# allows for making basic training configurations and visualizes (terminal UI) training data
# (background: display of my home trainer broke)
#
# Michael Pilgermann (kichkasch@gmx.de)
# 2016-03-08
#

import struct 
import time
from blessings import Terminal
from config import *
from daumcommands import *
from daumlib import *


def niceEndless(ser, cockpitAddress):
	t = Terminal()
	with t.fullscreen():
		while True:
			print t.clear()
			runData = getRunDaten(ser, cockpitAddress)
			with t.location(10, 2):
				print "Person: " + C_PERSONS[runData[C_RUN_PERSON]]
			with t.location(10, 3):
				print "Programm: " + str(runData[C_RUN_PROGRAM])
			with t.location(10, 4):
				progressBar = " " + "#" * (runData[C_RUN_RPM] / 2) 
				print "Umdrehungen: " + str(runData[C_RUN_RPM]) + " [" + progressBar
			with t.location(124, 4):
				print "]"
			time.sleep(1)



ser = initConnection()

setProgram(ser, cockpitAddress, C_PROGRAM_INTERVAL_MID)
time.sleep(1)
setPerson(ser, cockpitAddress, 1, C_PERSON[0]) 
time.sleep(1)

niceEndless(ser, cockpitAddress)
ser.close()  