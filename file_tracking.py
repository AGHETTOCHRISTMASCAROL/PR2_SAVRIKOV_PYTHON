import time
import os
from watchdog.observers import Observer
from file_tracking_class import FileTracking

path :str = os.getcwd() #путь к папке со криптом
event_handler = FileTracking() #обработчик
observer = Observer()
observer.schedule(event_handler, path, recursive=True) #следит за папкой со скриптами
observer.start()

try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()