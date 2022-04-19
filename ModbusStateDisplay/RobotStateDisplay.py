#!/usr/bin/env python
""""Prototype program to constantly monitor the state of a Doosan Cobot through modbus TCP,
printing the result in terminal."""

# Built-in modules
from time import sleep
# 3rd party modules
from pymodbus.client.sync import ModbusTcpClient
# Personal modules

__author__ = "Daniel Philbey"
__copyright__ = "Copyright 2022, Daniel Philbey"
__credits__ = []
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Daniel Philbey"
__email__ = "daniel.philbey@gmail.com"
__status__ = "Prototype"


# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or 
# (at your option) any later version.

#This program is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
# GNU General Public License for more details.

#You should have received a copy of the GNU General Public License 
# along with this program. If not, see <https://www.gnu.org/licenses/>.



# Robot Modbus constants
ROBOT_IP = '192.168.127.100'  # Address here, should be something like what's provided (can't remember)

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
        if robot.connect(): # If connection is successful
            while(1):   # loop indefinitey. (whilerobot.connect() might be better, but unsure without testing)

                state_val = robot.read_holding_registers(259, 1)    # read the 'Robot State' holding register 259

                if state_val is not None:
                    print(f'Robot state: {STATE_LOOKUP[state_val]}')
                else:
                    print("Read error")

                sleep(0.5)

if __name__ == "__main__":
    monitor_and_print()
