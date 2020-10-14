import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import Sendmail

if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

def on_created(event):
    msg = f"{event.src_path} has been Generated.\n Please Have a look!!"
    Sendmail.sendMail(msg)

my_event_handler.on_created = on_created

path = "..\Receiver"  #Receiver folder
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

