import math
import threading
import os
import time

def cpu_task():
  start = time.time()
  result = math.factorial(150000)
  print(f"Thread ID: {threading.get_ident()}, Process ID: {os.getpid()}, Time difference: {time.time() - start} seconds")

if __name__ == "__main__":
  print(f"Main process ID: {os.getpid()}")

  print("== Starting single threaded ==")
  start_time = time.time()
  for _ in range(10):
    cpu_task()
  
  print(f"Single-threaded total execution time: {time.time() - start_time} seconds")

  print("==============================")

  print("== Starting multi threaded==")
  start_time = time.time()
  threads = []
  for _ in range(10):
    thread = threading.Thread(target=cpu_task)
    threads.append(thread)
    thread.start()
  
  for thread in threads:
    thread.join()

  print(f"Multi-threaded total execution time: {time.time() - start_time} seconds")
