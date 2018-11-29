
import sys
import subprocess
import os

import pexpect

MAC = "00:22:D0:D8:F5:22"

	


	
def battery():
	child = pexpect.spawn("gatttool -I")
	child .sendline("connect 00:22:D0:D8:F5:22")
	child.sendline("connect")
	#child.expect("Attempting to connect to 00:22:D0:CD:34:6A")
	child.expect("Connection successful", timeout = 15)
	print("Conencted successfully")
	child.sendline("char-read-hnd 27")
	child.expect("Characteristic value/descriptor: ", timeout=10)
	child.expect("\r\n", timeout=10)
	print("charge: "),
	print(int(child.before,16), "%")


def heartread():
	child = pexpect.spawn("gatttool -I")
	child .sendline("connect 00:22:D0:D8:F5:22")
	child.sendline("connect")
	#child.expect("Attempting to connect to 00:22:D0:CD:34:6A")
	child.expect("Connection successful", timeout = 15)
	print("Conencted successfully")
	try:
		while 1:
			child.sendline("char-write-req 0x0013 0100")
			child.expect("Characteristic value was written successfully")
			child.expect("Notification handle = 0x0012 value: ", timeout = 10)
			child.expect("\r\n", timeout = 10)
			h = int(child.before[2:5],16)
			print(h, "bpm")
			myfile = open('/home/pi/Desktop/RoverDesign/Code/Heart2Results.txt','a')
			myfile.write(str(h) + "\n")
			
	
	except KeyboardInterrupt:
		child.sendline("char-write-req 0x0013 0000")
		child.expect("Characteristic value was written successfully")
	myfile.close
	
def heartread2():

	child = pexpect.spawn("sudo gatttool -t random -b 00:22:D0:D8:F5:22 -I connect")
	child .sendline("connect 00:22:D0:D8:F5:22")
	child.sendline("connect")
	#child.expect("Attempting to connect to 00:22:D0:CD:34:6A")
	child.expect("Connection successful", timeout = 15)
	print("Conencted successfully")

	try:
		while 1:
			child.sendline("char-write-req 0x0013 0100")
			child.expect("Characteristic value was written successfully")
			child.expect("Notification handle = 0x0012 value: ", timeout = 10)
			child.expect("\r\n", timeout = 10)
			h = int(child.before[2:5],16)
			print(h, "bpm")
			myfile = open('/home/pi/Desktop/RoverDesign/Code/Heart2Results.txt','a')
			myfile.write(str(h) + "\n")
			
	
	except KeyboardInterrupt:
		child.sendline("char-write-req 0x0013 0000")
		child.expect("Characteristic value was written successfully")
	myfile.close
def close():
	gatt = subprocess.Popen(['exit'])
try:
	while 1:
		print("Please enter a command: " )
		print("1. Reset Log file.")
		print("2. Read the battery life of the monitor. If option 1 fails." )
		print("3. Start monitoring heartrate data. Crtl + c to stop" )
		print("4. Start monitoring heartrate data if 3 does not work." )
		print("5. Exit cmd")
		var = input()
		if var == 1:
			myfile = open('/home/pi/Desktop/RoverDesign/Code/Heart2Results.txt','w')
			myfile.write("") 
		if var == 2:
			battery()
		if var == 3:
			heartread2()
		if var == 4:
			heartread()
		if var == 5:
			quit()
			
			
except:
	print("Disguise's my errors as a successful exit")



