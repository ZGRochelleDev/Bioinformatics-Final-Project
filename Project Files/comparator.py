import re #Regular expression
# Why use dictionary over list. List and Dictionary lookup both O(1).
# A list(aka array) or dictionary could be used here, both are O(1) for lookup.
# Dictionaries take up more space in memory; hashing.
# The advantage here is for key-value relationship mapping.
# In this case below, the meaningful key is searched and the related value is returned.

codons = {'A': ['GCT', 'GCC', 'GCA', 'GCG'], 'R': ['CGT', 'CGC', 'CGG', 'AGA', 'AGG'], \
'N': ['AAT', 'AAC', 'AAU'], 'D': ['GAT', 'GAC', 'GAU'], 'C': ['TGT', 'TGC', 'UGU', 'UGC'], \
'Q': ['CAA', 'CAG'], 'E': ['GAA', 'GAG'], 'G': ['GGT', 'GGC', 'GGA', 'GGG', 'GGU'], \
'H': ['CAT', 'CAC', 'CAU'], 'I': ['ATT', 'ATC', 'ATA', 'AUU', 'AUC', 'AUA'], \
'L': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG', 'UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'], \
'K': ['AAA', 'AAG'], 'MET': ['ATG', 'AUG'], 'F': ['TTT', 'TTC', 'UUU', 'UUC'], 'P': ['CCT', 'CCC', 'CCA', 'CCG', 'CCU'], \
'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC', 'UCU', 'UCC', 'UCA', 'UCG', 'AGU'], 'T': ['ACT', 'ACC', 'ACA', 'ACG', 'ACU'], \
'W': ['TGG', 'UGG'], 'Y': ['TAT', 'TAC', 'UAU', 'UAC'], 'V': ['GTT', 'GTC', 'GTA', 'GTG', 'GUU', 'GUC', 'GUA', 'GUG'], \
'STOP': ['TAA', 'TGA', 'TAG', 'UAA', 'UGA', 'UAG']}

# Highlighter class for color Blue
class bcolors:
    blue = '\033[94m'
    ENDC = '\033[0m'

# readSamples() is called by compare()
# compare passes codonsList
# readSamples() highlites Stop codons	
def readSamples(codonsList):
    #use the regular expressions to find all occurrences of substring 'MET'
    global newcodonslist
    x =  [m.start() for m in re.finditer('MET', codonsList)]
    #xlength=len(x)
    for i in x:
        cut = codonsList[i:i+3]
        highlighter = bcolors.blue + cut + bcolors.ENDC
        newcodonslist = codonsList.replace(cut, highlighter)
    print newcodonslist

# object sequence is passed to compare (by assignment), from classMaker() in main.py
# object codonsList is passed to method readSamples above, by assignment
# variables are objects in python. Good articles: 
# https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747
# https://medium.com/school-of-code/passing-by-assignment-in-python-7c829a2df10a
def compare(sequence):
      newList = []
      x = 0
      y = len(sequence)
      for i in range(0,y):
            #The 'items() method' returns a list of tuple pairs: https://www.tutorialspoint.com/python/dictionary_items.htm
            for key, value in codons.items(): 
                  if sequence[i] in value:
                        newList.append(key)
      codonsList = "".join(newList)
      readSamples(codonsList)