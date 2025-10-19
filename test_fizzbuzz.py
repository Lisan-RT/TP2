import unittest
from fizzbuzz import affiche  

class TestFizzBuzz(unittest.TestCase):

    def test_affiche_contient_mots(self):
        resultat = affiche() 
        self.assertIn("Fizz", resultat)
        self.assertIn("Buzz", resultat)
        self.assertIn("FrisBee", resultat)

    def test_affiche_15(self):
        resultat = affiche(15)
        self.assertIn("FrisBee", resultat)

if __name__ == "__main__":
    unittest.main()
