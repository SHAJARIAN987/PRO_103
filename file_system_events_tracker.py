import sys
import time
import os
import shutil
import random
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/home/arshiaj87/Python_Projects/PRO_102/Downloads"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey! {event.src_path} has been created.")
    def on_deleted(self, event):
        print(f"Woah! {event.src_path} was just deleted.")
    def on_moved(self, event):
        print(f"{event.src_path} was moved.")
    def on_modified(self, event):
        print(f"This just in! {event.src_path} has been modified.")

event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive = True)
observer.start()


try:
    while True:
        time.sleep(2) 
        print("running...")
except KeyboardInterrupt:
    print("Stopped!")
    observer.stop