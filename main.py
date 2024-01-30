import psutil

#Algorithims
def FCFS(file):
     #No Need to do anything list comes in order recieved 
     return file
def SJF(file):
    
    return file
def PS(file):

    return file
#Stats
def CPUUsage():
    return psutil.getloadavg()

#Interface

#File Processing
def fileOpen(fileName):
        operationList = [[]]
        if fileName.endswith('.txt'):
            file = open(fileName)
            for line in file:
                name = file.readline.split(0)
                arrival = file.readline.split(1)
                priority = file.readline.split(2)
                CPUBurst = file.readline.split(3)
                IOBurst = file.readline.split(4)
                operationList.append[{"name": name, "arrival":arrival, "priority": priority, "CPUBurst": CPUBurst, "IOBurst": IOBurst}]
            return file
        else:
             return None


 

