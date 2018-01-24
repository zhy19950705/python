from multiprocessing import Pool
import os,time,random
def run_task(name):
    print 'task %s (pid=%s) is running...' % (name,os.getpid())
    time.sleep(random.random()*3)
    print 'task %s end' % name
if __name__=='__main__':
    print 'current process %s.' % os.getpid()
    p=Pool(processes= 3)
    for i in range(5):
        p.apply_async(run_task,args=(i,))
    print 'waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'all subprocesses done'