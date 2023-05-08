import pandas as pd


def first_fit(mb, p):
    allocated_memory = [-1] * len(p)
    for i in range(len(p)):
        for j in range(len(mb)):
            if mb[j]["size"] >= p[i]["process_size"]:
                allocated_memory[i] = mb[j]["id"]
                mb[j]["size"] -= p[i]["process_size"]
                break
    for i in range(len(p)):
        if allocated_memory[i] != -1:
            print("El proceso {0} se aloja en el bloque de memoria {1}".format(p[i]["process"],allocated_memory[i]))
        else:
            print("El proceso {0} no se aloja en ningun bloque de memoria".format(p[i]["process"]))


def best_fit(mb, p):
    allocated_memory = [-1] * len(p)
    for i in range(len(p)):
        best_block_index = -1
        for j in range(len(mb)):
            if mb[j]["size"] >= p[i]["process_size"]:
                if best_block_index == -1 or mb[j]["size"] < mb[best_block_index]["size"]:
                    best_block_index = j
        if best_block_index != -1:
            allocated_memory[i] = mb[best_block_index]["id"]
            mb[best_block_index]["size"] -= p[i]["process_size"]
    for i in range(len(p)):
        if allocated_memory[i] != -1:
            print("El proceso {0} se aloja en el bloque de memoria {1}".format(p[i]["process"],allocated_memory[i]))
        else:
            print("El proceso {0} no se aloja en ningun bloque de memoria".format(p[i]["process"]))



def worst_fit(memory_blocks, processes):
    memory_blocks = sorted(memory_blocks, key=lambda x: x['size'], reverse=True)
    allocated_blocks = []
    for process in processes:
        worst_block = None
        for block in memory_blocks:
            if block['size'] >= process['process_size'] and (worst_block is None or block['size'] > worst_block['size']):
                worst_block = block
        if worst_block is not None:
            worst_block['size'] -= process['process_size']
            allocated_block = {'name': worst_block['id'], 'allocated': process['process']}
            allocated_blocks.append(allocated_block)
    return allocated_blocks


def next_fit(memory_blocks, processes):
    allocated_blocks = []
    current_block_index = 0
    for process in processes:
        allocated = False
        for i in range(len(memory_blocks)):
            block_index = (current_block_index + i) % len(memory_blocks)
            block = memory_blocks[block_index]
            if block['size'] >= process['process_size']:
                block['size'] -= process['process_size']
                allocated_block = {'name': block['id'], 'allocated': process['process']}
                allocated_blocks.append(allocated_block)
                allocated = True
                current_block_index = block_index
                break
        if not allocated:
            print("No se puede alojar {0} con el tamaño {1}".format(process['process'], process['process_size']))
    return allocated_blocks


def main():
    col_names = ["process", "process_size"]
    processes = pd.read_csv("archivos.txt", names=col_names).to_dict('records')
    for process in processes:
        process['process_size'] = int(process['process_size'][:-2])
    memory_blocks = [{'id': 0, 'size': 1000},
                     {'id': 1, 'size': 400},
                     {'id': 2, 'size': 1800},
                     {'id': 3, 'size': 700},
                     {'id': 4, 'size': 900},
                     {'id': 5, 'size': 1200},
                     {'id': 6, 'size': 1500}]
    print("Lista de procesos")
    print(pd.DataFrame(processes))
    print("="*50)
    print("Memoria")
    print(pd.DataFrame(memory_blocks))
    print("="*50)

    while True:
        print("Selecciona un algoritmo:")
        print("1. Primer ajuste")
        print("2. Mejor ajuste")
        print("3. Peor ajuste")
        print("4. Siguiente ajuste")
        print("5. Salir")
        algo = input("Ingresa tu opcion: ")
        if algo == '1':
            first_fit(memory_blocks, processes)

        elif algo == '2':
            best_fit(memory_blocks, processes)

        elif algo == '3':
            allocated_memory = []
            allocated_memory = worst_fit(memory_blocks, processes)
            for block in allocated_memory:
                print("Bloque de memoria {0} alojado por el proceso {1}".format(block['name'],block['allocated']))

        elif algo == '4':
            am = []
            am = next_fit(memory_blocks, processes)
            for block in am:
                print("Bloque de memoria {0} alojado por el proceso {1}".format(block['name'],block['allocated']))

        elif algo == '5':
            print("Sale!")
            return False
        else:
            print("Seleccion invalida. Por favor escoja entre las opciones 1, 2, 3, 4 or 5.")

if __name__ == '__main__':
    main()