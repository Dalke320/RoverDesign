import pexpect
import time
try:
	while 1:

		child = pexpect.spawn("git add Heart1results.txt Heart2results.txt gpsresults.txt")
		child = pexpect.spawn("git commit -m 'Log file update'")
		child = pexpect.spawn("git push https://Dalke320:Roverdesign320@github.com/Dalke320/RoverDesign.git master")
		print("Something is happening!")
		time.sleep(1)

except KeyboardInterrupt:
	child = pexpect.spawn("exit")
