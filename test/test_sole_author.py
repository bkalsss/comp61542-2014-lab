'''
Created on 23 Mar 2014

@author: mbaxkgo2
'''
from comp61542 import app
from os import path
import unittest 
import comp61542
from comp61542.database import database

class TestFirst(unittest.TestCase):

    def setUp(self):
        dir, _ = path.split(__file__)
        data = "dblp_curated_sample.xml"
        comp61542.app.config['TESTING'] = True
        comp61542.app.config['DATASET'] = data
        comp61542.app.config['DATABASE'] = path.join(dir, "..", "data", data)
        self.data_dir = path.join(dir, "..", "data")
        
  
    def test_sole_author(self):
        db = database.Database()
        
        
        self.assertTrue(db.read(path.join(self.data_dir, "dblp_curated_sample.xml")))
        header, dat = db.get_sole_author(4)
        
        self.assertEqual(dat[0], ['Stefano Ceri', 78 , 33, 8])        
        self.assertEqual(dat[53], ['Khalid Belhajjame', 19 , 4, 2])
        self.assertEqual(dat[1], ['Piero Fraternali', 0 , 7, 0])


    def test_sole_author_by_publication(self):
        db = database.Database()
        
        
        self.assertTrue(db.read(path.join(self.data_dir, "dblp_curated_sample.xml")))
        header, dat = db.get_sole_author(2)
        
        self.assertEqual(dat[0], ['Stefano Ceri', 3 , 0, 0])        
        self.assertEqual(dat[53], ['Khalid Belhajjame', 0 , 0, 0])
        self.assertEqual(dat[1], ['Piero Fraternali', 0 , 1, 0])
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()