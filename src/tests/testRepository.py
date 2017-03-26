'''
Created on Mar 15, 2017

@author: Utilizator
'''
import unittest
from repository.Repository import Repository
from domain.Entity import Entity
from repository.FileRepository import FileRepository

class Test(unittest.TestCase):


    def setUp(self):
        self.__repo=Repository()
        self.__repo1=FileRepository("C:\\Users\\Utilizator\\Desktop\\scramble\\input")
        self.__entity1 =  Entity("asads")
        self.__entity2=Entity("assde")
        self.__entity3=Entity("ujjefsf")
        self.__entity4=Entity("iuiuyit")
    def tearDown(self):
        del self.__repo
        del self.__entity1 
        del self.__entity2 
        del self.__entity3 


    def testName(self):
        assert(len(self.__repo1.getAll())==5)
        self.__repo.add(self.__entity1)
        self.__repo.add(self.__entity2)
        self.__repo.add(self.__entity3)
        self.__repo.add(self.__entity4)
        assert(len(self.__repo.getAll())==4)
        r=self.__repo1.returnRandom()
        print(r)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()