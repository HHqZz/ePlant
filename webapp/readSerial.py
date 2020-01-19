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
            #print(array[1] + "°C")
            w_file(array[1],1)
        elif array[0] == "HUMI":
            #print(array[1] + "%")
            w_file(array[1],2)
        elif array[0] == "MOIS":
            w_file(array[1],3)
            #print(array[1] + " (sans unitée)")
    ser.close()     


def w_file(var, n_file):
    f = None
    if n_file == 1:
        f = open("temperature.txt", "w")
    if n_file ==2:
        f=open("humidite.txt","w")
    if n_file == 3:
        f=open("water.txt","w")
    f.write(var)
    f.close()