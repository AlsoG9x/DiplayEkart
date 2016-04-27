#!/usr/bin/python
# -*- coding: utf8 -*-


import random, os, time

turns = 6 #nombre de tours donner par le conducteur
max_turns = turns
battery = 47

while 1:
    file = open('variables.txt','w')
    
    #Quand le Capteur à effet Hall détecte la vitesse on l'affiche ici
    speed = random.randrange(0,30)
    print "\t","speed: ", speed, "km/h"
    file.write(str(speed) + '\n')
    
    #Quand le Capteur de tours détecte un tours on décrémente la variable
    print "\t","turns: ", turns,"/", max_turns
    file.write(str(turns) + '\n')

    #Quand la tension batteries diminue on décrémente la variable
    print "\t","battery: ", battery, "%"
    file.write(str(battery) + '\n')

    file.close()

    print "\n" * 10 #On 'clear' l'écran à chaque fois
    if(speed > 15):
        battery = battery - 1 #Simulation
    if(speed > 26):
        turns = turns - 1 #Simulation
    time.sleep(1)
    #Attendre 1 seconde sinon l'écran est clear trop souvent
