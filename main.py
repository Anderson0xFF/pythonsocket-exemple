import connection_manager
#import time;

manager = connection_manager.ConnectionManager("127.0.0.1", 7171)
manager.start()

#time.sleep(15000)
