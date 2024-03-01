# OMRON FINS SIMULATOR
**Introduction**

This script allows your Ruby-enabled PC to act as a virtual PLC. It was implemented for debugging programs that communicate with PLCs using the FINS protocol.

**Features**

Starts a UDP socket on the specified port (default: 9600) and responds to FINS protocol requests.
Currently, it only supports reading and writing to the DM area and acquiring the date/time.
Does not support the TCP protocol.

**Requirements**

Ruby 1.8 or higher (verified on Linux, MacOSX, and Windows)
PC with Ruby and the PLC must be able to communicate on UDP port 9600 (or other specified port)

**Installation**

1. Clone the project to your PC:
```
git clone https://github.com/hiroeorz/omron-fins-simulator.git
```
2. Run the omron_plc.rb file:
```
ruby omron_plc.rb --address=<IP_address> --port=<port_number>
```

**Example of execution:**
```
cd omron-fins-simulator
ruby omron_plc.rb --address=192.168.0.6 --port=9600
```

**Available options:**
```
$ ruby omron_plc.rb --address=192.168.0.6 --port=9600 --count_up_dm=5095 --countup_interval=5 --load_file=/tmp/dm.yaml
```
- `--address`: IP address of your PC (default: 127.0.0.1)
- `--port`: Port number (default: 9600)
- `--count_up_dm`: Specifies the DM numbers to be automatically incremented (comma-separated)
- `--countup_interval`: Automatic increment interval (default: 5 seconds)
- `--load_file`: DM configuration file to load at startup (YAML format): The DM configuration file is loaded at startup. If not specified, all DM values start at 0. The script can be used to test and debug programs that communicate with Omron PLCs via FINS.

    * DM configuration file (YAML format)
    ```
    3: 0
    100: 11
    101: 21
    102: 0xff
    103: 0x10
    ```


**Setting and acquiring values interactively**

After startup, the script waits for input on the console. 

```
$ ruby omron_plc.rb --address=192.168.0.6 --port=9600

Loading /tmp/test.yaml...done
UDP Socket bind to host:192.168.0.6, port:9600.

----------------------------------------------------
PLC SIMULATOR SYSTEM
----------------------------------------------------
SET DM COMMAND     : > set <dm number>, <value>
GET DM COMMAND     : > get <dm number>
GET DM LIST COMMAND: > get_list <dm number>, <count>
EXIT COMMAND       : > exit
----------------------------------------------------

> 
```

The following commands are available:

- `set <dm_number>, <value>`: Set the value in the DM memory
- `get <dm_number>`: Get the value from the DM memory
- `get_list <dm_number>, <count>`: Get values from a series of consecutive DM addresses
- `exit`: Terminate the program

**Example of interaction:**
```
$ ruby omron_plc.rb --address=192.168.0.6 --port=9600

Loading /tmp/test.yaml...done
UDP Socket bind to host:172.16.15.35, port:9600.

----------------------------------------------------
PLC SIMULATOR SYSTEM
----------------------------------------------------
SET DM COMMAND     : > set <dm number>, <value>
GET DM COMMAND     : > get <dm number>
GET DM LIST COMMAND: > get_list <dm number>, <count>
EXIT COMMAND       : > exit
----------------------------------------------------

> 
> set 1, 100
ok

> set 2, 200
ok

> set 3, 300
ok

> get_list 1, 3
1 : 100
2 : 200
3 : 300

> exit

$
```

**For more information:**
Refer to the GitHub repository: https://github.com/hiroeorz/omron-fins-simulator/blob/master/omron_plc.rb