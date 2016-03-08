# daum internals
# provided in serial port documentation

CMDgetAddress = 0x11
CMDrunDaten = 0x40
C_RUN_PROGRAM = 2	# 0-79
C_RUN_PERSON = 3	# 0 - 4
C_RUN_ACTIVE = 4	# 0 inactive; 1 active
C_RUN_POWER = 5		# in Watt; multiply by 5
C_RUN_RPM = 6		# Round per minute (0..199)
C_RUN_SPEED = 7		# speed (before comma)
C_RUN_DISTANCE_A = 8	# overall distance in 100 m
C_RUN_DISTANCE_B = 9	# overall distance in 100 m
C_RUN_GEAR = 16		# Gear
CMDsetGear = 0x53	# 1-28
CMDgetVersion = 0x73
C_VER_COCKPIT_TYPES = ["Cardio", "Fitness", "Vita De Luxe", "8008", "8080", "Therapie"]
CMDsetProgram = 0x23	# 0-79
C_PROGRAM_INTERVAL_MID = 4	# medium interval training, 34 minutes
CMDsetPerson = 0x24
C_PERSON_SEX_MALE = 0
C_PERSON_SEX_FEMALE = 1