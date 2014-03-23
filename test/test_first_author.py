'''
Created on 23 Mar 2014

@author: mbaxkgo2
'''
import unittest 
from comp61542.database import database

class TestFirst(unittest.TestCase):

    def setUp(self):
        pass

    def test_first_author_publications(self):
        self.assertEqual(darabase.mean([]), 0)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()