import unittest
from ahh_python.Functional import install

class TestList(unittest.TestCase):
    def setUp(self):
        install()

    def test_list_map(self):
        self.assertEqual([1, 2, 3].map(lambda x: x + 1).to_list(), [2, 3, 4])

        list1 = list(range(1000))
        self.assertEqual(list1.map(lambda x: str(x)).to_list(), [str(x) for x in list1])

    def test_list_filter(self):
        self.assertEqual([1, 2, 3].filter(lambda x: x % 2 == 0).to_list(), [2])

        list1 = list(range(1000))
        self.assertEqual(list1.filter(lambda x: x % 2 == 0).to_list(), [x for x in list1 if x % 2 == 0])

    def test_list_reduce(self):
        self.assertEqual([1, 2, 3].reduce(lambda x, y: x + y), 6)

        list1 = list(range(1000))
        self.assertEqual(list1.reduce(lambda x, y: x + y), sum(list1))

if __name__ == '__main__':
    unittest.main()