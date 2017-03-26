'''
Created on Mar 15, 2017

@author: Utilizator
'''
import random
from copy import deepcopy

class Controller(object):
    '''
    bridge between console and repository
    '''


    def __init__(self, repo):
        '''
        Constructor
        initializes the repository
        '''
        self.__repo = repo
        self.__undoList=[]
        
    def undo(self,scrambled):
        '''
        returns the operation before the last swap
        raises:
            IndexError if there are no swaps to undo
        '''        
        try:
            scrambled=self.__undoList.pop()
        except IndexError:
            raise Exception("There are no other operations to undo")
        return scrambled   
        
    def add(self,entity):
        '''
        adds an entity
        '''
        self.__repo.add(entity)  
         
    def getAll(self):
        '''
        returns all entities
        '''
        return self.__repo.getAll()
    
    #def swap(self,word1,letter1,word2,letter2):
    #    '''
    #    swaps two words with the corresponding letters
    #    '''
    #    return self.__repo.swap(word1,letter1,word2,letter2)
        
    def returnRandom(self):
        '''
        returns a random entity
        '''
        return self.__repo.returnRandom()
    
    def stringToList(self,string):
        '''
        converts a string into a list
        '''
        l=[]
        for c in string:
            l.append(c)
        return l
    def listToString(self,l):
        '''
        converts a list into a string
        '''
        string=""
        for elem in l:
            string=string+elem
        return string
        
    def getScore(self,entity):
        return entity.score
        
    def scramble(self,entity):
        length=entity.get_score()
        string=self.stringToList(entity.get_string())
        timesForShuffle=random.randint(0,100)
        for i in range(timesForShuffle):
            a=random.randint(1,length-2)
            b=random.randint(1,length-2)
            if string[a] != " " and string[b] != " " and string[a-1]!=" " and string[b-1]!=" ":
                string[a],string[b]=string[b],string[a]
        return self.listToString(string)
                
    def getNumberOfWords(self,string):
        w=0
        for i in range(len(string)):
            if string[i]==" ":
                w+=1;
        return w+1
    
    def getPosition(self,string,word,letter):
        '''
        i=0
        length=0
        if word>0:
            length+=1
        while word>0:
            length+=1
            i+=1
            if string[i]==" ":
                word-=1
        length+=1
        '''
        i=0
        words=0
        letters=0
        
        if word==0:
            return letter
        pos=0
        while word>0:
            if string[pos]==" ":
                word-=1
            pos+=1
        while letter>0:
            pos+=1
            letter-=1  
        return pos
    
    def swap(self,theWord,word1,letter1,word2,letter2):
      
        
        w=self.getNumberOfWords(theWord)  
        if word1<0 or word1>w-1 or word2<0 or word2>w-1:
            raise Exception("Incorrect indices! ")        
        if word1==word2:
            if letter1==0 or letter1==len(theWord)-1:
                raise Exception("You cannot swap the first or last letter of a word! ")
        
        #if letter1==0 or letter1==len(theWord[word1])-1 or letter2==0 or letter2==len(theWord[word2])-1:
        #    raise Exception("You cannot swap the first or last letter of a word! ")
        self.__undoList.append(deepcopy(theWord))
        theWord=self.stringToList(theWord)
        pos1=self.getPosition(theWord, word1, letter1)
        pos2=self.getPosition(theWord, word2, letter2)

        if pos1==0 or pos1==len(theWord)-1 or theWord[pos1+1]==" " :
            raise Exception("You cannot swap the first or last letter of a word! ")
        if pos2==0 or pos2==len(theWord)-1 or theWord[pos2+1]==" " :
            raise Exception("You cannot swap the first or last letter of a word! ")
        
        theWord[pos1], theWord[pos2] = theWord[pos2],theWord[pos1]
        theWord=self.listToString(theWord)
        return theWord
    
          
   
        