import serial
import time

arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)

def write_read(x):
    arduino.write(x.encode())
    time.sleep(0.05)
    data = arduino.readline()
    return data


while True:
    num = input("Enter a number: ")
    value = write_read(num)
    print(value)