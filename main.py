#Algorithims
import queue
from operator import itemgetter
#Quantum should be 0 by default 
Quantum = 1


def FCFS(file): 
    #Sorts the the list by arrival
    file = sorted(file, key=lambda x: x['arrival'])
    return file
  
def SJF(file):
    file = sorted(file, reverse=False, key=lambda x: x['arrival'])

#time instance - 

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
        

#Round Robing stuff
def RR(queue):
    readyQueue = queue.Queue()
   
    file = sorted(file, key=lambda x: x['CPUBurst'])
   
    for x in fileOpen.operationList:

        if file.operationList.CPUBurst[x] > Quantum:
            #push the operation to the ready state queue?
            file.operationList.CPUBurst[x].push(readyQueue)

        elif file.operationList.CPUBurst[x] < Quantum:
            continue
   
  
    
 #For the round robin, if the CPU Burst at [x] is greater than the quantum, do we push it to the stack
    return readyQueue
#print((fileOpen("TestFiles/test1.txt")))
#print((PS(fileOpen("TestFiles/test1.txt"))))
#print(FCFS(PS(fileOpen("TestFiles/test1.txt"))))
print(RR(fileOpen("TestFiles/test1.txt")))


