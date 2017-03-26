'''
Created on Mar 15, 2017

@author: Utilizator
'''
import random

class Repository(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._entities={}
        self.undoList=[]
    
    def add(self,entity):
        '''
        input data:
            an entity of the form Entity
        output data:
            the entities with the new entity appended
        we store an entity in the repository by its id
        '''
#         self.__undoList.append(deepcopy(self._entities))
        self._entities[entity.id] = entity
        
           
    def getAll(self):
        '''
        returns all entities in repository
        '''
        return [x for x in self._entities.values()]
    
    def returnRandom(self):
        '''
        returns a randomID from the list of entities
        '''
        ids = []
        for id in self._entities.keys():
#            print(id)
#            print(self._entities[id])
            ids.append(id)
            
        '''
        in ids we have all the IDs
        '''
        rand = random.choice(ids)
        '''
        generate a random id
        '''
        return self._entities[rand]
        