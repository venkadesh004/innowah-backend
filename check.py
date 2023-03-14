import torch
import cv2
import numpy

model = torch.hub.load('ultralytics/yolov5', 'custom', path='./last.pt')

results = model(cv2.cvtColor(cv2.imread('./1.jpeg'), cv2.COLOR_BGR2RGB))

string = """
Empty DataFrame
Columns: [xmin, ymin, xmax, ymax, confidence, class, name]
Index: []
"""

print(type(results))
print()
print()
print(results.pandas().xyxy[0].name[0])
print()
print()
print()
print(str(results.pandas().xyxy[0]))
print()
print()
print(string)
print()
print()
if (str(results.pandas().xyxy[0]) == string):
    print(True)
else:
    print(False)
print()
print()
print(len(results.xyxy[0].numpy()))
print()
print()
print(dir(results))