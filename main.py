#Algorithims
from operator import itemgetter


def FCFS(file): 
    #Sorts the the list by arrival
    file = sorted(file, key=lambda x: x['arrival'])
    return file
def SJF(file):
    
    return file
def PS(file):
    #sorts the list by its priority
    file = sorted(file, key=lambda x: x['priority'])
    return file
#Stats
def CPUUsage(file, index):
    return list(map(itemgetter('CPUBurst'), file))[index]

def IOBurst(file, index):
    return list(map(itemgetter('IOBurst'), file))[index]
#Interface

#File Processing
def fileOpen(fileName):
        operationList = []
        if fileName.endswith('.txt'):
            file = open(fileName)
            while True:
                CPUBurst = []
                IOBurst = []
                operationDict = {}
                unkeyedList = file.readline().split()
                index = 3
                if unkeyedList != []:
                    name = unkeyedList[0]
                    arrival = int(unkeyedList[1])
                    priority = int(unkeyedList[2])
                    while index <= len(unkeyedList):
                        CPUBurst.append(int(unkeyedList[index]))
                        if index + 1 < len(unkeyedList):
                            IOBurst.append(int(unkeyedList[index + 1]))
                        index = index + 2
                else:
                    break
                operationDict = {"name": name, "arrival":arrival, "priority": priority, "CPUBurst": CPUBurst, "IOBurst": IOBurst}
                operationList.append(operationDict)
            return operationList
        else:
             return None
print((fileOpen("TestFiles/test1.txt")))
print((PS(fileOpen("TestFiles/test1.txt"))))
print(FCFS(PS(fileOpen("TestFiles/test1.txt"))))

 

