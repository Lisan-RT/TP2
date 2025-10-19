import unittest 
from fizzbuzz import affiche 

def test_affiche():
    resultat = affiche()
    assert "Fizz" in resultat 
    assert "Buzz" in resultat 
    assert "FrisBee" in resultat

if __name__ == "__main__":
    unittest.main()