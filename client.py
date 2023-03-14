import socket
from picamera import PiCamera
import numpy as np
from gpiozero import LED, Button
from time import sleep
import RPi.GPIO as GPIO

HOST = '192.168.234.23'
PORT = 9096

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

camera = PiCamera()

GPIO.setmode(GPIO.BCM)

led = LED(17)
led2 = LED(27)
#led2.on()
# button = Button(27)
GPIO.setup(3, GPIO.IN)

while True:
	#print(led2.is_active)
	#try:
	#	client.connect((HOST, PORT))
	#except:
	#	print(GPIO.input(3))
	if GPIO.input(3) == 0:
		print("Eye is blinked")
		led.on()
		camera.start_preview()
		camera.capture("./image.jpg")
		camera.stop_preview()
		try:
			file = open('image.jpg', 'rb')
			print("Sending images")
			image_data = file.read(1024)
			while image_data:
				client.send(image_data)
				image_data = file.read(1024)
				print(image_data)
			client.send(image_data)
			print(str(image_data)+" Last msg sent!!")
			file.close()
			file = open('image.jpg', 'rb')
			image_data = file.read(1024)
			while image_data:
				client.send(image_data)
				image_data = file.read(1024)
				print(image_data)
			client.send(image_data)
			file.close()
			led.off()
		except:
			print("Image sent")
		dataServer = client.recv(1024)

		# print(dataServer.decode('utf-8'))
		print("Received Data", dataServer.decode('utf-8'))
		if (dataServer.decode('utf-8') == "redLED"):
			if (led2.is_active == False):
				led2.on()
			else:
				led2.off()

		client.close()
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.connect((HOST, PORT))
		#except:
			#client.close()
			# client.connect((HOST, PORT))
	else:
		led.off()

client.close()