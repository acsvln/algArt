import sys
import unittest
import math
from alg_factorization import ferm


def testFerm(A):
    res = ferm(A)
    assert res[0] * res[1] == A


class EuclidTest(unittest.TestCase):
    # in the book there was (557, 563) answer
    def testFerm_31391(self):
        testFerm(31391)

    def testFerm_400(self):
        testFerm(400)

    def testFerm_99999(self):
        testFerm(99999)

    def testFerm_4012301(self):
        testFerm(4012301)

    # sadly uint32 is too big for our algo, so we use signed version
    def testFerm_int32(self):
        testFerm(2147483647)


if __name__ == "__main__":
    unittest.main()  # run all tests
