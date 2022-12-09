import requests
import json
import RPi.GPIO as GPIO
import serial
from time import time, sleep
import sys

uart = serial.Serial("/dev/ttyS0", baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=8, timeout=1)

geturl='https://hub1li4sqe.execute-api.eu-central-1.amazonaws.com/pbl3/info'
posturl='https://hub1li4sqe.execute-api.eu-central-1.amazonaws.com/pbl3/db'

x = requests.get(geturl)
print(x)
getdata=x.json()
print(getdata)

datatosend={'lastNames': 'Popecki,Roszczyk,Szczepaniak', 'moduleID':'2137'}
requests.post(posturl, json = datatosend)

received_data = ''

received_data += (uart.read(uart.inWaiting())).decode('utf-8')
sleep(1)
print(received_data)
