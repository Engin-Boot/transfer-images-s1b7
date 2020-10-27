import paho.mqtt.publish as publish
msg= input("Enter the Image Name")
try:
    publish.single("ImageName", msg , hostname="mqtt.eclipse.org")
except:
    print("Failed to Connect")
