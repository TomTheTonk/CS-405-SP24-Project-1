
import os
import time

"""
    Sorts the processes by arrival to for FCFS

    :param file: list of processes to be run on
    :type: list of dictionaries
    :return: file, list sorted by arrival time
    :rtype: list
    """
def FCFS(file): 
    #Sorts the the list by arrival
    file = sorted(file, key=lambda x: x['arrival'])
    return file
"""
    Sorts the processes by CPUBursts then by arrival time for SJF

    :param file: list of processes to be run on
    :type: list of dictionaries
    :return: file, list sorted by CPUBursts time
    :rtype: list
    """
def SJF(file):
    file = sorted(file, reverse=False, key=lambda x: ( x['CPUBurst'][0], x['arrival']))
    return file
"""
    Sorts the processes by priority for PS

    :param file: list of processes to be run on
    :type: list of dictionaries
    :return: file, list sorted by priority
    :rtype: list
    """
def PS(file):
    #sorts the list by its priority
    file = sorted(file, key=lambda x: x['priority'])
    return file
  

"""
    Saves and writes the logs and processes output to a file.

    :param file: list of processes and their data
    :type: list of dictionaries
    :param log: list of the logs from running the processes
    :type: list of strings
    :return: a file with all the logs and process
    :rtype: file
    """
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

    """
    Main menu to start and the code.

    :param: None
    :type: None
    :return: None
    :rtype: None
    """
def termRun():
    algorithim = 0
    file = None
    log = []
    #Entry parameters to be set
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
    #Main Menu
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
        #Match Case to pick which option from menu
        match(selection):
            case 1: 
                try {
                    File myObj = new File("filename.txt");
                    Scanner myReader = new Scanner(myObj);
                    while (myReader.hasNextLine()) {
                        String data = myReader.nextLine();
                        System.out.println(data);
                    }
                    myReader.close();
                    } catch (FileNotFoundException e) {
                    System.out.println("File not Found");
                    e.printStackTrace();
                    } finally {
                        System.out.print("Contents Saved")
                    }
            case 2:
                #Which algorithm to run the process on
                print("Select an algorithm")
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
                #Run the processes
                log, file = scheduler(file, log, mode, simTime)
            case 4:
                #Save the output
                saveFiles(file, log)
            case 5:
                break


#File Processing
"""
    Takes a directory given and writes it to a list of dictionaries 

    :param fileName: name of the file to write to the list of dictionaries
    :type: String
    :return: A list of dictionaries  with all the info on the file written to it
    :rtype: list
    """
def fileOpen(fileName):
        operationList = []
        #Have PID start with 1 for my own preference
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
                #One index of the list
                operationDict = {"name": name, "PID": PID, "arrival":arrival, "priority": priority, "CPUBurst": CPUBurst, "IOBurst": IOBurst, "State": "New", "arrivalTime": None, "finishTime": None, "turnAround": None, "waitTime": None, "IOwaitTime": None}
                PID = PID + 1
                #Append the one dictionary to the list
                operationList.append(operationDict)
                
            return operationList
        else:
             return None



#Scheduler
"""
    Takes the preferences and selections from the main menu and simulates a CPU 
    It is split into two. If algorithim is 0 or 3(FCFS and PS) then it runs process by process if algorithim is 1 or SJF it always runs on the first index of the file but sorts it to move the next process to the top
    After running it saves the movements of processes to log and all info from running the process on the list of dictionaries
    :param file: list of dictionaries with all the process and info stored on it
    :type: List
    :param algorithm: an int that holds which algorithim the scheduler will run 
    :type: int
    :param sim: Simulation Mode can be 0 or 1(Auto Manual)
    :type: int
    :param simTime: int that stores which metric the results of the simulation will be in. Msecs or Seconds
    :type: int
    :return log: list of the changes in the scheduler such as processes moving to readyqueue
    :rtype: list
    :return file: list of dictionaries with all the output data stored on it
    :type: list
    """
def scheduler(file, algorithim, sim, simTime):
    aveWaitTime = 0
    aveTurnaround = 0
    Throughput = 0
    log = []
    systemTime = 0
    #Stores all CPUtimes for later computing 
    saved = [] 
    for t in range(len(file)):
        saved.append({"ID": file[t].get("PID"), "CPUTimes": sum(file[t].get("CPUBurst")), "IOTimes": sum(file[t].get("IOBurst"))})
    totalIOBurst = 0
    totalBurst = 0
    #sort the list by its algortim 
    match(algorithim):
        case 0: 
            file = FCFS(file)
                        
        case 1: 
            file = SJF(file)
                        
        case 2: 
            file = PS(file)

    schedulerPrint(file, [], [], "")                    
    #Move all processes from new to ready queue
    for p in range(len(file)):
        if file[p].get("State") == "New":
            file[p].update({'State': "Ready"})
            log.append(file[p].get("name") + " was added to ready queue")
    #To run if FCFS or PS
    if algorithim != 1:
        totalRun = 0 #how many times the scheduler should run
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
                    #If in ready queue or if the process has cpubursts left and has no iobursts
                    if (file[p].get("State") == "Ready" and cpuTime != []) or (file[p].get("State") == "Running" and oiTime == [] and cpuTime != []):
                        #if in ready queue move to the running queue
                        if file[p].get("State") == "Ready":
                            file[p].update({'State': "Running"})
                            log.append(file[p].get("name") + " was added to the CPU")
                        #print(file[p].get("name") + " was added to the CPU")
                            
                        #if in manual or auto mode
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
                    # if waiting for the OI 
                    elif file[p].get("State") == "Waiting" and oiTime != []: 
                    
                        log.append(file[p].get("name") + " was added to the IO")
                        #print(file[p].get("name") + " was added to the IO")

                        #Add to the OI
                        file[p].update({'State': "OIRunning"})
                        #If in manual or auto mode
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
                    #If has oibursts to run after the cpu add to the oi queue            
                    if oiTime != [] and file[p].get("State") == "Running":
                        file[p].update({'State': "Waiting"})
                        log.append(file[p].get("name") + " was added to the waiting queue for the IO")
                        #print(file[p].get("name") + " was added to the waiting queue for the IO")
                        schedulerPrint(file, [], [], (log))
                    #If it is finsihed running in the OI and has cpubursts add back to ready queue
                    elif cpuTime != [] and file[p].get("State") == "OIRunning":
                        file[p].update({'State': "Ready"})
                        log.append(file[p].get("name") + " was added to the ready queue")
                        #print(file[p].get("name") + " was added to the ready queue")
                        schedulerPrint(file, cpuTime, oiTime, (log))
                    #IF it has no oibursts or cpubursts add to terminated queue and add all the metrics
                    elif oiTime == [] and cpuTime == []:
                        file[p].update({'State': "Terminated"})
                        log.append(file[p].get("name") + " was added to terminated queue")
                        #print(file[p].get("name") + " was added to terminated queue")

                        #If in seconds or milliseconds
                        if simTime == 1:
                            #Since it is in the ready queue at the start put 0 for arrivalTime
                            file[p].update({'arrivalTime': str(0)+"ms" })
                            file[p].update({'finishTime': str(systemTime) + "ms"})
                            file[p].update({'turnAround': str((systemTime))+"ms"})
                            #Grab the Cpu and Oi count since we pop them from the file 
                            for q in range(len(saved)):
                                if saved[q].get("ID") == file[p].get("PID"):
                                    totalBurst = saved[q].get("CPUTimes") + totalBurst
                                    totalIOBurst = saved[q].get("IOTimes") + totalIOBurst
                            file[p].update({'waitTime': str((systemTime / totalBurst)) + "ms"})
                            file[p].update({'IOwaitTime': str(0)+"ms"})

                        elif simTime == 0:
                            file[p].update({'arrivalTime': str(0)+"s" })
                            file[p].update({'finishTime': str((systemTime)/1000.0) + "s"})
                            file[p].update({'turnAround': str((systemTime)/1000.0)+"s"})
                            for q in range(len(saved)):
                                if saved[q].get("ID") == file[p].get("PID"):
                                    totalBurst = saved[q].get("CPUTimes") + totalBurst
                                    totalIOBurst = saved[q].get("IOTimes") + totalIOBurst
                            file[p].update({'waitTime': str((systemTime / totalBurst)/1000.0) + "s"})
                            file[p].update({'IOwaitTime': str((systemTime / totalIOBurst)/1000.0)+ "s"})
                        aveWaitTime = aveWaitTime + ((systemTime / totalBurst))
                        aveTurnaround = aveTurnaround + (systemTime)

                        #"arrivalTime": None, "finishTime": None, "turnAround": None, "waitTime": None, "IOwaitTime": None}
                        schedulerPrint(file, [], [], (log))
                        break
            #If you control c then it runs this. Not the best way to stop and pause since if you have any error it will run
            except:
                pause = input("Enter Stop to exit or enter any key to resume: ")
                if pause == "Stop":
                   break
                else: 
                    pass
        aveTurnaround = aveTurnaround / len(file)
        aveWaitTime = aveWaitTime / len(file)
        Throughput = len(file) / systemTime
        if simTime == 0:
            log.append("--------------------------------------------------")
            log.append("Average Throughput: " + str(Throughput)+ " per ms, Average WaitTime: " + str(aveWaitTime) + " ms, Average Turnaround Time: "+ str(aveTurnaround) + " per ms" )
        elif simTime == 1:
            log.append("--------------------------------------------------")
            log.append("Average Throughput: " + str(Throughput/1000)+ " per s, Average WaitTime: " + str(aveWaitTime/1000) + " s, Average Turnaround Time: "+ str(aveTurnaround /1000) + " per s" )
        schedulerPrint(file, [], [], (log))
        return log, file
    #To run if SJF
    #Main difference from above is the need to recheck for the shortest job to do. This is done by resorting each run for the shortest to be at the top
    #It is very similar to above and could be merged though time management issues got in the way

    else:
        #Totalrun is an array for SJF
        totalRun = []
        for p in range(len(file)):
            totalRun.extend(file[p].get("IOBurst")) # list of oi times
            totalRun.extend(file[p].get("CPUBurst")) #list of cpu times)
       
        for p in range(len(totalRun)):
            #Remove the terminated processes from the file and append to the end so to not throw index error
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
                #While it is not 0 keep running or compute to do. Runs one process and OI process then resorts
                while(currIO != 0 or currCPU != 0):

                    if (file[0].get("State") == "Ready" and cpuTime != []) or (file[0].get("State") == "Running" and oiTime == [] and cpuTime != []):
                        if file[0].get("State") == "Ready":
                            file[0].update({'State': "Running"})
                            log.append(file[0].get("name") + " was added to the CPU")
                        #print(file[p].get("name") + " was added to the CPU")
                        #Check if in auto or manual mode
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
                    #If in waiting queue for OI add to the IO   
                    elif file[0].get("State") == "Waiting" and oiTime != []: 
                    
                        log.append(file[0].get("name") + " was added to the IO")
                        #print(file[p].get("name") + " was added to the IO")
                        file[0].update({'State': "OIRunning"})
                        schedulerPrint(file, [], oiTime, (log))
                        #Check if in manual or auto mode
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
                    #If running and has  Io bursts left add to waiting queue
                    if oiTime != [] and file[0].get("State") == "Running":
                        file[0].update({'State': "Waiting"})
                        log.append(file[0].get("name") + " was added to the waiting queue for the IO")
                        #print(file[p].get("name") + " was added to the waiting queue for the IO")
                        schedulerPrint(file, [], [], (log))
                    #If it has CPUbursts left and is in the oi add back to the readyqueue
                    elif cpuTime != [] and file[0].get("State") == "OIRunning":
                        file[0].update({'State': "Ready"})
                        log.append(file[0].get("name") + " was added to the ready queue")
                        #print(file[p].get("name") + " was added to the ready queue")
                        schedulerPrint(file, cpuTime, oiTime, (log))
                    #IF has no more oi or cpu bursts terminate and add info
                    elif oiTime == [] and cpuTime == []:
                        file[0].update({'State': "Terminated"})
                        log.append(file[0].get("name") + " was added to terminated queue")
                        #print(file[p].get("name") + " was added to terminated queue")

                        #Check which metrics to return with
                        if simTime == 1:
                            file[0].update({'arrivalTime': "0ms" })
                            file[0].update({'finishTime': str(systemTime) + "ms"})
                            file[0].update({'turnAround': str(systemTime)+"ms"})
                            for q in range(len(saved)):
                                if saved[q].get("ID") == file[0].get("PID"):
                                    totalBurst = saved[q].get("CPUTimes") + totalBurst
                                    totalIOBurst = saved[q].get("IOTimes") + totalIOBurst
                            file[0].update({'waitTime': str((systemTime) / totalBurst) + "ms"})
                            file[0].update({'IOwaitTime': str(systemTime / totalIOBurst)+ "ms"})
                        if simTime == 0:
                            file[p].update({'arrivalTime': str(0)+"s" })
                            file[0].update({'finishTime': str(systemTime/1000.0) + "s"})
                            file[0].update({'turnAround': str((systemTime)/1000.0)+"s"})
                            for q in range(len(saved)):
                                if saved[q].get("ID") == file[0].get("PID"):
                                    totalBurst = saved[q].get("CPUTimes") + totalBurst
                                    totalIOBurst = saved[q].get("IOTimes") + totalIOBurst
                            file[0].update({'waitTime': str((((systemTime)) / totalBurst)/1000.0) + "s"})
                            file[0].update({'IOwaitTime': str(systemTime / totalIOBurst) + "s"})
                        aveWaitTime = aveWaitTime + ((systemTime / totalBurst))
                        aveTurnaround = aveTurnaround + (systemTime)
                        schedulerPrint(file, [], [], (log))
                        break

                        #After each termination move the next shortest job to the front this is done in case the same process isnt the next shortest
                        
                    

                    
            except:
                pause = input("\nEnter Stop to exit or enter any key to resume: ")
                if pause == "Stop":
                   break
                else: 
                    pass
        aveTurnaround = aveTurnaround / len(file)
        aveWaitTime = aveWaitTime / len(file)
        Throughput = len(file) / systemTime
        if simTime == 0:
            log.append("--------------------------------------------------")
            log.append("Average Throughput: " + str(Throughput)+ " per ms, Average WaitTime: " + str(aveWaitTime) + " ms, Average Turnaround Time: "+ str(aveTurnaround) + " per ms" )
        elif simTime == 1:
            log.append("--------------------------------------------------")
            log.append("Average Throughput: " + str(Throughput/1000)+ " per s, Average WaitTime: " + str(aveWaitTime/1000) + " s, Average Turnaround Time: "+ str(aveTurnaround /1000) + " per s" )
        schedulerPrint(file, [], [], (log))
        return log, file
    
  
"""
    The scheduler console look prints the stop and pause, queues, CPU and IO, the list of directories, and log as the scheduler runs
    :param file: list of dictionaries with all the process and info stored on it
    :type: List
    :param cpuTime: list with the current cpu bursts on it
    :type: list
    :param OItime: list with the current ioBursts on it
    :type: list
    :return log: list of the changes in the scheduler such as processes moving to readyqueue
    :rtype: None
    :return: Prints the info in the console
   
"""

def schedulerPrint(file, cpuTime, OItime, log):
    readyQueue = []
    oiQueue = []
    cpu = []
    oi =[]
    terminated = []
    #Clear each run to keep console clean
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
#RR we never got to finish and include
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

