import socket
import cv2
import numpy as np
import os
from time import sleep
import datetime
import torch
import pandas

# host = socket.gethostbyname(socket.gethostname())

HOST = '192.168.179.23'
PORT = 9096

# cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((HOST, PORT))
# 
# server.listen()

# while True:
    # message, address = server.recvfrom(1024)
    # print(f"Connected to {address}")

    # # message = communication_socket.recv(1024).decode('utf-8')

    # # cv2.imshow("Image", message)

    # message = message.decode('utf-8')

    # print(f"Message from client is: {message}")

    # array = list(message)
    # print(array)

    # server.sendto(f"Got your message! Thank you!".encode('utf-8'), address)

    # # server.close()

    # # print(f"Connection with {address} ended!")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

model = torch.hub.load('ultralytics/yolov5', 'custom',  path='./last.pt')

while True:
    print("New connection")
    client_socket, address = server.accept()

    file = open("image.jpg", "wb")
    image_chunk = client_socket.recv(1024)

    i = 0

    while i <= 450:
        file.write(image_chunk)
        image_chunk = client_socket.recv(1024)

        i += 1

    file.close()
    # client_socket.close()
    print("Detecting LED in image")
    result = model(cv2.cvtColor(cv2.imread('./image.jpg'), cv2.COLOR_BGR2RGB))
    print(result)

    if len(result.xyxy[0].numpy()) > 0:
        if (result.pandas().xyxy[0].name[0] == "redLED"):
            client_socket.send(str(result.pandas().xyxy[0].name[0]).encode('utf-8'))
        else:
            client_socket.send("NotREDLED".encode('utf-8'))
    else:
        client_socket.send("NotREDLED".encode('utf-8'))        

    client_socket.close()