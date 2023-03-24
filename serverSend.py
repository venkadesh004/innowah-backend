import socket
import cv2
import numpy as np
import os
from time import sleep
import datetime
import torch
import pandas
import pickle

# host = socket.gethostbyname(socket.gethostname())

HOST = '192.168.9.23'
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
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

# model = torch.hub.load('ultralytics/yolov5', 'custom',  path='./last.pt')

while True:
    print("New connection")
    client_socket, address = server.accept()
    print(client_socket, address)
    print(type(client_socket))


    # file = open("image.jpg", "wb")
    # image_chunk = client_socket.recv(1024)

    # print(image_chunk)

    # i = 0

    # # while i <= 450:
    # #     file.write(image_chunk)
    # #     image_chunk = client_socket.recv(1024)

    # while i <= 1000:
    #     file.write(image_chunk)
    #     image_chunk = client_socket.recv(1024)

    #     i += 1

    # with open("fileToWrite.jpg", "wb") as fileWriter:
    #     i = 0
    #     printingFlag = 0
    #     while True:
    #         data = client_socket.recv(1024)
    #         print(data)
    #         # print(type(data))
    #         if data == b'':
    #             break
    #         else:
    #             printingFlag = 1
    #         # if data.decode() == "flag":
    #         #     break
    #         fileWriter.write(data)
    #         # print("just wrote data", i)
    #         i += 1
    #     print("I have finished writing", i)

    # if printingFlag == 1:
    #     img = cv2.imread("./fileToWrite.jpg")
    #     print("Image", img)
        # cv2.imshow("Image", img)

    # file.close()
    # file.close()
    # print(img)
    # client_socket.close()
    # print("Detecting LED in image")
    # result = model(cv2.cvtColor(cv2.imread('./image.jpg'), cv2.COLOR_BGR2RGB))
    # print(result)

    # if len(result.xyxy[0].numpy()) > 0:
    #     if (result.pandas().xyxy[0].name[0] == "redLED"):
    #         client_socket.send(str(result.pandas().xyxy[0].name[0]).encode('utf-8'))
    #     else:
    #         client_socket.send("NotREDLED".encode('utf-8'))
    # else:
    #     client_socket.send("NotREDLED".encode('utf-8'))  
    # 

    inputData = int(input("Enter (1/0): "))
    if (inputData == 1):
        client_socket.send("on".encode('utf-8'))
    else:
        client_socket.send("off".encode('utf-8'))      

    client_socket.close()

# cv2.destroyAllWindows()