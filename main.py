#Algorithims
import queue
from operator import itemgetter
#Quantum should be 0 by default 
Quantum = 1

def getStartTime(time):
     return time

def setTime(time, t):
     time._age = t



currentTime = property(getStartTime, setTime)




#PCB
def PCB():
        name = fileOpen(key=lambda x: x['name'])
        identity = int
        arrivalTime = fileOpen(key=lambda x: x['arrival'])
        cpuBurst = fileOpen(key=lambda x: x['CPUBurst'])
        priority = fileOpen(key=lambda x: x['priority'])

        startTime = int
        finishTime = int
        turnAroundTime = int
        waitingTime = int



        
processOne = PCB()






     

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



#File Processing, Think of this like the Driver class in Lab 4 :)
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
        


#Scheduler
def scheduler():
        name = fileOpen(key=lambda x: x['name'])  #Name of algorithm
        processes = [] #Queue of processes
        readyOrNotHereIComeQueue = [] # ready Queue
        completedProcs = [] #Queue of complete processes
        curProc = " "
        systemTime = int 

       
#While loop to state when process should be moved to readyQueue
        while not processes.empty() or not readyOrNotHereIComeQueue.empty() :
             print("System Time: " + systemTime)

             for p in processes:
                  if fileOpen(key=lambda x: x['arrival'] == systemTime):
                        readyOrNotHereIComeQueue.append(str(p))
                        #readyOrNotHereIComeQueue.append(p)


        processes.removeAll(readyOrNotHereIComeQueue)
        curProc = p
        print()

        if curProc == (fileOpen(key=lambda x: x['arrival']) < 0):
                curProc.setStartTime(systemTime)
                exec(curProc, 1)

        for p in readyOrNotHereIComeQueue:
             if p != curProc:
                  #Increase waiting time by 1
                  p += 1
        #increment systemTime by 1 unit          
        systemTime += 1

        #if the current processe's CPU burst is equal to 0
        # set the curProc's finishTime to the systemTime
        # remove the curProc from the readyQueue
        # and add the curProc to the finishedProcs 
       
        curProc == readyOrNotHereIComeQueue.__getitem__(0) 
       







#Round Robing stuff
def RR(queue):
    readyQueue = []
   
    file = sorted(file, key=lambda x: x['CPUBurst'])
   
    for x in fileOpen.operationList:

        if file.operationList.CPUBurst[x] > Quantum:
            #push the operation to the ready state queue?
            file.operationList.CPUBurst[x].append(readyQueue)

        elif file.operationList.CPUBurst[x] < Quantum:
            continue
   
  
    
 #For the round robin, if the CPU Burst at [x] is greater than the quantum, do we push it to the stack
    return readyQueue
#print((fileOpen("TestFiles/test1.txt")))
#print((PS(fileOpen("TestFiles/test1.txt"))))
print(FCFS(PS(fileOpen("TestFiles/test1.txt"))))
#print(RR(fileOpen("TestFiles/test1.txt")))

print(scheduler)
