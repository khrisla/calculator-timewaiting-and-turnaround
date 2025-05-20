from algorithm import Algorithm 

class Scheduler:

    def __init__(self):
        self.original_processes = []

    def receiveProcesses(self):
        print(f"{'-'*67}\n🔷 Bem-vindo ao calculador de tempo de espera e turnaround. 🔷\n{'-'*67}")

        while True:
            try:
                quantity = int(input("💠 Quantos processos deseja inserir? \n➡ "))
                if quantity > 0:
                    break
                else:
                    print(f"⚠️  Digite um número maior que 0 ⚠️\n{'-'*67}")
            except ValueError:
                print(f"⚠️  Digite apenas números inteiros. ⚠️\n{'-'*67}")

        self.original_processes = []
        
        for i in range(quantity):
            while True:
                name = input(f"🔹 Digite o >nome< do {i+1}º processo: \n➡ ").strip()
                if name:
                    break
                else:
                    print(f"⚠️  O nome não pode estar vazio ⚠️")

            while True:
                try:
                    order = int(input(f"🔹 Digite a >ordem< de execução do processo '{name}': \n➡ "))
                    break
                except ValueError:
                    print(f"⚠️  Digite um número inteiro. ⚠️")

            while True:
                try:
                    size = int(input(f"🔹 Digite o >tamanho< do processo '{name}': \n➡ "))
                    if size > 0:
                        self.original_processes.append([order, size, name])
                        break
                    else:
                        print(f"⚠️  Digite um número maior que 0 ⚠️")
                except ValueError:
                    print(f"⚠️  Digite um número inteiro. ⚠️")

    def chooseAlgorithm(self):
        while True:
            processes = [p[:] for p in self.original_processes]
            while True:
                try:
                    self.choose_algorithm = int(input(f"{'-'*67}\n🔷 Escolha o algoritmo de escalonamento: 🔷 \n\n1️⃣  - FIFO (First In First Out) \n2️⃣  - SJF (Shortest Job First) \n3️⃣  - Ambos \n{'-'*67}\n➡ "))
                    if self.choose_algorithm in [1, 2, 3]:
                        break
                    else:
                        print(f"⚠️  Digite apenas 1, 2 ou 3 ⚠️\n{'-'*67}")
                except ValueError:
                    print(f"⚠️  Digite 1, 2 ou 3 ⚠️\n{'-'*67}")

            if self.choose_algorithm == 1:
                self.run_algorithm("FIFO", processes)
            elif self.choose_algorithm == 2:
                self.run_algorithm("SJF", processes)
            elif self.choose_algorithm == 3:
                self.run_algorithm("FIFO", [p[:] for p in processes])
                self.run_algorithm("SJF", [p[:] for p in processes])

            while True:
                again = input("🔂 Deseja executar outro algoritmo? (s/n): ").strip().lower()
                if again in ["s", "n"]:
                    break
                else:
                    print("⚠️  Por favor, digite apenas 's' para sim ou 'n' para não.")

            if again == "n":
                break


    def run_algorithm(self, algorithm_name, processes):
        algorithm = Algorithm(processes)
        if algorithm_name == "FIFO":
            result = algorithm.FIFO()
        else:
            result = algorithm.SFJ()
        self.showWTTA(result, algorithm_name)

    def showWTTA(self, results, algorithm_name):
        total_waiting = 0
        total_turnaround = 0

        print(f"\n*️⃣  Resultados - Algoritmo: {algorithm_name}")
        print(f"{'-'*90}")
        print(f"{'Nome':^15} | {'Ordem de Chegada':^18} | {'T. Execução':^12} | {'T. Espera':^10} | {'Turnaround':^13}")
        print(f"{'-'*90}")

        for process in results:
            order = process[0]
            size = process[1]
            name = process[2]
            wait = process[3]
            turnaround = process[4]

            total_waiting += wait
            total_turnaround += turnaround

            print(f"{name:^15} | {order:^18} | {size:^12} | {wait:^10} | {turnaround:^13}")

        avg_waiting = total_waiting / len(results)
        avg_turnaround = total_turnaround / len(results)

        print(f"{'-'*90}")
        print(f"{'MÉDIA':^15} | {'-':^18} | {'-':^12} | {avg_waiting:^10.2f} | {avg_turnaround:^13.2f}")
        print(f"{'-'*90}")

