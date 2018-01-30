def dictionaries(sequence, myRCList)

def rFrame1(sequence):
      dict1 = {}
      x = 0
      var = 0
      while x < len(sequence):
            dict1[var] = sequence[0+x:3+x]
            var = var + 1
            x = x + 3
      return dict1
      
def rFrame2(sequence):
      dict2 = {}
      x = 0
      var = 0
      while x < len(sequence):
            dict2[var] = sequence[1+x:4+x]
            var = var + 1
            x = x + 3
      return dict2
      
def rFrame3(sequence):
      dict3 = {}
      x = 0
      var = 0
      while x < len(sequence):
            dict3[var] = sequence[2+x:5+x]
            var = var + 1
            x = x + 3
      return dict3

def rFrame4(myRCList):
      dict4 = {}
      x = 0
      var = 0
      while x < len(myRCList):
            dict4[var] = myRCList[0+x:3+x]
            var = var + 1
            x = x + 3
      return dict4
      
def rFrame5(myRCList):
      dict5 = {}
      x = 0
      var = 0
      while x < len(myRCList):
            dict5[var] = myRCList[1+x:4+x]
            var = var + 1
            x = x + 3
      return dict5
      
def rFrame6(myRCList):
      dict6 = {}
      x = 0
      var = 0
      while x < len(myRCList):
            dict6[var] = myRCList[2+x:5+x]
            var = var + 1
            x = x + 3
      return dict6