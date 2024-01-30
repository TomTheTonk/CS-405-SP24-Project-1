import psutil

#Algorithims

#Stats
def CPUUsage():
    return psutil.getloadavg()

#Interface

#File Processing
def fileOpen(fileName):
        
        operationList = []
        file = open(fileName)
        for line in file:
            name = file.readline.split(0)
            arrival = file.readline.split(0)
            priority = file.readline.split(0)
            CPUBurst = file.readline.split(0)
            IOBurst = file.readline.split(0)
            operationList.append[[name, arrival, priority, CPUBurst, IOBurst]]
        return file



