import threading
import time


def get_request():
    print("Get request...")
    time.sleep(3)
    print("Done")


if __name__ == "__main__":
    thread_1 = threading.Thread(target=get_request)
    thread_2 = threading.Thread(target=get_request)
    thread_3 = threading.Thread(target=get_request)
    thread_1.start()
    thread_2.start()
    thread_3.start()