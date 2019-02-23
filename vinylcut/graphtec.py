#!/usr/bin/python

import serial, os

class Graphtec():
    def __init__(self):
        return
        self.s = serial.Serial("/dev/ttyS0", 9600, stopbits=serial.STOPBITS_TWO)

    def Run(self, filename):
        return
        print(os.path)
        # cut_file = os.listdir('./CUT_NOW')[0]
        s.write(open(filename,"r").read())
        s.close()
        # os.rename("./CUT_NOW/"+cut_file, "./CUT_DONE/"+cut_file)

    def Stop(self):
        self.s.reset_output_buffer()
        s.close()

    def Pause(self):
        self.s.set_output_flow_control(True)

    def UnPause(self):
        self.s.set_output_flow_control(False)