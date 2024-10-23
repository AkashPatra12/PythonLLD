import threading

lock = threading.Lock()
counter = 0

def increment():
    global counter
    with lock:
        for i in range(10):
            print(counter)
            counter += 1


threads = [threading.Thread(target=increment) for _ in range(10)]

# start the threads
for thread in threads:
    thread.start()

# wait for all the threads to complete
for thread in threads:
    thread.join()

print("end")