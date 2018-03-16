import file_reader
import reverse_complement
import comparator
import rFrameClass
#from rFrameClass import *

def classMaker(sequence, myRCList):
      print "\n"
      print "Reading frame 1: "
      Rframe1 = rFrameClass.Rframe(sequence, 0, 3)
      comparator.compare(Rframe1.format())
      print "\n"
      print "Reading frame 2: "
      Rframe2 = rFrameClass.Rframe(sequence, 1, 4)
      comparator.compare(Rframe2.format())
      print "\n"
      print "Reading frame 3: "
      Rframe3 = rFrameClass.Rframe(sequence, 2, 5)
      comparator.compare(Rframe3.format())
      print "\n"
      print "Reading frame 4: "
      Rframe4 = rFrameClass.Rframe(myRCList, 0, 3)
      comparator.compare(Rframe4.format())
      print "\n"
      print "Reading frame 5: "
      Rframe5 = rFrameClass.Rframe(myRCList, 1, 4)
      comparator.compare(Rframe5.format())
      print "\n"
      print "Reading frame 6: "
      Rframe6 = rFrameClass.Rframe(myRCList, 2, 5)
      comparator.compare(Rframe6.format())

if __name__ == '__main__':
      sequenceFile = str(raw_input("Enter the name of your txt file containg your dna/rna without the .txt: "))
      defaultSequence = file_reader.readSequence(sequenceFile)
      reverseComplement = reverse_complement.foo(defaultSequence)

      classMaker(defaultSequence, reverseComplement)
