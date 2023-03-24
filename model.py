import torch
import cv2

# model = torch.hub.load('ultralytics/yolov5', 'custom',  path='./last.pt')
model = torch.hub.load('./yolov5', 'custom', path='./last.pt', source='local')


def model_output(data):
    return model(data)