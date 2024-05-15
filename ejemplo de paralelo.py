#GALLEGOS LIZARRAGA RUDY ALEX

#THREADING PARA HILOS
#MUTIPROCESSING PARA PARALLEO

import threading
import multiprocessing
import time

# AQUI CONCURRENTE Y APEND JALA AL RPTA
def sumar_numeros_concurrente(num1, num2, rpta):
    rpta.append(num1 + num2)

# AQUI PARALELO Y PUT JALA AL RPTA
def sumar_numeros_paralelo(num1, num2, rpta):
    rpta.put(num1 + num2)

def main_concurrente():
    # Declara para concu
    rpta = []

    # pide n1 y n2 para concu
    numero1 = int(input("Holi , este es concurrente , ingresa n1: "))
    numero2 = int(input("Ingresa n2: "))

    # Declarar un hilo para sumar los números
    t = threading.Thread(target=sumar_numeros_concurrente, args=(numero1, numero2, rpta))

    # enciende el concu
    t.start()

    # para que cargue
    t.join()

    # print de rpta
    print("La suma de", numero1, "y", numero2, "es:", rpta[0])

def main_paralelo():
    # Declaración paralelo con queque
    rpta = multiprocessing.Queue()

    # pide para paraleo
    numero1 = int(input("Holi, este es paralelo, ingresa n1: "))
    numero2 = int(input("Ingresa n2: "))

    # Declara paralelo
    p = multiprocessing.Process(target=sumar_numeros_paralelo, args=(numero1, numero2, rpta))

    
    p.start()

    
    p.join()

    # aqui debe tener resultado
    suma = rpta.get()

    # print de paralelo
    print("La suma de", numero1, "y", numero2, "es:", suma)

if __name__ == "__main__":
    # con esto se mid el tiempo de ejecución para la tarea concurrent
    start_time_concurrente = time.time()
    main_concurrente()
    end_time_concurrente = time.time()
    tiempo_concurrente = end_time_concurrente - start_time_concurrente

    # este para paralela
    start_time_paralela = time.time()
    main_paralelo()
    end_time_paralela = time.time()
    tiempo_paralela = end_time_paralela - start_time_paralela

    # print de cada uno
    print("Tiempo de ejecución (concurrente):", tiempo_concurrente, "segundos")
    print("Tiempo de ejecución (paralelo):", tiempo_paralela, "segundos")

    # compara con if y elsee
    if tiempo_concurrente < tiempo_paralela:
        print("La tarea concurrente demoró menos tiempo en ejecutarse")
    elif tiempo_concurrente > tiempo_paralela:
        print("La tarea paralela demoró menos tiempo en ejecutarse")
    else:
        print("Ambas tareas tomaron el mismo tiempo en ejecutarse")
