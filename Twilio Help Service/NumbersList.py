import os, sys
import random
import numpy

list = []


 
def addtoFile(num):
    file = open("savedNumbers.txt","w") 
    file.write(num)
    file.close()
    file = open("savedNumbers.txt","r") 
    print file.read() 
    file.close()

def writeListToFile():
    file = open("savedNumbers.txt","w")

    for item in list:
        file.write("%s\n" % item)
    file.close()

def readtolist():
    file = open("savedNumbers.txt", "r")
    list = file.read().splitlines()
    file.close()

def addnum(PhNum):
    if list.count(PhNum) is 0:
        list.append(PhNum)
        addtoFile(PhNum)
    else:
        None
    writeListToFile()
    readtolist()
    print("registered: ")
    for x in list:
        print(x)

def removenum(PhNum):
    readtolist()
    list.remove(PhNum)
    writeListToFile()

def RetRandomNum():
    random.seed(a=None)
    lengthList = len(list)-1
    number = random.randint(0,lengthList)
    return list[number]