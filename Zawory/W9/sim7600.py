"""
This file contains functions supporting Waveshare SIM7600X 4G HAT
To start up the module the functions should be executed in the following order:
- power_on

2021 Marcin Kolakowski WUT
"""

import RPi.GPIO as GPIO
import serial
from time import time, sleep
import sys

uart = serial.Serial("/dev/ttyS0", baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=8, timeout=1)

sreadlen = 1024 # max number of chars to read from serial in one try 

log_file = open("log.txt", 'a')

def power_on(power_key=6):
	"""Power on the module

	Parameters
	----------
	power_key : int
		gpio output for sim7600 power control (default: 6)
	"""
	print('Starting SIM7600X')
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(power_key,GPIO.OUT)
	sleep(0.1)
	GPIO.output(power_key,GPIO.HIGH)
	sleep(2)
	GPIO.output(power_key,GPIO.LOW)

	for i in range(20):
		sleep(1)
		sys.stdout.write('.')
		sys.stdout.flush()

	print('\nSIM7600X is ready')

def power_down(power_key=6):
	"""Power down the module

	Parameters
	----------
	power_key : int
		gpio output for sim7600 power control (default: 6)
	"""
	print('Powering down SIM7600X')
	GPIO.output(power_key,GPIO.HIGH)
	sleep(3)
	GPIO.output(power_key,GPIO.LOW)
	for i in range(18):
		sleep(1)
		sys.stdout.write('.')
		sys.stdout.flush()
	print('\nGood bye')


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



if __name__ == "__main__":
	#power_on()
	while True:
		AT_test()
		sleep(5)

