import RPi.GPIO as GPIO
import serial
from time import time, sleep
import sys

uart = serial.Serial("/dev/ttyS0", baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=8, timeout=1)

sreadlen = 1024 # max number of chars to read from serial in one try 

def AT_test():
	while True:
		if not uart.inWaiting():
			user_input = input('Insert AT command:  ')
			uart.write((user_input + "\r\n").encode('utf-8'))

			timestamp = time()
			log_file.write(str(timestamp) + ": \n")
			log_file.write("Command: \n" + user_input + '\n\n')

		sleep(0.1)
		received_data = ''
		if uart.inWaiting():
			received_data += (uart.read(uart.inWaiting())).decode('utf-8')
			sleep(0.03)
			log_file.write("Response: \n" + received_data + '\n\n')
			print(received_data)

def connect_test():
    uart.write(('AT').encode('utf-8'))
    print('Status połączenia z modułem LoRa: \n')
    readData()
    print('\n\n')

def get_data(node):
    

def main():
    connect_test()



if __name__ == "__main__":
	while True:
        main()