#!/usr/bin/python
# -*- coding: utf8 -*-


import time

fileTurns = open('turns.txt', 'r')
turns = fileTurns.read()
max_turns = turns

while 1:
	file = open('variables.txt','w')
	
	fileSpeed = open('vitesse1.txt', 'r')
	speed = fileSpeed.read()
	fileSpeed.close()	

	fileRfid = open('rfid.txt', 'r')
	rfid = fileRfid.read()
	fileRfid.close()
	
	fileBattery = open('battery.txt', 'r')
	battery = fileBattery.read() 
	file.Battery.close()

	turns = fileTurns.read()
	fileTurns.close()
	

	print "\t","speed: ", speed, "km/h"
	file.write(str(speed) + '\n')

	print "\t","turns: ", turns,"/", max_turns
	file.write(str(turns) + '\n')

	print "\t","battery: ", battery, "%"
	file.write(str(battery) + '\n')

	file.close()

	print "\n" * 10 #Clear de l'écran
	time.sleep(1) #Wait  1 sec
