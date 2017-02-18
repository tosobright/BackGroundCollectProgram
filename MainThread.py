__author__ = 'Toso'
import threading
import TcpListen
import MySQL
import misc

exitFlag = 0

def SaveDataToSQL():
    data=''
    while exitFlag == 0:
        if not TcpListen.TcpQueue.empty():
            data=TcpListen.TcpQueue.get()
            MySQL.MySQLData(data)
            misc.print_time('------SaveDataToSQL_'+data+'------',1)
        else:
            misc.print_time('SQL_Thread',1)

def Thread2():
    while exitFlag == 0:
        misc.print_time('Thread2',1)

thread1 = threading.Thread(target=SaveDataToSQL,args=())
thread2 = threading.Thread(target=Thread2,args=())

thread1.start()
thread2.start()
TcpListen.tcplisten()

print "Exiting Main Thread"