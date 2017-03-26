'''
Created on Mar 15, 2017

@author: Utilizator
'''
import unittest
from repository.Repository import Repository
from controller.Controller import Controller
from domain.Entity import Entity

class Test(unittest.TestCase):


    def setUp(self):
        self.__repo=Repository()
        self.__ctrl=Controller(self.__repo)
        self.__entity1 = Entity("abcd efg ijk")
        self.__entity2=Entity("assde")
        self.__entity3=Entity("ujjefsf")
        self.__entity4=Entity("iuiuyit")


    def tearDown(self):
        pass


    def testName(self):
        self.__ctrl.add(self.__entity1)
        assert(len(self.__repo.getAll())==1)
        self.__ctrl.add(self.__entity2)
        self.__ctrl.add(self.__entity3)
        self.__ctrl.add(self.__entity4)
        r=self.__ctrl.returnRandom()
        s=self.__ctrl.swap(self.__entity1.string,0,1,2,1)
        print(s)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()