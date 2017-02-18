__author__ = 'Toso'
import time

def print_time(threadname,delay):
    time.sleep(delay)
    print '%s:%s'%(threadname,time.ctime(time.time()))