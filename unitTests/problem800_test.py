import unittest

target = __import__("problem800.py")
isPrime = target.isPrime


class TestProblem800(unittest.TestCase):
    def test_is_prime(self):
        n = 5
        result = isPrime(n)
        self.assertEqual(result, true)


if __name__ == "__main__":
    unittest.main()
