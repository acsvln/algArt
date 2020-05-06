import unittest
from alg_euclid import euclid, euclidMutualSubst


class EuclidTest(unittest.TestCase):
    def testEuclid_8_6(self):
        assert euclid(8, 6) == 2

    def testEuclid_12_8(self):
        assert euclid(12, 8) == 4

    def testEuclid_180_168(self):
        assert euclid(180, 168) == 12

    def testEuclidMutualSubst_8_6(self):
        assert euclidMutualSubst(8, 6) == 2

    def testEuclidMutualSubst_12_8(self):
        assert euclidMutualSubst(12, 8) == 4

    def testEuclidMutualSubst_180_168(self):
        assert euclidMutualSubst(180, 168) == 12


if __name__ == "__main__":
    unittest.main()  # run all tests
