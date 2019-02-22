#!/usr/bin/python

import serial, os

class Graphtec():
    def Run(self, filename):
        print(os.path)
        # cut_file = os.listdir('./CUT_NOW')[0]
        s = serial.Serial("/dev/ttyS0", 9600, stopbits=serial.STOPBITS_TWO)
        s.write(open(filename,"r").read())
        s.close()
        # os.rename("./CUT_NOW/"+cut_file, "./CUT_DONE/"+cut_file)