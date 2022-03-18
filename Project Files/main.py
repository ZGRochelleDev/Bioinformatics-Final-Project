import os
import compareCodons
#from import *

class Rframe(object):
    def __init__(self, input, num1, num2):
        self.input = input
        self.num1 = num1
        self.num2 = num2
        
    def format(self):
        self.dict1 = {}
        var = 0
        x = 0
        while x < len(self.input):
            self.dict1[var] = self.input[self.num1+x:self.num2+x]
            var = var + 1
            x = x + 3
        return self.dict1

def classMaker(sequence, myRCList):
    print("\n")
    print("Reading frame 1: ")
    Rframe1 = Rframe(sequence, 0, 3)
    compareCodons.compare(Rframe1.format())
    print("\n")
    print("Reading frame 2: ")
    Rframe2 = Rframe(sequence, 1, 4)
    compareCodons.compare(Rframe2.format())
    print("\n")
    print("Reading frame 3: ")
    Rframe3 = Rframe(sequence, 2, 5)
    compareCodons.compare(Rframe3.format())
    print("\n")
    print("Reading frame 4: ")
    Rframe4 = Rframe(myRCList, 0, 3)
    compareCodons.compare(Rframe4.format())
    print("\n")
    print("Reading frame 5: ")
    Rframe5 = Rframe(myRCList, 1, 4)
    compareCodons.compare(Rframe5.format())
    print("\n")
    print("Reading frame 6: ")
    Rframe6 = Rframe(myRCList, 2, 5)
    compareCodons.compare(Rframe6.format())

#sequence is being passed as a string, placed into a list >> in order to use the "insert" method
def reverseComplement(sequence):
    seqList = list(sequence)
    revcompList = []
    for i in range(len(seqList)):
        if seqList[i] == "A":
            revcompList.insert(i, "T")
        if seqList[i] == "T":
            revcompList.insert(i, "A")
        if seqList[i] == "G":
            revcompList.insert(i, "C")
        if seqList[i] == "C":
            revcompList.insert(i, "G")
        if seqList[i] == "U":
            revcompList.insert(i, "A")
    return "".join(revcompList)

#This file reader handles:
    # - lowercase
    # - 'newlines'
    # - statements that start with " > "
def readSequence(sequenceFile):
    myList = [ ]
    fileDir = os.path.dirname(os.path.realpath(__file__)) + "\\" + sequenceFile + ".txt"
    with open(fileDir, 'r') as myfile:
        for line in myfile:
            if ('>' not in line):
                myList.append(line.replace('\n', ''))
    sequence = "".join(myList)
    return sequence.upper()

if __name__ == '__main__':
    sequenceFile = str(input("Enter the name of your txt file containg your dna/rna without the .txt: "))
    defaultSequence = readSequence(sequenceFile)
    reverseComplement = reverseComplement(defaultSequence)
    classMaker(defaultSequence, reverseComplement)
