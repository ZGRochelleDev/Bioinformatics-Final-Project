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