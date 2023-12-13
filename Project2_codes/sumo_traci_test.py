
#!/usr/bin/env python 

""" 
@file    sumo_traci_test.py
@author  Xiaoliang Ma
@date    2018-11-08
@version $Id$

Test via TraCI interface

Updated: 2021-11-12

""" 

import os, subprocess, sys, socket, time, struct, random, math, numpy

# define the path of sumo in computer

if 'SUMO_HOME' in os.environ:
	sumo_path=os.environ['SUMO_HOME']
else:
    # edit path
    sumo_path = '/usr/local/Cellar/sumo/1.9.2_2/share/sumo'

sys.path.append(os.path.join(sumo_path, 'tools'))
sys.path.append(os.path.join(sumo_path, 'bin'))

import traci

conf_file = "sumo_test.sumo.cfg"
sumo_cmd=["sumo-gui", "-c", conf_file]
traci.start(sumo_cmd)

# simulation loop with configured simulation time
i = 1
laststep = 1800

while i < laststep:
    traci.simulationStep()
    IDList = traci.vehicle.getIDList()
    # print the vehicle info when not empty
    if len(IDList):
        print(i, IDList)
    i=i+1
traci.close()
print("SUMO simulation finished!")



