# app.py file handles the user input and calls a function accordingly

import sys

def decide(args):
	
	help = """
	------------------TravelManage-----------------
	Flag	Description
	 -h     Show this help command
	 -n		Add new Trip (Opens New Trip)
	 -l		Login to user (Opens Login)
	 -r     Register user (Opens Register Form)
	 -c     Cancels existing trip
	 -s     Shows Existring trip details
	-----------------------------------------------"""


	length = len(args)
	if length == 1:
		print('No Flag Provided add -h flag for help')
		return
	
	if length == 2:
		if args[1] == '-h':
			print(help)
			return
		elif args[1] == '-n':
			print('Added new trip')
			return
		elif args[1] == '-l':
			print('Logged In')
			return

	elif length == 3:
		if args[1] == '-c' and isalnum(args[2]):
			st = None		
			# TODO: ABSTRACT THE CANCELLATION FUNCTION
			return

		elif args[1] == '-s' and isalnum(args[2]):
			st = None
			# TODO: ABSTRACT THE SHOW FUNCTION
			return
			
	else:
		decide(['h'])
		return	

decide(sys.argv)
