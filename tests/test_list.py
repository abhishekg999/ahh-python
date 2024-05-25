import unittest
from ahh_python.Functional import install

class TestList(unittest.TestCase):
    def setUp(self):
        install()

    def test_list_map(self):
        self.assertEqual([1, 2, 3].map(lambda x: x + 1).to_list(), [2, 3, 4])

if __name__ == '__main__':
    unittest.main()