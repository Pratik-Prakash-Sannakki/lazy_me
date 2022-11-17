import os
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer 
import time
import json
ext=[]

filepaths = "/Users/pratiksannakki/Desktop/lazy/jj/yo"

class MyHandler(FileSystemEventHandler):
    def on_modified(self,event):
        for filename in os.listdir(filepaths):
            #destpaths= "/Users/pratiksannakki/Documents/hello/Textfile"
            ext= os.path.splitext(filename)[-1].lower()
            if ext == ".txt":
                destpaths= "/Users/pratiksannakki/Desktop/lazy/jj/hello/Textfile"
                src=filepaths+"/"+filename
                dest=destpaths+"/"+filename
                os.rename(src,dest)
            
            elif ext == ".py":
                destpaths= "/Users/pratiksannakki/Desktop/lazy/jj/hello/pythonfile"
                src=filepaths+"/"+filename
                dest=destpaths+"/"+filename
                os.rename(src,dest)
                
            else:
                destpaths= "/Users/pratiksannakki/Desktop/lazy/jj/hello/unknown"
                src=filepaths+"/"+filename
                dest=destpaths+"/"+filename
                os.rename(src,dest)

eventhandler= MyHandler()
Observer=Observer()
Observer.schedule(eventhandler,filepaths,recursive=True)
Observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    Observer.stop()
Observer.join()
