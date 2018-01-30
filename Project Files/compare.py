import re
codons = {'A': ['GCT', 'GCC', 'GCA', 'GCG'], 'R': ['CGT', 'CGC', 'CGG', 'AGA', 'AGG'], \
'N': ['AAT', 'AAC', 'AAU'], 'D': ['GAT', 'GAC', 'GAU'], 'C': ['TGT', 'TGC', 'UGU', 'UGC'], \
'Q': ['CAA', 'CAG'], 'E': ['GAA', 'GAG'], 'G': ['GGT', 'GGC', 'GGA', 'GGG', 'GGU'], \
'H': ['CAT', 'CAC', 'CAU'], 'I': ['ATT', 'ATC', 'ATA', 'AUU', 'AUC', 'AUA'], \
'L': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG', 'UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'], \
'K': ['AAA', 'AAG'], 'MET': ['ATG', 'AUG'], 'F': ['TTT', 'TTC', 'UUU', 'UUC'], 'P': ['CCT', 'CCC', 'CCA', 'CCG', 'CCU'], \
'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC', 'UCU', 'UCC', 'UCA', 'UCG', 'AGU'], 'T': ['ACT', 'ACC', 'ACA', 'ACG', 'ACU'], \
'W': ['TGG', 'UGG'], 'Y': ['TAT', 'TAC', 'UAU', 'UAC'], 'V': ['GTT', 'GTC', 'GTA', 'GTG', 'GUU', 'GUC', 'GUA', 'GUG'], \
'STOP': ['TAA', 'TGA', 'TAG', 'UAA', 'UGA', 'UAG']}

class bcolors:
    blue = '\033[94m'
    ENDC = '\033[0m'
    
def readSamples(almostdone):
    global cut, highlighter ## Returns an error without stating global var: https://stackoverflow.com/questions/18002794/local-variable-referenced-before-assignment-in-python
    x =  [m.start() for m in re.finditer('MET', almostdone)]
    xlength=len(x)
    for i in x:
      cut = almostdone[i:i+3]
      highlighter = bcolors.blue + cut + bcolors.ENDC
    print almostdone.replace(cut, highlighter)

def compare(sequence):
      newList = []
      x = 0
      y = len(sequence)
      for i in range(0,y):
            for key, value in codons.items():
                  if sequence[i] in value:
                        newList.append(key)
      almostdone = "".join(newList)
      readSamples(almostdone)
