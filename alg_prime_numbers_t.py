import unittest
from alg_prime_numbers import bruteforce, eratosthenes, sundaram, atkin


class PrimeNumbersTest(unittest.TestCase):
    def testBruteforce(self):
        assert bruteforce(self._N) == self._expected

    def testEratosthenes(self):
        assert eratosthenes(self._N) == self._expected

    def testSundaram(self):
        assert sundaram(self._N) == self._expected

    def testAtkin(self):
        assert atkin(self._N) == self._expected

    _N = 100

    _expected = [
        2, 3, 5, 7, 11, 13, 17, 19,
        23, 29, 31, 37, 41, 43, 47,
        53, 59, 61, 67, 71, 73, 79,
        83, 89, 97
    ]


if __name__ == "__main__":
    unittest.main()  # run all tests
