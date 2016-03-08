# User configuration
#

from daumcommands import *

SERIAL_PORT = '/dev/ttyUSB0'	
cockpitAddress = 0							# extracted with sGetAddress

C_PERSONS = ['Guest', 'Jule', 'Micha']	# put names of training people here; don't delete guest
C_PERSON = []
# provide details for training people: age, sex, height, weight
C_PERSON.append([37, C_PERSON_SEX_FEMALE, 175, 67])
C_PERSON.append([37, C_PERSON_SEX_MALE, 200, 120])