from operator import itemgetter
#Algorithims
def FCFS(file): 
    #Sorts the the list by arrival
    file = sorted(file, key=itemgetter("arrival"))
    return file
def SJF(file):
    
    return file
def PS(file):
    #sorts the list by its priority
    file = sorted(file, key=itemgetter("priority"))
    return file
#Stats
def CPUUsage():
    return None

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
                print(unkeyedList)
                if unkeyedList != []:
                    name = unkeyedList[0]
                    arrival = unkeyedList[1]
                    priority = unkeyedList[2]
                    while index <= len(unkeyedList):
                        CPUBurst.append(unkeyedList[index])
                        if index + 1 < len(unkeyedList):
                            IOBurst.append(unkeyedList[index + 1])
                        index = index + 2
                else:
                    break
                operationDict = {"name": name, "arrival":arrival, "priority": priority, "CPUBurst": CPUBurst, "IOBurst": IOBurst}
                operationList.append(operationDict)
            return operationList
        else:
             return None


print(fileOpen("TestFiles/testio.txt"))
 

