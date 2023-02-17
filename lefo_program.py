import queue

# Create a new LIFO queue
my_queue = queue.LifoQueue()

# Add items to the queue
my_queue.put(10)
my_queue.put(20)
my_queue.put(30)
my_queue.put(40)

# Print the contents of the queue
print("Items in the LIFO queue:")
while not my_queue.empty():
    print(my_queue.get())
