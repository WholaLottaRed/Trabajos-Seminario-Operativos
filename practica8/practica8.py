import threading
import time
import random

current_num = 0
lock = threading.Lock()

def escribir(filename, frequency):
    global current_num
    while True:
        with lock:
            current_num += 1
            with open(filename, 'a') as f:
                f.write(str(current_num) + '\n')
        time.sleep(random.uniform(frequency*0.5, frequency*2.0))

def leer(filename, frequency):
    while True:
        with lock:
            with open(filename, 'r') as f:
                lines = f.readlines()
            print(''.join(lines))
        time.sleep(random.uniform(frequency*1.0, frequency*2.0))

escritor1 = threading.Thread(target=escribir, args=('threads.txt', 0.5,))
escritor2 = threading.Thread(target=escribir, args=('threads.txt', 1.0,))
escritor3 = threading.Thread(target=escribir, args=('threads.txt', 2.0,))

lector1 = threading.Thread(target=leer, args=('threads.txt', 1.0,))
lector2 = threading.Thread(target=leer, args=('threads.txt', 1.5,))
lector3 = threading.Thread(target=leer, args=('threads.txt', 2.0,))

escritor1.start()
escritor2.start()
escritor3.start()
lector1.start()
lector2.start()
lector3.start()

escritor1.join()
escritor2.join()
escritor3.join()
lector1.join()
lector2.join()
lector3.join()