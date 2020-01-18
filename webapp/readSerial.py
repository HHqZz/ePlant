# You will need the pyserial module :
#       pip3 install pyserial
#
import serial    

def read():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5) # open serial port with 5s timeout
    print("PANAME CEST LA VIEIIIIIIIIIIIIIi")
    while(1):
        msg = ser.readline().decode('utf-8')
        array = (msg.rstrip()).split(":") # retire la nouvelle ligne puis sépare l'identifiant de la valeur
        if array[0] == "TEMP":
            print(array[1] + "°C")
        elif array[0] == "HUMI":
            print(array[1] + "%")
        elif array[0] == "MOIS":
            print(array[1] + " (sans unitée)")
    ser.close()     