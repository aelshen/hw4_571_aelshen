'''
#==============================================================================
cky.py
/Users/aelshen/Documents/Dropbox/School/CLMS 2013-2014/Winter 2014/Ling 571-Deep Processing Techniques for NLP/hw2_571_aelshen/src/cky.py
Created on Jan 29, 2014
@author: aelshen
#==============================================================================
'''
from __future__ import print_function
import nltk 
import os
import sys

#==============================================================================
#--------------------------------Constants-------------------------------------
#==============================================================================
DEBUG = True

#==============================================================================
#-----------------------------------Main---------------------------------------
#==============================================================================
def main():
    if len(sys.argv) < 4:
        print("feature_parse.py requires 3 arguments" 
               + os.linesep + "(1)grammar file"
               + os.linesep + "(2)data file"
               + os.linesep + "(3)result file")
        sys.exit()
    
    grammar_file = "file:" + sys.argv[1]
    
    grammar = nltk.data.load(grammar_file)
    data_file = open(sys.argv[2], 'r')
    result_file = open(sys.argv[3], 'w')
    
    parser = nltk.parse.FeatureEarleyChartParser(grammar)
    
    for sentence in data_file.readlines():
        if not sentence.strip():
            continue
        
        sentence = sentence.strip().split()
        result_file.write(" ".join(sentence) )
        parse = parser.nbest_parse(sentence, 1)
        if parse:
            result_file.write(parse[0].pprint(margin=500) + os.linesep*2)
        else:
            result_file.write(os.linesep)
    
    print("Hello, World!")
#==============================================================================    
#---------------------------------Functions------------------------------------
#==============================================================================
##-------------------------------------------------------------------------
## test()
##-------------------------------------------------------------------------
##    Description:        description
##
##    Arguments:        arguments
##
##    Calls:                calls
##
##        Returns:            returns
##-------------------------------------------------------------------------
def test():
    print("Test")


#==============================================================================    
#------------------------------------------------------------------------------
#==============================================================================
if __name__ == "__main__":
    sys.exit( main() )