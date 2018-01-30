#sequence is being passed as a string, placed into a list >> in order to use the "insert" method

def foo(sequence):
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