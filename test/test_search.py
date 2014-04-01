'''
Created on 23 Mar 2014

@author: mbaxkgo2
'''
from comp61542 import app
from os import path
import unittest 
import comp61542
from comp61542.database import database
from comp61542.views import showSearchAuthor

class TestFirst(unittest.TestCase):

    def setUp(self):
        dir, _ = path.split(__file__)
        data = "dblp_curated_sample.xml"
        comp61542.app.config['TESTING'] = True
        comp61542.app.config['DATASET'] = data
        comp61542.app.config['DATABASE'] = path.join(dir, "..", "data", data)
        self.data_dir = path.join(dir, "..", "data")
  
    def test_first_author_publications(self):
        db = database.Database()
        
        self.assertTrue(db.read(path.join(self.data_dir, "dblp_curated_sample.xml")))
        dat = db.get_coauthor_list('Stefano Ceri')

        self.assertEqual(dat[0], 'Piero Fraternali')
        self.assertEqual(dat[1], 'Carlo Batini')
        self.assertEqual(dat[2], 'Shamkant B. Navathe')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()