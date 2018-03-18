import sys
import random
import numpy

list = []

def addnum(PhNum):
    list.append(PhNum)

def removenum(PhNum):
    list.remove(PhNum)

def RetRandomNum():
    random.seed(a=None)
    lengthList = len(list)-1
    number = random.randint(0,lengthList)
    return list[number]
 