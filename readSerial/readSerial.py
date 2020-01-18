# You will need the pyserial module :
#       pip3 install pyserial
#
import serial    

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5) # open serial port with 5s timeout

while(1):
    print(ser.readline())
    print(ser.readline())
    print(ser.readline())

ser.close()     