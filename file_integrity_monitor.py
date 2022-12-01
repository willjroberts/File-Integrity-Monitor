from sys import argv
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

#Initialize
event_handler = LoggingEventHandler()
observer = Observer()

def file_monitor(args):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        handlers = [logging.FileHandler({args[2]}, 'a')]   
                        )
    
    with open(args[1]) as f:
        paths = f.readlines()

    watching = []
    for i in paths:
        path = i.rstrip()
        observer.schedule(event_handler, path, recursive=True)
        watching.append(observer)

    observer.start()
    print('Monitoring started...')

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print('Monitoring stopped')
    observer.join()

file_monitor(argv)



