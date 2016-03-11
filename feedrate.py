#!/usr/bin/env python2
# Quick and Dirty Python Script for calculating feedrates in a 3D printer

print ("Extruder Feed Rate Calibration Aid\n----------------------------------\n")
erate = float(raw_input("Feed Rate (steps): "))
dlength = float(raw_input("Desired Length: "))
alength = float(raw_input("Actual Length: "))

newfeed = (dlength * erate) / alength
print ("\nSet the new feed rate to " + str(round(newfeed, 3)))
