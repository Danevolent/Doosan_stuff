#!/usr/bin/env python
""""
Prototype program to constantly monitor the state of a Doosan Cobot through modbus TCP,
printing the result in terminal.

Requires device running this program to be connected to a Doosan Cobot
"""
from time import sleep
from pymodbus.client.sync import ModbusTcpClient

__author__ = "Daniel Philbey"
__copyright__ = "Copyright 2022, Daniel Philbey"
__credits__ = []

__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Daniel Philbey"
__email__ = "daniel.philbey@gmail.com"
__status__ = "Prototype"

# Robot IP address, should be something like 192.168.127.100
ROBOT_IP = '192.168.127.100' 

# State lookup to get description of register value
STATE_LOOKUP = ["INITIALIZING","STANDBY",\
    "OPERATING", "SAFE OFF",\
    "TEACHING", "SAFE STOP",\
    "EMERGENCY STOP", "HOMING",\
    "RECOVERY", "SAFE STOP2",\
    "SAFE OFF2=10","NOT READY"]

def monitor_and_print(address=ROBOT_IP, port=502, unit_id=1):
    """Monitors the Robot State holding register."""

    # Initialise modbus connection
    robot = ModbusTcpClient(host=ROBOT_IP, port=502, unit_id=1, auto_open=True)

    # main loop
    while(1):
        if robot.connect(): # if connection is successful
            # while(robot.connect()) might be better, but unsure without testing
            while(1):   # loop indefinitey. 
                # read the 'Robot State' holding register
                state_val = robot.read_holding_registers(259, 1) 
                # if value returned, print state
                if state_val is not None:
                    print(f'Robot state: {STATE_LOOKUP[state_val]}')
                else:
                    print("Read error")
                sleep(0.5)  # wait 0.5 seconds

if __name__ == "__main__":
    """Monitor and print state, if called from commandline"""
    monitor_and_print()
