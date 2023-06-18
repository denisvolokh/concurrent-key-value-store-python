import threading

class ConcurrentKVStore():
    def __init__(self):
        self.store = dict() # key-value store
        self.locks = dict() # storage of locks for each key
    
    def put(self, key, value):
        # get the lock for the key or create one if it doesn't exist
        lock = self.locks.setdefault(key, threading.Lock())

        with lock:
            self.store[key] = value
        
    def get(self, key):
        # get the lock for the key or create one if it doesn't exist
        lock = self.locks.setdefault(key, threading.Lock())

        with lock:
            return self.store.get(key)