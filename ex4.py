import threading
import random
import time


def thread_func(thread_num):
    tempo_espera = random.randint(1, 5)
    print(f"Thread {thread_num} iniciou. Esperando {tempo_espera} segundos.")
    time.sleep(tempo_espera)
    print(f"Thread {thread_num} terminou.")


threads = []


for i in range(5):
    thread = threading.Thread(target=thread_func, args=(i+1,))
    thread.start()
    threads.append(thread)
    
    time.sleep(random.uniform(0.1, 0.5))


for thread in threads:
    thread.join()

print("Todas as threads terminaram. Programa principal encerrado.")