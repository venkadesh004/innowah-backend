from flask import Flask, request
import torch
import cv2
import pandas
from model import model_output

app = Flask(__name__)

i = 0

@app.route('/', methods=["GET"])
def getData():
    with open('ledState.txt', 'r') as data:
        return data.read()
    
@app.route('/toggle', methods=["POST"])
def toggleData():
    with open('ledState.txt', 'r') as data:
        prevData = data.read()
        print(prevData)
    if prevData == "on":
        with open('ledState.txt', 'w') as writer:
            writer.write("off")
    else:
        with open('ledState.txt', 'w') as writer:
            writer.write("on")
    
    return "Done"
    
@app.route('/postData', methods=["GET", "POST"])
def addData():
    # print(data)
    img = request.get_data()
    # print(img[115:len(img)-15])
    # with open('iState.txt', 'r') as iState:
    #     i = iState.read()

    # i = int(i)

    with open("./finalImage.jpg", "wb") as fileWriter:
        # i = 0
        image = img[115:len(img)-15]
        fileWriter.write(image)

    # i += 1

    # with open('iState.txt', 'w') as iState:
    #     iState.write(str(i))

    result = model_output(cv2.imread('./finalImage.jpg'))
    print(result)
    if len(result.xyxy[0].numpy()) > 0:
        print(result.pandas().xyxy[0].name[0])
        if (result.pandas().xyxy[0].name[0] == "led"):
            with open('ledState.txt', 'r') as data:
                prevData = data.read()
            print(prevData)
            if prevData == "on":
                with open('ledState.txt', 'w') as writer:
                    writer.write("off")
            else:
                with open('ledState.txt', 'w') as writer:
                    writer.write("on")
    
    return "Done"

if __name__ == "__main__":
    app.run(debug=True)