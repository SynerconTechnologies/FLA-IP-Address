# FLA-IP-Address
A small GUI utility to enter the IP address of the FLA and write it to the synercon.ini file for the RP1210 DLL.

This utility is written in Python quing PyQt5.

The default IP address for the Forensic Link Adapter is 192.168.7.2. This is the default IP for the USB-to-Ethernet connection that is enabled using the BeagleBone Gadget Drivers. 

The utility lets a user enter the IP address displayed one the screen in case they want to use an Ethernet connection. 

In the current state, the entire synercon.ini in the C:\Windows directory will be overwritten. The contents of that file are contained in the source code.


