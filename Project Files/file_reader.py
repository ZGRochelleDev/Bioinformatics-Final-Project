#This file reader handles:
        # - lowercase
        # - 'newlines'
        # - statements that start with " > "

def readSequence(sequenceFile):
        myList = [ ]
        with open(sequenceFile + ".txt", 'r') as myfile:
            for line in myfile:
                if ('>' not in line):
                  myList.append(line.replace('\n', ''))
        sequence = "".join(myList)
        return sequence.upper()