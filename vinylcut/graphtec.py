#!/usr/bin/python

import serial, os

class Graphtec():
    def __init__(self):
        self.s=None
        try:
            self.s = serial.Serial("/dev/ttyUSB0", 9600, stopbits=serial.STOPBITS_TWO)
        except serial.serialutil.SerialException:
            print("Failed to open serial port")

    def Run(self, filename):
        if self.s:
            print(os.path)
            # cut_file = os.listdir('./CUT_NOW')[0]
            self.s.write(str.encode(open(filename,"r").read()))
            # self.s.close()
            # os.rename("./CUT_NOW/"+cut_file, "./CUT_DONE/"+cut_file)
            return True
        else:
            return False

    def Stop(self):
        self.s.reset_output_buffer()
        # self.s.close()

    def Pause(self):
        self.s.set_output_flow_control(True)

    def UnPause(self):
        self.s.set_output_flow_control(False)