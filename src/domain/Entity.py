'''
Created on Mar 15, 2017

@author: Utilizator
'''

class Entity(object):

    '''
    classdocs
    '''


    def __init__(self, string):
        '''
        Constructor
        '''
        self.__string = string
        self.__id = id(self)
        l=len(self.__string)
        for i in range(0,l):
            if self.__string[i] == " ":
                l=l-1
        self.__score = l
    def __str__(self):
        return self.__string
    def get_string(self):
        return self.__string


    def get_id(self):
        return self.__id


    def get_score(self):
        return self.__score


    def set_string(self, value):
        self.__string = value


    def set_id(self, value):
        self.__id = value


    def set_score(self, value):
        self.__score = value


    def del_string(self):
        del self.__string


    def del_id(self):
        del self.__id


    def del_score(self):
        del self.__score

    string = property(get_string, set_string, del_string, "string's docstring")
    id = property(get_id, set_id, del_id, "id's docstring")
    score = property(get_score, set_score, del_score, "score's docstring")
        