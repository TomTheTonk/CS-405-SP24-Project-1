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


#Queue
def queue(file):
    while file != []:

        file.pop()
def saveFiles(file):
    with open('tester.txt', 'w') as f:
        for line in file:
            f.write("%s\n" % line)
    print("Saved to tester.txt")

def termRun():
    algorithim = 0
    file = None
    print("Enter Simulation Mode 0(Auto) or 1(Manual)")
    mode = int(input())
    if mode != 1 and mode != 0:
        raise Exception("Mode Must be 0 or 1")
    print("Enter simulation unit time")
    simTime = int(input())
    print("Enter Time Slice for RR")
    timeSlice = int(input())

    while(True):
        print("--------------------------------------------------")
        print("Simulation Mode is ", mode, " Simulation Unit Time is ", simTime,  " Time Slice is ", timeSlice)
        print("--------------------------------------------------")
        if file != None:
           [print(i) for i in file]
        else:
            print("No File to Run")
        print("--------------------------------------------------")
        print("Select an option")
        print("1. Input A File")
        print("2. Select Algorithim")
        print("3. Run File")
        print("4. Save Files")
        print("5. Quit")
        print("--------------------------------------------------")
        selection = int(input())
        
        match(selection):
            case 1: 
                print("Enter A Test File")
                file = input()
                file = fileOpen(file)

            case 2:
                print("Select an Algorthim")
                print("FCFS 0 (Default)")
                print("SJF 1")
                print("PS 2")
                print("RR 3")
                algorithim = int(input())
                match(algorithim):
                    case 0: 
                        print("FCFS selected")
                        
                    case 1: 
                        print("SJF selected")
                        
                    case 2: 
                        print("PS selected")
                        
                    case 3: 
                        print("RR selected")
                        
            case 3:
                queue(file)
            case 4:
                saveFiles(file)
            case 5:
                break


#File Processing
def fileOpen(fileName):
        operationList = []
        PID = 1
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
                operationDict = {"name": name, "PID": PID, "arrival":arrival, "priority": priority, "CPUBurst": CPUBurst, "IOBurst": IOBurst, "State": "New", "arrivalTime": None, "finishTime": None, "turnAround": None, "waitTime": None, "IOwaitTime": None}
                PID = PID + 1
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


