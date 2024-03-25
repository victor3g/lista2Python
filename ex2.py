import threading


variavel_global = 0


lock = threading.Lock()


def incrementar_variavel():
    global variavel_global
    for _ in range(100):
        with lock:
            variavel_global += 1


thread1 = threading.Thread(target=incrementar_variavel)
thread2 = threading.Thread(target=incrementar_variavel)


thread1.start()
thread2.start()


thread1.join()
thread2.join()


print("Valor final da variável global:", variavel_global)
