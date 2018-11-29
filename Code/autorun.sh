#!/bin/bash

cd /home/pi/Desktop/RoverDesign/Code

xterm -e sudo python2 Heartread1.py -hold & 
xterm -e  sudo python2 Heartread2.py -hold & 
xterm -e  sudo python testgps.py -hold 


