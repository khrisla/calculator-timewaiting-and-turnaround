class Algorithm:
    
    def __init__(self, processes):
        self.processes = processes

    def FIFO(self):
        processes = sorted(self.processes, key=lambda x: x[0])
        time = 0

        for i in range(len(processes)):
            processes[i].append(time)
            time += processes[i][1]
            processes[i].append(time)

        return processes

    def SFJ(self):
        processes = sorted(self.processes, key=lambda x: x[1])
        time = 0

        for i in range(len(processes)):
            processes[i].append(time)
            time += processes[i][1]
            processes[i].append(time)

        return processes
