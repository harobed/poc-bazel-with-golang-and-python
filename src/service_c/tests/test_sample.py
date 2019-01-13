import unittest
from service_c import app


class TestSample(unittest.TestCase):
    def test_ok(self):
        print(42)

        self.assertEquals(42, 42)


if __name__ == "__main__":
    unittest.main()
