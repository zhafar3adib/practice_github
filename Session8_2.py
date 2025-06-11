from multiprocessing import Process
import os 
import time

def task():
    time.sleep(1)
    timestamp = time.time()

    print(f'Worker Process ID: {os.getpid()}, cureent timestamp {timestamp}')

if __name__ == '__main__':
    print('== Running using loop')
    for _ in range(5):
        task()

    print('== Running using multiprocessing')
    processes = []
    for _ in range(5):
        p = Process(target=task)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()