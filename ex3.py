import threading
import random
import queue
import time

fila = queue.Queue()

def gerar_numeros():
    for _ in range(10):
        numero = random.randint(1, 100)
        fila.put(numero)
        print(f"Thread geradora: número {numero} colocado na fila")
        time.sleep(1)


def imprimir_numeros():
    while True:
        if not fila.empty():
            numero = fila.get()
            print(f"Thread consumidora: número {numero} retirado da fila")
        else:
            break


thread_geradora = threading.Thread(target=gerar_numeros)
thread_consumidora = threading.Thread(target=imprimir_numeros)

thread_geradora.start()
thread_consumidora.start()


thread_geradora.join()
thread_consumidora.join()

print("Programa principal encerrado.")
