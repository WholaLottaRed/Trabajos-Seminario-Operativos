from collections import deque
import pandas as pd


def round_robin(processes, quantum):
    queue = deque(processes)
    time = 0
    while queue:
        process = queue.popleft()
        if process["burst_time"] > quantum:
            time += quantum
            process["burst_time"] -= quantum
            queue.append(process)
        else:
            time += process["burst_time"]
            process["completion_time"] = time
    return processes


def sjf(processes):
    processes = sorted(processes, key=lambda process: process["burst_time"])

    execution_order = []
    current_time = 0
    while len(processes) > 0:
        next_process = processes.pop(0)
        execution_order.append(next_process["process"])
        current_time += next_process["burst_time"]
        for process in processes:
            process["waiting_time"] = max(0, current_time - process["arrival_time"])

    return execution_order

def fifo(processes):
    processes = sorted(processes, key=lambda process: process["arrival_time"])
    execution_order = []
    for process in processes:
        execution_order.append(process["process"])

    return execution_order


#ordernar por burst time
#asignar un numero aleatorio a los procesos denominado como prioridad
#usar fifo en caso de empate


# def priority(processes):
#     processes = sorted(processes, key = lambda process: process["burst_time"])
#     execution_order = []
#     while len(processes) > 0:
#         next_process = processes.pop(0)
#         execution_order.append(next_process["process"])
#         for process in processes:
#             random_priority = rnd.randint(1, 10)
#             processes["priority"] = random_priority

# TODO 
# def priority_based_scheduling(processes):
#     processes['priority'] = np.random.randint(1, 10, processes.shape[0])
#     # Create a priority queue based on the priority values in the processes
#     # priority_queue = [(process['priority'], process) for process in processes]
#     # return heapq.heapify(priority_queue)
#     return processes


def main():
    col_names = ["process", "burst_time", "arrival_time", "priority", "position"]
    processes = pd.read_csv("procesos.txt", names=col_names).to_dict('records')
    while True:
        print("Selecciona una opcion:")
        print("1. Agregar un nuevo proceso")
        print("2. Correr el algoritmo")
        print("3. Salir")
        choice = input("Ingresa tu opcion: ")
        
        if choice == '1':
            name = input("Ingresa el nombre del proceso: ")
            burst_time = int(input("Ingresa tiempo de duracion: "))
            priority = int(input("Ingresa la prioridad: "))
            position = int(input("Ingresa la posicion (0 = final/ 1 = principio): "))
            arrival = int(input("Ingresa el tiempo de llegada:"))
            process_new = {"process": name, "burst_time": burst_time,"arrival_time":arrival, "priority": priority, "position": position}
            if process_new["position"] == 0:
                processes.append(process_new)
                print(pd.DataFrame(processes))
            elif process_new["position"] == 1:
                processes.insert(0, process_new)
                print(pd.DataFrame(processes))
            else:
                break
        elif choice == '2':
            while True:
                print("Selecciona uno de estos algoritmos:")
                print("1. Round Robin")
                print("2. SJF")
                print("3. FIFO")
                print("4. PBS")
                algo = input("Enter your choice: ")
                if algo == '1':
                    round_robin_arrange = round_robin(processes, 3)
                    print(pd.DataFrame(round_robin_arrange))
                    break
                elif algo == '2':
                    sjf_arrange = sjf(processes)
                    print(', '.join(map(str, sjf_arrange))) 
                    break
                elif algo == '3':
                    fifo_arrange = fifo(processes)
                    print(', '.join(map(str, fifo_arrange)))
                    break
                #elif algo == '4':
                    #pass
                else:
                    print("Opcion invalida. Ingresa alguna de estas opciones: 1, 2, 3 o 4.")
        elif choice == '3':
            print("Sale!")
            break
        else:
            print("Opcion invalida. Ingresa alguna de estas opciones: 1, 2 o 3.")


if __name__ == '__main__':
    main()