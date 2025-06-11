import threading
import time
import random

data = None
condition = threading.Condition()

def producer():
  global data
  while True:
    with condition:
      # generate random data
      data = random.randint(1, 100)
      print(f"Generated data: {data}")
      condition.notify()
    
    time.sleep(random.uniform(0.5, 2))

def consumer():
  global data
  while True:
    with condition:
      condition.wait()
      print(f"Consumed data: {data}")
      data = None
    
    time.sleep(random.uniform(0.5, 1))

if __name__ == "__main__":
  producer_thread = threading.Thread(target=producer)
  consumer_thread = threading.Thread(target=consumer)

  consumer_thread.start()
  producer_thread.start()

  consumer_thread.join()
  producer_thread.join()