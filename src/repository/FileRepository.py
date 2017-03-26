'''
Created on Mar 15, 2017

@author: Utilizator
'''
from repository.Repository import Repository
from domain.Entity import Entity
class FileRepository(object):
    '''
    classdocs
    '''


    def __init__(self, fileName):
        '''
        Constructor
        '''
        Repository.__init__(self)
        self.__fileName = fileName
        self.__loadFromFile()
        
    def add(self, entity):
        Repository.add(self, entity)
        
    def getAll(self):
        return Repository.getAll(self) 
       
    def __loadFromFile(self):
        try:
            f=open(self.__fileName,"r")
            line=f.readline().strip()
            while line!="":
                '''
                we create an entity from every line of the file and add it to the repository
                '''
                entity=Entity(line)
                '''
                and add it in the repository
                '''
                Repository.add(self, entity)
                #we continue parsing the file
                line=f.readline().strip()
        except IOError:
            raise Exception()
        finally:
            f.close()
    def returnRandom(self):
        return Repository.returnRandom(self)