import threading
import time
import random

orders_file = "orders_wo_mutex.txt"

def read_orders():
  with open(orders_file, "r") as file:
    orders = file.readlines()
  return orders

def write_orders(orders):
  with open(orders_file, "w") as file:
    file.writelines(orders)

def process_order(chef_id):
  orders = read_orders()
  print(f"Chef {chef_id} read orders: {orders}")

  time.sleep(random.uniform(0.1, 0.5))

  new_order = f"Order from Chef {chef_id}\n"
  orders.append(new_order)
  print(f"Chef {chef_id} adding new order: {new_order}")

  write_orders(orders)
  print(f"Chef {chef_id} wrote orders: {orders}")

if __name__ == "__main__":
  with open(orders_file, "w") as file:
    file.write("Initial Order\n")

  threads = []
  for i in range(10):
    t = threading.Thread(target=process_order, args=(i,))
    threads.append(t)
    t.start()

  for t in threads:
    t.join()