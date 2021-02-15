# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 01:30:25 2021

@author: Ray Liu
"""


import serial
import time
import json

class hub_serial:
    def __init__(self, comm_port, baud_rate = 115200, timeout = 10, patience = 5):
        self.comm_port = comm_port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.patience = patience
        self.message = {}
        
    def connect_serial(self, patience = None):
        if patience == None:
            patience = self.patience
        if patience >= 0:
            try:   
                self.ser = serial.Serial(self.comm_port, self.baud_rate, timeout=self.timeout)
                self.ser.flushInput()
            except:
                try:
                    self.ser.close()
                except:
                    pass
                self.connect_serial(patience = patience-1)
        else:
            print("Error: cannot connect to the Hub\n")
            
    def reset_device(self):
        self.ser.setDTR(False) 
        time.sleep(0.03)    
        self.ser.setDTR(True)  
        time.sleep(0.03)
        
    def close_connection(self):
        self.ser.close()
        
    def get_message(self, patience = None):
        if patience == None:
            patience = int(self.patience)
        elif patience == 1:
            self.reset_device()
            self.get_message(patience = 0)
        elif patience < 0:
            return
        # print(f'patience = {patience}\n')
        time.sleep(0.03)
        self.ser.flushInput()
        time.sleep(0.03)
        ser_bytes = self.ser.readline()
        decoded_bytes = (ser_bytes[0:len(ser_bytes)-2].decode("ISO-8859-1"))
        try:
            self.message = json.loads(decoded_bytes)
        except:
            # self.get_message(patience = patience-1)
            pass
    

# ser = serial.Serial('COM7', 115200, timeout=10)
# ser.flushInput()
# for i in range(10):
#     ser_bytes = ser.readline()
#     decoded_bytes = (ser_bytes[0:len(ser_bytes)-2].decode("ISO-8859-1"))
#     print(decoded_bytes)
#     # hub_message = json.loads(decoded_bytes)
#     # print(hub_message)
#     time.sleep(0.01)

# ser.close()


hub = hub_serial('COM7', 115200, timeout=10)

for i in range(100):
    print(f'In loop {i}\n')
    hub.connect_serial()
    hub.get_message()
    print(hub.message)
    hub.close_connection()
    time.sleep(0.5)