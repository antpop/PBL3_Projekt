import requests
import json
import RPi.GPIO as GPIO
import serial
from time import time, sleep
import sys

uart = serial.Serial("/dev/ttyS0", baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=8, timeout=1)

def readData():
    received_data=' '
    received_data += (uart.read(uart.inWaiting())).decode('utf-8')
    print(received_data)

def connect():
    uart.write(('AT+CGDCONT?').encode('utf-8'))
    print('Informacje o stanie sieci: \n')
    readData()
    print('\n\n')
    uart.write(('AT+CGDCONT=1,"IPv4v6","plus"').encode('utf-8'))
    readData()
    print('\n\n')
    uart.write(('AT+NETOPEN').encode('utf-8'))
    readData()
    print('\n\n')
    uart.write(('AT+IPADDR').encode('utf-8'))
    print('Adres IP:\n')
    readData()
    print('\n\n')
    uart.write(('AT+HTTPINIT').encode('utf-8'))
    readData()
    print('\n\n')
    uart.write(('AT+HTTPPARA="URL", "https://hub1li4sqe.execute-api.eu-central-1.amazonaws.com/pbl3/info"').encode('utf-8'))
    readData()
    print('\n\n')
    uart.write(('AT+HTTPACTION=0').encode('utf-8'))
    readData()
    print('\n\n')
    length=255
    uart.write((f'AT+HTTPREAD=0,{length}').encode('utf-8'))
    readData()
    print('\n\n')
    uart.write(('AT+HTTPPARA="URL", "https://hub1li4sqe.execute-api.eu-central-1.amazonaws.com/pbl3/db"').encode('utf-8'))
    readData()
    print('\n\n')
    uart.write(('AT+HTTPDATA=64,1000').encode('utf-8'))
    uart.write(("{'lastNames': 'Popecki,Roszczyk,Szczepaniak', 'moduleID':'1'}").encode('utf-8'))
    readData()
    print('\n\n')
    uart.write(("AT+HTTPACTION=1").encode('utf-8'))
    readData()
    print('\n\n')
    uart.write(("AT+HTTPHEAD").encode('utf-8'))
    readData()
    print('\n\n')
    uart.write(("AT+HTTPTERM").encode('utf-8'))
    readData()
    print('\n\n') 



def postget():
    geturl='https://hub1li4sqe.execute-api.eu-central-1.amazonaws.com/pbl3/info'
    posturl='https://hub1li4sqe.execute-api.eu-central-1.amazonaws.com/pbl3/db'

    x = requests.get(geturl)
    print(x)
    getdata=x.json()
    print(getdata)

    datatosend={'lastnames': 'Popecki,Roszczyk,Szczepaniak', 'moduleID':'1'}
    requests.post(posturl, json = datatosend)


connect()
