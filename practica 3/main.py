from collections import deque
import pandas as pd
# import random as rnd
# import heapq
# import numpy as np

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


    

def main():
    
    col_names = ["process", "burst_time", "arrival_time"]
    processes = pd.read_csv("practica 3/procesos.txt", names=col_names).to_dict('records')
    print("Procesos desorganizados")
    print(pd.DataFrame(processes))
    print("*"*90)
    
    round_robin_arrange = round_robin(processes, 3)
    sjf_arrange = sjf(processes)
    fifo_arrange = fifo(processes)

    print("Round robin ")
    print(pd.DataFrame(round_robin_arrange)) 
    print("*"*90)
    print("Shortest Job First")
    print(', '.join(map(str, sjf_arrange))) 
    print("*"*90)
    print("First In - First Out")
    print(', '.join(map(str, fifo_arrange)))
    # print(priority_based_scheduling(processes))

if __name__ == '__main__':
    main()