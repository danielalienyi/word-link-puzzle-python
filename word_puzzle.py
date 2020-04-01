
def getWords():
    # Opens a file named 'words.txt' and extracts all the words in it as list
    # 'words.txt' contains 50000+ dictionary words
    
    filename = "words.txt"    
    fh = open(filename,"r")              # read file
    words = fh.readline().split(" ")     # read the content and split into list
    fh.close()                           # close file handle
    return words

def mapCharacter(word):
    # count each letter in 'word' and return a map of letter against count
    # the key in the returend dictionary is letter in word and the value is the number of times it occurs in the word
    
    wordDict = {}     # initialize dictionary
    for c in word:
        wordDict[c] = wordDict.get(c,0) + 1  # increment current character count in dictionary. 
    return wordDict

def canFormWord(possibleCharMap, charMap):
    # checks if 'charMap' is a subset of 'possibleCharMap'
    # both inputs are dictionaries
    
    for c in charMap:
        if c not in possibleCharMap:  # return false if a character in 'charMap' is not in 'possibleCharMap'
            return False
        elif charMap[c] > possibleCharMap[c]:  # return false if a character occurs more in 'charMap' than in 'possibleCharMap'
            return False
    return True 
def getNLetterWords(words,possibleCharMap, n):
    # returns all n-letter words that can formed from the letters in dictionary 'possibleCharMap'
    # words is a list of dictionary words
    
    nLetterWords = []       # initialize result list
    for word in words:    # go through each word in words
        if len(word) == n and canFormWord(possibleCharMap,mapCharacter(word)): # check if current word is n-letter and also if the word is a subset of possibleCharMap
            nLetterWords.append(word)     # add current word to the result list once it passes the above checks
            
    return nLetterWords
    
def solveWordCrossPuzzle(possibleChars, *wordsLength):
    # possibleChars is a string of charcters from which to construct all words
    # *wordsLength is a variable parameter that represents a list of word lengths to be constructed
    # this function returns all dictionary words that can be constructed from 'possibleChars'.
    # The length of the returned words must be in 'wordsLength'
    
    lengthMap = {}
    possibleChars = possibleChars.lower()  # convert possibleChars to lower case
    possibleCharMap = mapCharacter(possibleChars) # map characters in 'possibleChar'
    for i in wordsLength:
        # map the number in wordsLength
        lengthMap[i] = lengthMap.get(i,0) + 1
        
    words = getWords()  # get all dictionary words
    result = []
    for i in lengthMap:
        result = result + getNLetterWords(words,possibleCharMap,i) # get words for each word length
    return result

    

solveWordCrossPuzzle("pile",3,3,3,4)

