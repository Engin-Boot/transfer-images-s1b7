import paho.mqtt.client as mqtt
from tempfile import NamedTemporaryFile
import shutil
import csv
import os

def OpenAndUpdateCSVFile(DiagnosedImageName,csvfilename):
    with open(csvfilename, 'a') as file:
        writer = csv.writer(file)
        if(os.stat(csvfilename).st_size == 0):
            writer.writerow(["IMAGE_NAME","DIAGNOSIS_STATUS"])
            writer.writerow([DiagnosedImageName,"PENDING"])
            file.close();
        else:
            writer.writerow([DiagnosedImageName,"PENDING"])
            file.close();

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("writingImageName")


def on_message(client, userdata, msg):
    csvfilename = r"D:\transfer-images-s1b7\MC3File\status.csv"
    OpenAndUpdateCSVFile(msg.payload.decode("utf-8"),csvfilename)
    print(msg.topic + " " + (msg.payload).decode("utf-8"))


if __name__=="main":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("mqtt.eclipse.org", 1883, 60)
    client.loop_forever()
