class Algorithm:
    
    def __init__(self, processes):
        self.processes = processes

    def FIFO(self):
        processes = sorted(self.processes)
        values = 0
        
        for i in range(len(self.processes)):
            processes[i].append(values)
            values += processes[i][1]
            processes[i].append(values)
            
        return processes
    
    def SFJ(self):
        processes = sorted(self.processes, key=lambda x: x[1])
        values = 0
        
        for i in range(len(self.processes)):
            processes[i].append(values)
            values += processes[i][1]
            processes[i].append(values)
            
        return processes

