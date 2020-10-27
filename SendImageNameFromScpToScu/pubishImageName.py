import time
import paho.mqtt.publish as publish
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

def on_created(event):
    msg = f"{event.src_path[33:]}"  #Body of the mail
    try:
        publish.single("writingImageName", msg, hostname="mqtt.eclipse.org")
    except:
        print("Failed to Connect and Publish")
       

my_event_handler.on_created = on_created

path = r"D:\transfer-images-s1b7\Receiver"  # (Receiver folder)
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

my_observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()

