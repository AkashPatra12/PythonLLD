import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls, *args, **kwargs)
                print("new instance")
            else:
                print("Existing already")
        return cls._instance

obj1 = Singleton()
obj2 = Singleton()

obj3 = Singleton()

threads = [threading.Thread(target=Singleton) for _ in range(10)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
