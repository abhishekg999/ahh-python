import unittest
from ahh_python.Functional import install

class TestList(unittest.TestCase):
    def setUp(self):
        install()

    def test_list_map(self):
        self.assertEqual([1, 2, 3].map(lambda x: x + 1).to_list(), [2, 3, 4])

        list1 = list(range(1000))
        self.assertEqual(list1.map(lambda x: str(x)).to_list(), [str(x) for x in list1])

if __name__ == '__main__':
    unittest.main()