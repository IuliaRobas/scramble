'''
Created on Mar 15, 2017

@author: Utilizator
'''
import unittest
from domain.Entity import Entity

class Test(unittest.TestCase):


    def setUp(self):
        self.__entity1 =  Entity("abcd")
        self.__entity2 = Entity("ab cd ef gh")


    def tearDown(self):
        del self.__entity1 
        del self.__entity2 


    def testName(self):
        assert(self.__entity2.score == 8)
        assert(self.__entity1.string=="abcd")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()