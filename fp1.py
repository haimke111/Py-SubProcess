import os
import random
import sys
import multiprocessing
import time
import psutil


def sub(t):
    time.sleep(t)
#    print ("sub pid=" + str(os
    print ("timestamp=" + str(time.time()))
    print ("random time=" + str(t))
    return


def running():

    for q in psutil.process_iter():
        if q.name() == 'python':
            print (q.cmdline())
            if len(q.cmdline())>1 and 'fp1.py' in q.cmdline()[1]:
                return True

    return False

if __name__ == '__main__':
    if running():
        print ("process already running, terminating")
        sys.exit()

    child_processes = []
    count = 5
    x = 0
    y = 0
    print ("arg=" + sys.argv[1])
    print("mypid=" + str(os.getpid()))

    for i in range(int(sys.argv[1])):
        p = multiprocessing.Process(target=sub(random.randint(1, 20)))
        child_processes.append(p)
        p.start()
        print ("sub pid=" + str(p.pid))

    for child in child_processes:
        child.join()


    for child in child_processes:
        if child.exitcode == 0:
            x = x + 1
        else:
            y = y + 1

    print(str(x) + " processes completed successfully")
    print(str(y) + " processes failed to complete")

