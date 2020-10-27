import paho.mqtt.client as mqtt
from tempfile import NamedTemporaryFile
import shutil
import csv

def OpenAndUpdateCSVFile(DiagnosedImageName):
    filename =r"D:\transfer-images-s1b7\MC3File\status.csv"
    tempfile = NamedTemporaryFile(mode='w', delete=False)

    fields = ['IMAGE_NAME','DIAGNOSIS_STATUS']
    with open(filename, 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields)
        for row in reader:
            if row['IMAGE_NAME'] ==DiagnosedImageName:
                print('updating row', row['IMAGE_NAME'])
                row['IMAGE_NAME'], row['DIAGNOSIS_STATUS'] = row['IMAGE_NAME'],"Completed"
            row = {'IMAGE_NAME': row['IMAGE_NAME'], 'DIAGNOSIS_STATUS': row['DIAGNOSIS_STATUS']}
            writer.writerow(row)
    shutil.move(tempfile.name, filename)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("DiagonosedImageName")
   


def on_message(client, userdata, msg):
    OpenAndUpdateCSVFile(msg.payload.decode("utf-8"))
    print(msg.topic+" "+(msg.payload).decode("utf-8"))
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
    
client.connect("mqtt.eclipse.org", 1883, 60)
    
client.loop_forever()
