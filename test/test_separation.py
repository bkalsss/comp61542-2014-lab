import unittest
from comp61542.database.database import Author, Publication
from os import path
import comp61542
from comp61542.database import database


class Test(unittest.TestCase):

    def setUp(self):
        auth1 = Author("Author1")
        auth2 = Author("Author2")
        auth3 = Author("Author3")
        auth4 = Author("Author4")
        auth5 = Author("Author5")
        
        self.pub1 = Publication(0, "Pub1", "2002", [0, 1, 2])
        self.pub2 = Publication(3, "Pub2", "1999", [3, 0, 2])
        self.pub3 = Publication(1, "Pub3", "2012", [0])

        directory, _ = path.split(__file__)
        data = "dblp_curated_sample.xml"
        comp61542.app.config['TESTING'] = True
        comp61542.app.config['DATASET'] = data
        comp61542.app.config['DATABASE'] = path.join(directory, "..", "data", data)
        
        db = database.Database()
        db.authors = [auth1, auth2, auth3, auth4, auth5]
        db.author_idx = {"Author1":0, "Author2":1, "Author3":2, "Author4":3, "Author5":4}
        db.publications = [self.pub1, self.pub2, self.pub3]
        self.db = db
        comp61542.app.config['DATABASE'] = self.db

    def test_separation_list_correctly(self):
        anticipate = [[1, 1, 1, 1, 0], [1, 1, 1, 0, 0], [1, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
        self.db.get_result_authors_separation()
        self.assertEqual(anticipate, self.db.result_authors_separation)

    def test_authors_degree_of_separation(self):
        self.db.get_result_authors_separation()
        separation = self.db.get_authors_degree_of_separation(0, 3)
        self.assertEqual(0, separation)
        separation = self.db.get_authors_degree_of_separation(1, 3)
        self.assertEqual(1, separation)
        separation = self.db.get_authors_degree_of_separation(4, 3)
        self.assertEqual(-1, separation)
        separation = self.db.get_authors_degree_of_separation(3, 3)
        self.assertEqual(0, separation)


if __name__ == "__main__":
    unittest.main()