#!/usr/bin/python

import serial, os
print(os.path)
cut_file = os.listdir('./CUT_NOW')[0]
s = serial.Serial("/dev/ttyUSB0", 9600, stopbits=serial.STOPBITS_TWO)
s.write(str.encode(open("./CUT_NOW/"+cut_file,"r").read()))
s.close()
os.rename("./CUT_NOW/"+cut_file, "./CUT_DONE/"+cut_file)