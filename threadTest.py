'''
import _thread
import time

def print_time(name, delay):
    count = 0
    while count < 5:
        print("%s:%s:%s"%(name, time.ctime(time.time()),time.localtime()))
        time.sleep(delay)
        count += 1

try:
    _thread.start_new_thread(print_time,("thread-1",2))
    _thread.start_new_thread(print_time,("thread-2",3))
except:
    print("Error!")

while 1:  #没有这个,主进程退出之后线程就不执行了
    pass
'''

import threading
import time


class myThread(threading.Thread):

    def __init__(self, name, delay, threadsLock):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
        self.threadsLock = threadsLock

    def run(self):
        super().run()
        self.threadsLock.acquire()
        print("开始线程%s" % self.name)
        count = 0
        while count < 5:
            print("%s:%s" % (self.name, time.ctime(time.time())))
            time.sleep(self.delay)
            count += 1
        print("退出%s" % self.name)
        self.threadsLock.release()


class listPlusThread(threading.Thread):
    def __init__(self, name, list, delay, threadsLock):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
        self.threadsLock = threadsLock
        self.list = list

    def run(self):
        super().run()
        #self.threadsLock.acquire()
        print("开始线程%s" % self.name)
        i = 0
        while i < len(self.list):
            self.list[i] += 1
            #time.sleep(self.delay)
            i += 1
        print("退出%s" % self.name)
        #self.threadsLock.release()


class printListThread(threading.Thread):
    def __init__(self, name, list, threadsLock):
        threading.Thread.__init__(self)
        self.name = name
        self.list = list
        self.threadsLock = threadsLock

    def run(self):
        #self.threadsLock.acquire()
        print("开始%s" % self.name)
        i = 0
        while i < len(self.list):
            print(self.list[i], end=' , ')
            i += 1
        print("\n结束%s" % self.name)
        #self.threadsLock.release()


threadLock = threading.Lock()
# thread1 = myThread('thread-1', 2, threadLock)
# thread2 = myThread('thread-2', 3, threadLock)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
mylist = [1, 2, 3, 4, 5]
thread1 = listPlusThread("thread-1", mylist, 0.001, threadLock)
thread2 = printListThread("thread-2", mylist, threadLock)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程")
