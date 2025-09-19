import threading
import time


def task(name):
    print(f"Thread {name}: starting...")
    time.sleep(2)
    print(f"Thread {name}: finishing.")


def print_numbers():
    for i in range(1, 6):
        print(i)


def main():
    t1 = threading.Thread(target=task, args=("A",))
    t1.start()
    print("Main thread: doing other work.")
    t1.join()
    print("All done")

    counting = threading.Thread(target=print_numbers)
    counting.start()
    counting.join()


main()
