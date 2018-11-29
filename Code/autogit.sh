#!/bin/bash

cd /home/pi/Desktop/RoverDesign/Code

while true; do
git add Heart1Results.txt Heart2Results.txt gpsresults.txt
git commit -m "Log file update"
git push https://Dalke320:Roverdesign320@github.com/Dalke320/RoverDesign.git master
sleep 1
done
