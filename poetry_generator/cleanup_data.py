'''
    Cleaning the Data

    Clean data should look like:
        [poem1, poem2, poem3, ... , poem n]

        poem1:    ex.   An ocean voyage.
                              As waves break over the bow,
                              the sea welcomes me.

                words: ['~', 'an', ' ', 'ocean', ' ', 'voyage', '.', '\n', '~', 'as', ' ', 'waves', ' ', 'break', ' ',
                           'over', ' ', 'the', ' ', 'bow', ',', '\n', 'the', ' ', 'sea', ' ', 'welcomes', ' ', 'me', '.']
           numLines: [3, 3, 3, 3, 3, 3, 3, 2, 2, ... , 0]

                so the inputs would look like: [3, '~'], [3, 'an'], [3, ' '], [3, 'ocean'], [3, ' '],
                                            [3, 'voyage'], [3, '.'], [3, '\n'], [2, '~'], [2, 'a'], ... [1, '.'], [0, 'EOP']
'''

import numpy as np
import re

alph =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
possibleChars = " ".join(alph) + '!"#$%&\'()*+,-./:;<=>?@[\\]^_`’{|}~\n'

def cleaning(f1, f):
    poemsString = f1.read()
    # replace all occurences of capitals with lower case
    
    upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    dictionary = dict(list(zip(upper, alph)))
    for key,val in dictionary.items():
        poemsString = poemsString.replace(key, "~"+val)
    poemsString = poemsString.replace("—", "-")
    
    poems =(poemsString.split("\n\n^^~e~o~p^^\n"))
    indices_to_pop = []
    
    for i in range(len(poems)):
        poem = (poems[i].strip(' \n'))
        if 'no poem here' in poem:
            poem = ''
            
        poemList = re.split('(\W)',  poem)
        
        # get rid of empty chars & hex values
        numLines = poemList.count('\n') + 1
        
        linesMore = 1
        for j in range(len(poemList)-1, -1, -1):
            n = poemList[j]
            if(n == '' or n[0] not in possibleChars):
                poemList.pop(j)
            else:
                # make a tuple of the lines left & the word
                poemList[j] = (linesMore, n)
                if n == '\n':
                    linesMore += 1
                
        if len(poemList) == 0:
            poemList = ['']
            indices_to_pop.append(i)
        
        # add a beginning of file, end of file, & number of lines
        numLines = poemList.count('\n') + 1
        poemList = ['^^{}', '^^{}', '^^{}', '^^{}'] + [numLines] + poemList + [(0,'*EOF')]
        
        poems[i] = poemList
        #poem = str(numLines) + '\n' + poem

    for index in range(len(indices_to_pop)-1, -1, -1): 
        poems.pop(index)

    f.write(str(poems))

    return poems
    

def main():
    poems = []

    # read in file
    '''
    f1 = open("raw_data/PoetryFoundationData1-10.txt", "r")
    f2 = open("raw_data/PoetryFoundationData11-20.txt", "r")
    f3 = open("raw_data/PoetryFoundationData21-30.txt", "r")
    f4 = open("raw_data/PoetryFoundationData31-40.txt", "r")
    f5 = open("raw_data/PoetryFoundationData41-50.txt", "r")

    poems += cleaning(f1)
    poems += cleaning(f2)
    poems += cleaning(f3)
    poems += cleaning(f4)
    poems += cleaning(f5)
    '''
    f1 = open("raw_data/PoetryFoundationData1.txt", "r")
    #f2 = open("raw_data/PoetryFoundationData2.txt", "r")
    #f3 = open("raw_data/PoetryFoundationData3.txt", "r")

    f = open("clean_data/fixed_data_small3.txt", 'w')
    
    poems += cleaning(f1, f)
    #poems += cleaning(f2, f)
    #poems += cleaning(f3, f)
    
    print(len(poems))
    

main()
