import pycontext  # Ensures paho is in PYTHONPATH
import paho.mqtt.publish as publish
msg= input("Enter the Image Name")
publish.single("ImageName", msg , hostname="mqtt.eclipse.org")
