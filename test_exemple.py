import unittest

#On copie la fct qu'on veut tester
def est_pair(nbr):
    return nbr % 2 == 0


class MonTest(unittest.TestCase):
    #On définit les outils qu'on aura besoin pour les tests
    def setUp(self):
        self.liste = list(range(100))
        self.value_test = 5

    def test_est_pair(self):
        #assertTrue -> si est_pair(2)est True, ça renvoie True sinon c False
        self.assertTrue(est_pair(2))
        #assertFalse -> si est_pair(1) est False, ça renvoie True sinon c False
        self.assertFalse(est_pair(1))
        self.assertEqual(True, est_pair(0))
        self.assertFalse(est_pair(self.value_test))

    def test_est_pair_avec_liste(self):
        for n in self.liste:
            self.assertEqual(est_pair(n), n % 2 == 0)

    def test_est_pair_positif(self):
        self.assertTrue(est_pair(2))
        self.assertFalse(est_pair(5))

    def test_est_pair_negatif(self):
        self.assertTrue(est_pair(-2))
        self.assertFalse(est_pair(-5))

    def test_est_pair_zero(self):
        self.assertTrue(est_pair(0))


if __name__ == "__main__":
    #Pour lancer les tests
    unittest.main()
