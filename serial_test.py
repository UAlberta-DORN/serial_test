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
                time.sleep(0.03)
                self.ser.flushInput()
                self.ser.flushOutput()
                time.sleep(0.03)
            except:
                try:
                    self.ser.close()
                except:
                    pass
                self.connect_serial(patience = patience-1)
        else:
            print("Error: cannot connect to the Hub\n")
            
    def reset_device(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        time.sleep(0.03)
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
        ser_bytes = self.ser.readline()
        decoded_bytes = (ser_bytes[0:len(ser_bytes)-2].decode("ISO-8859-1"))
        try:
            self.message = json.loads(decoded_bytes)
        except:
            # self.get_message(patience = patience-1)
            pass
    def send_object(self, json_obj = {}):
        if json_obj == {}:
            print("Please send something useful, thank you")
            return
        mesg_to_send = json.dumps(json_obj).encode('utf-8')
        self.ser.write(mesg_to_send)
        
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

try:
    hub.close_connection()
except:
    pass
hub = hub_serial('COM7', 115200, timeout=10)
try:
    print("Connecting Serial...")
    hub.connect_serial()
    command_object = [{'command':'Callback','id':["3C:61:05:3D:D3:79", "3C:61:05:3D:D4:ED", "7C:9E:BD:F4:06:69"]}]
    hub.send_object(command_object)
    for i in range(100):
        print(f'In loop {i}\n')
        # hub.connect_serial()
        hub.get_message()
        print(hub.message)
        
        # hub.close_connection()
        time.sleep(0.5)
except:
    pass
hub.close_connection()
# hub.reset_device()
