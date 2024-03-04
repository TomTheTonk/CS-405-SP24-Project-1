
import os
import time


def FCFS(file): 
    #Sorts the the list by arrival
    file = sorted(file, key=lambda x: x['arrival'])
    return file
  
def SJF(file):
    file = sorted(file, reverse=False, key=lambda x: (x['State'] != "Terminated", x['CPUBurst'][0], x['arrival']))

    return file

def PS(file):
    #sorts the list by its priority
    file = sorted(file, key=lambda x: x['priority'])
    return file
  
#Stats

def saveFiles(file, log):
    print("Enter a name for the file to save the results to")
    output = input()
    output= output + ".txt"
    with open(output, 'w') as f:
        for line in file:
            f.write("%s\n" % line)
        for line in log:
            f.write("%s\n" % line)
    print("Saved to", output)

def termRun():
    algorithim = 0
    file = None
    log = []
    print("Enter Simulation Mode as integer: Auto(0) or Manual(1)")
    mode = int(input())
    if mode != 1 and mode != 0:
        raise Exception("Mode Must be 0 or 1")
    
    print("Enter simulation unit time: Frames-per-second(0) or Frames-per-ms(1)")
    simTime = int(input())
    if simTime != 1 and simTime != 0:
        raise Exception("Must be 0 or 1")
    
    print("Enter Time Slice for RR:")
    timeSlice = int(input())

    while(True):
        os.system('clear')
        print("--------------------------------------------------")
        print("Simulation Mode is:", mode, "(Auto(0) Manual(1)) Simulation Unit Time is:", simTime,  "Time Slice is:", timeSlice)
        match(algorithim):
                    case 0: 
                        print("FCFS selected")
                        
                    case 1: 
                        print("SJF selected")
                        
                    case 2: 
                        print("PS selected")
                        
                    #case 3: 
                    #    print("RR selected")
        print("--------------------------------------------------")
        if file != None:
           [print(i) for i in file]
        else:
            print("No processes to run")
        print("--------------------------------------------------")
        print("Select an option")
        print("1. Input a File")
        print("2. Select Algorithim(FCFS Default)")
        print("3. Run Processes")
        print("4. Save Output")
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
                print("FCFS: 0 (Default)")
                print("SJF: 1")
                print("PS: 2")
                print("RR: 3")
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
                log, file = scheduler(file, log, mode, simTime)
            case 4:
                saveFiles(file, log)
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



#Scheduler
def scheduler(file, algorithim, sim, simTime):
    log = []
    systemTime = 0
    saved = [] 
    for t in range(len(file)):
        saved.append({"ID": file[t].get("PID"), "CPUTimes": sum(file[t].get("CPUBurst"))})

    totalBurst = 0
    match(algorithim):
        case 0: 
            file = FCFS(file)
                        
        case 1: 
            file = SJF(file)
                        
        case 2: 
            file = PS(file)

    schedulerPrint(file, [], [], "")                    

    for p in range(len(file)):
        if file[p].get("State") == "New":
            file[p].update({'State': "Ready"})
            log.append(file[p].get("name") + " was added to ready queue")
        
    if algorithim != 1:
        totalRun = 0
        for p in range(len(file)):
            oiTime = file[p].get("IOBurst") # list of oi times
            cpuTime = file[p].get("CPUBurst") #list of cpu times
            for i in range(len(cpuTime)):
                totalRun = cpuTime[i] + totalRun
            for i in range(len(oiTime)):
                totalRun = oiTime[i] + totalRun
            if cpuTime != []:
                currCPU = cpuTime[0]
            if oiTime != []:
                currIO = oiTime[0]
            try:
                for i in range(totalRun):
                    
                    if (file[p].get("State") == "Ready" and cpuTime != []) or (file[p].get("State") == "Running" and oiTime == [] and cpuTime != []):
                        if file[p].get("State") == "Ready":
                            file[p].update({'State': "Running"})
                            log.append(file[p].get("name") + " was added to the CPU")
                        #print(file[p].get("name") + " was added to the CPU")
                        if sim == 1:
                                schedulerPrint(file, cpuTime, [], (log))
                                time.sleep(1)
                                systemTime = systemTime + 1
                                currCPU = currCPU - 1
                                cpuTime[0] = cpuTime[0] - 1
                                file[p].update({'CPUBurst': cpuTime})
                                input("Enter any key to continue: ")
                                if cpuTime[0] == 0:
                                    cpuTime.pop(0)
                                
                        else:
                                schedulerPrint(file, cpuTime, [], (log))
                                time.sleep(1)
                                systemTime = systemTime + 1
                                currCPU = currCPU - 1
                                cpuTime[0] = cpuTime[0] - 1
                                file[p].update({'CPUBurst': cpuTime})
                                if cpuTime[0] == 0:
                                    cpuTime.pop(0)
                                
                    elif file[p].get("State") == "Waiting" and oiTime != []: 
                    
                        log.append(file[p].get("name") + " was added to the IO")
                        #print(file[p].get("name") + " was added to the IO")
                        file[p].update({'State': "OIRunning"})
                        if sim == 1:
                                schedulerPrint(file, [], oiTime, (log))
                                time.sleep(1)
                                systemTime = systemTime + 1
                                oiTime[0] = oiTime[0] - 1
                                currIO = currIO - 1
                                file[p].update({'OIBurst': oiTime})
                                input("Enter any key to continue: ")
                                if oiTime[0] == 0:
                                    oiTime.pop(0)
                                
                        else:
                                schedulerPrint(file, [], oiTime, (log))
                                time.sleep(1)
                                systemTime = systemTime + 1
                                oiTime[0] = oiTime[0] - 1
                                currIO = currIO - 1
                                file[p].update({'IOBurst': oiTime})
                                if oiTime[0] == 0:
                                    oiTime.pop(0)
                                

                    if oiTime != [] and file[p].get("State") == "Running":
                        file[p].update({'State': "Waiting"})
                        log.append(file[p].get("name") + " was added to the waiting queue for the IO")
                        #print(file[p].get("name") + " was added to the waiting queue for the IO")
                        schedulerPrint(file, [], [], (log))
                    elif cpuTime != [] and file[p].get("State") == "OIRunning":
                        file[p].update({'State': "Ready"})
                        log.append(file[p].get("name") + " was added to the ready queue")
                        #print(file[p].get("name") + " was added to the ready queue")
                        schedulerPrint(file, cpuTime, oiTime, (log))
                    elif oiTime == [] and cpuTime == []:
                        file[p].update({'State': "Terminated"})
                        log.append(file[p].get("name") + " was added to terminated queue")
                        #print(file[p].get("name") + " was added to terminated queue")

                        if simTime == 1:
                            file[p].update({'arrivalTime': str(file[p].get("arrival"))+"ms" })
                            file[p].update({'finishTime': str(systemTime) + "ms"})
                            file[p].update({'turnAround': str((systemTime - file[p].get("arrival")))+"ms"})
                            
                            for q in range(len(saved)):
                                if saved[q].get("ID") == file[p].get("PID"):
                                    totalBurst = saved[q].get("CPUTimes") + totalBurst
        
                            file[p].update({'waitTime': str((systemTime / totalBurst)) + "ms"})
                            file[p].update({'IOwaitTime': str(0)+"ms"})
                        elif simTime == 0:
                            file[p].update({'arrivalTime': str(file[p].get("arrival")/1000.0)+"s" })
                            file[p].update({'finishTime': str((systemTime)/1000.0) + "s"})
                            file[p].update({'turnAround': str((systemTime - file[p].get("arrival"))/1000.0)+"s"})
                            for q in range(len(saved)):
                                if saved[q].get("ID") == file[p].get("PID"):
                                    totalBurst = saved[q].get("CPUTimes") + totalBurst
                            file[p].update({'waitTime': str((systemTime - file[p].get("arrival") / totalBurst)/1000.0) + "s"})
                            file[p].update({'IOwaitTime': str(0)+ "s"})
                        #"arrivalTime": None, "finishTime": None, "turnAround": None, "waitTime": None, "IOwaitTime": None}
                        schedulerPrint(file, [], [], (log))
                        break
                        
            except:
                pause = input("Enter Stop to exit or enter any key to resume: ")
                if pause == "Stop":
                   break
                else: 
                    pass
                        
        schedulerPrint(file, [], [], (log))
        return log, file
    
    else:
        totalRun = []
        for p in range(len(file)):
            totalRun.extend(file[p].get("IOBurst")) # list of oi times
            totalRun.extend(file[p].get("CPUBurst")) #list of cpu times)
       
        for p in range(len(totalRun)):
            terminated = []
            for i in range(len(file)):
                if file[i].get("State") == "Terminated":
                    terminated.append(file[i])
            file = [i for i in file if i not in terminated]
            file = SJF(file)
            file.extend(terminated)
            oiTime = file[0].get("IOBurst") # list of oi times
            cpuTime = file[0].get("CPUBurst") #list of cpu times
            if cpuTime != []:
                currCPU = cpuTime[0]
            if oiTime != []:
                currIO = oiTime[0]
            try:
                while(currIO != 0 or currCPU != 0):
                    if (file[0].get("State") == "Ready" and cpuTime != []) or (file[0].get("State") == "Running" and oiTime == [] and cpuTime != []):
                        if file[0].get("State") == "Ready":
                            file[0].update({'State': "Running"})
                            log.append(file[0].get("name") + " was added to the CPU")
                        #print(file[p].get("name") + " was added to the CPU")
                        if sim == 1:
                                schedulerPrint(file, cpuTime, [], (log))
                                time.sleep(1)
                                systemTime = systemTime + 1
                                currCPU = currCPU - 1
                                cpuTime[0] = cpuTime[0] - 1
                                file[0].update({'CPUBurst': cpuTime})
                                input("Enter any key to continue: ")
                                if cpuTime[0] == 0:
                                    cpuTime.pop(0)

                        else:
                                schedulerPrint(file, cpuTime, [], (log))
                                time.sleep(1)
                                systemTime = systemTime + 1
                                currCPU = currCPU - 1
                                cpuTime[0] = cpuTime[0] - 1
                                file[0].update({'CPUBurst': cpuTime})
                                if cpuTime[0] == 0:
                                    cpuTime.pop(0)
                       
                    elif file[0].get("State") == "Waiting" and oiTime != []: 
                    
                        log.append(file[0].get("name") + " was added to the IO")
                        #print(file[p].get("name") + " was added to the IO")
                        file[0].update({'State': "OIRunning"})
                        schedulerPrint(file, [], oiTime, (log))
                        if sim == 1:
                                schedulerPrint(file, [], oiTime, (log))
                                time.sleep(1)
                                systemTime = systemTime + 1
                                oiTime[0] = oiTime[0] - 1
                                currIO = currIO - 1
                                file[0].update({'OIBurst': oiTime})
                                input("Enter any key to continue: ")
                                if oiTime[0] == 0:
                                    oiTime.pop(0)
                        else:
                            
                                schedulerPrint(file, [], oiTime, (log))
                                time.sleep(1)
                                systemTime = systemTime + 1
                                oiTime[0] = oiTime[0] - 1
                                currIO = currIO - 1
                                file[0].update({'IOBurst': oiTime})
                                if oiTime[0] == 0:
                                    oiTime.pop(0)

                    if oiTime != [] and file[0].get("State") == "Running":
                        file[0].update({'State': "Waiting"})
                        log.append(file[0].get("name") + " was added to the waiting queue for the IO")
                        #print(file[p].get("name") + " was added to the waiting queue for the IO")
                        schedulerPrint(file, [], [], (log))
                    elif cpuTime != [] and file[0].get("State") == "OIRunning":
                        file[0].update({'State': "Ready"})
                        log.append(file[0].get("name") + " was added to the ready queue")
                        #print(file[p].get("name") + " was added to the ready queue")
                        schedulerPrint(file, cpuTime, oiTime, (log))
                    elif oiTime == [] and cpuTime == []:
                        file[0].update({'State': "Terminated"})
                        log.append(file[0].get("name") + " was added to terminated queue")
                        #print(file[p].get("name") + " was added to terminated queue")
                        if simTime == 1:
                            file[0].update({'arrivalTime': str(file[p].get("arrival"))+"ms" })
                            file[0].update({'finishTime': str(systemTime) + "ms"})
                            file[0].update({'turnAround': str(systemTime)+"ms"})
                            for q in range(len(saved)):
                                if saved[q].get("ID") == file[0].get("PID"):
                                    totalBurst = saved[q].get("CPUTimes") + totalBurst
                            file[0].update({'waitTime': str((systemTime - file[0].get("arrival")) / totalBurst) + "ms"})
                            file[0].update({'IOwaitTime': str(systemTime)+ "ms"})
                        if simTime == 0:
                            file[p].update({'arrivalTime': str(file[0].get("arrival")/1000.0)+"s" })
                            file[0].update({'finishTime': str(systemTime/1000.0) + "s"})
                            file[0].update({'turnAround': str((systemTime - file[0].get("arrival"))/1000.0)+"s"})
                            for q in range(len(saved)):
                                if saved[q].get("ID") == file[0].get("PID"):
                                    totalBurst = saved[q].get("CPUTimes") + totalBurst
                            file[0].update({'waitTime': str((((systemTime - file[0].get("arrival"))) / totalBurst)/1000.0) + "s"})
                            file[0].update({'IOwaitTime': str(0) + "s"})
                        schedulerPrint(file, [], [], (log))
                        break

                        #After each termination move the next shortest job to the front this is done in case the same process isnt the next shortest
                        
                    

                    
            except:
                pause = input("\nEnter Stop to exit or enter any key to resume: ")
                if pause == "Stop":
                   break
                else: 
                    pass
        schedulerPrint(file, [], [], (log))
        return log, file
    
  
       
def manualSimulation():

    while(True):
        next = input("Enter Next to continue: ")
        if next == "Next":
            break
        
def schedulerPrint(file, cpuTime, OItime, log):
    readyQueue = []
    oiQueue = []
    cpu = []
    oi =[]
    terminated = []
    os.system('clear')
    for i in range(len(file)):
        if file[i].get("State") == "Ready":
            readyQueue.append(file[i].get("name"))
        if file[i].get("State") == "Waiting":
            oiQueue.append(file[i].get("name"))
        if file[i].get("State") == "Running":
            cpu.append(file[i].get("name"))
        if file[i].get("State") == "OIRunning":
            oi.append(file[i].get("name"))
        if file[i].get("State") == "Terminated":
            terminated.append(file[i].get("name"))
    print("--------------------------------------------------" + "\nEnter C^C to Pause/Stop Simulation")
    print("--------------------------------------------------")
    print("Ready Queue: ", readyQueue)
    print("OI Waiting Queue: ", oiQueue)
    print("Process in CPU: ", cpu)
    print("Process in OI: ", oi)
    print("Terminated Queue: ", terminated)
    print("--------------------------------------------------" )
    if oi != [] and cpu != []:
        print("CPU: ", cpuTime[0], " OI: ", OItime[0])
    elif cpu == [] and oi == []:
        print("CPU: Idle    ", " OI: Idle")
    elif cpu == []:
        print("CPU: Idle    ", " OI: ", OItime[0])
    elif oi == []:
        print("CPU: ", cpuTime[0], " OI: Idle")
    print("--------------------------------------------------" )
    [print(i) for i in file]
    print("--------------------------------------------------" )
    for i in log:
            print(i)
    print("--------------------------------------------------" )


#Round Robing stuff
def RR(queue, Quantum):
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
#print((fileOpen("TestFiles/test1.txt"))[1].get("State"))
scheduler((fileOpen("TestFiles/testio.txt")), 1, 0, 1)
#print(RR(fileOpen("TestFiles/test1.txt")))
#termRun()

