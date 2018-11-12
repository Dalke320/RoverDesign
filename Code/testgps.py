
import gps
import subprocess
import time


session = gps.gps()
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
myfile = open('/home/rover/rovercode/gpsresults.txt','a')
resetfile = open('/home/rover/rovercode/gpsresults.txt','w')



def time():
	print("Time works" )
	try:
		while 1:
			report = session.next()
			if report['class'] == 'TPV':
				if hasattr(report, 'time'):
					print (report.time)
					myfile.write("The time is: " + str(report.time) + "\n")
	except KeyboardInterrupt:
		print("Exiting time")


def position():
	print("Postion works" )
	try:
		while 1:
			report = session.next()
			if report['class'] == 'TPV':
				if hasattr(report, 'lon'):
					print (report.lon)
					myfile.write("Longitude: " + str(report.lon) + "\n")
				if hasattr(report, 'lat'):
					print (report.lat)
					myfile.write("Lattitude: " + str(report.lat) + "\n")
				if hasattr(report, 'lon'):
					print (report.speed)
					myfile.write("Speed: " + str(report.speed) + "\n")
			#time.sleep(2)
	except KeyboardInterrupt:
		print("Exiting Postion")



try:
	while 1:
		print("Please enter a command: " )
		print("1. Report time")
		print("2. Start reporting Latitude, Longitude and Speed, hit Ctrl+c to stop" )
		print("3. close")
		print("4. Clear the gps results file")
		var = raw_input()
		if var == '1':
			print("current time" + "\n")
			time() 
		if var == '2':
			print("Postion info" + "\n")
			position()
		if var == '3':
			myfile.close
			quit()
		if var == '4':
			resetfile.write("")
			
			
except:
	print("Disguise's my errors as a successful exit")
	#gatt = subprocess.Popen(['exit'])

