from store import ConcurrentKVStore
import threading

kv_store = ConcurrentKVStore()

def write():
    for i in range(5):
        kv_store.put("key", i)

def read():
    for i in range(3):
        print(kv_store.get("key"))
    
    print(kv_store.get("another_key"))

if __name__ == "__main__":
    t1 = threading.Thread(target=write)
    t2 = threading.Thread(target=read)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
