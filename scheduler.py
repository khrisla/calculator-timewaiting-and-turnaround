from algorithm import Algorithm 

class Scheduler:
    
    def __init__(self):
        self.processes = []
        
    def receiveProcesses(self):
        print(f"{'-'*67}\n🔷 Olá! Bem-vindo ao calculador de tempo de espera e turnaround.🔷\n{'-'*67}")
    
        for i in range(5):
            value = i
            while True:
                try:
                    size = int(input(f"💠 Qual o tamanho do {value+1}º processo? \n➡ "))
                    if size > 0:
                        self.processes.append([value, size])
                        break
                    else:
                        print(f"⚠️  Digite um número maior que 0 ⚠️\n{'-'*67}")
                except ValueError:
                    print(f"⚠️  Entrada inválida. Digite apenas números inteiros. ⚠️\n{'-'*67}")

        while True:
            try:
                self.choose_algorithm = int(input(f"{'-'*67}\n🔷 Digite o número do algoritmo escalonador que deseja utilizar:🔷 \n\n1️  - FIFO(First In First Out) \n2️⃣  - SFJ(Shortest Job First) \n{'-'*67}\n➡ "))
                if self.choose_algorithm in [1, 2]:
                    break
                else:
                    print(f"⚠️  Digite apenas 1 ou 2 ⚠️\n{'-'*67}")
            except ValueError:
                print(f"⚠️  Entrada inválida.(Digite 1 ou 2) ⚠️\n{'-'*67}")

        return self.processes
    
    def calculateWTTA(self):

        algorithm = Algorithm(self.processes)
        
        if self.choose_algorithm == 1:
            values = algorithm.FIFO()
            return values
        elif self.choose_algorithm == 2:
            values = algorithm.SFJ()
            return values


    def showWTTA(self):
        
        waiting_time = self.calculateWTTA()
        turn_around = self.calculateWTTA()
    
        values_waitingtime = 0
        values_turnaround = 0

        print('*️⃣  Resultados:')
        print(f"{'-'*67}")
        print(f"{'Processo':^10} | {'T. Execução':^12} | {'T. Espera':^10} | {'Turnaround':^17}")
        print(f"{'-'*67}")

        for i in range(len(waiting_time)):
            process = waiting_time[i][0] + 1
            execution = waiting_time[i][1]
            wait_time = waiting_time[i][2]
            turnaround = turn_around[i][3]

            values_waitingtime += wait_time
            values_turnaround += turnaround

            print(f"{process:^10} | {execution:^12} | {wait_time:^10} | {turnaround:^17}")

        print(f"{'-'*67}")
        avg = values_waitingtime / len(waiting_time)
        avg2 = values_turnaround / len(turn_around)
        print(f"{'MÉDIA':^10} | {'-':^12} | {avg:^10.2f} | {avg2:^17.2f}")
        print(f"{'-'*67}")


