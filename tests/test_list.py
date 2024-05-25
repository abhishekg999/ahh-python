import unittest
from ahh_python.Functional import install

list_1000 = list(range(1000))


class TestList(unittest.TestCase):
    def setUp(self):
        install()

    def test_list_map(self):
        self.assertEqual([1, 2, 3].map(lambda x: x + 1).to_list(), [2, 3, 4])
        self.assertEqual(
            list_1000.map(lambda x: str(x)).to_list(), [str(x) for x in list_1000]
        )

    def test_list_filter(self):
        self.assertEqual([1, 2, 3].filter(lambda x: x % 2 == 0).to_list(), [2])
        self.assertEqual(
            list_1000.filter(lambda x: x % 2 == 0).to_list(),
            [x for x in list_1000 if x % 2 == 0],
        )

    def test_list_reduce(self):
        self.assertEqual([1, 2, 3].reduce(lambda x, y: x + y), 6)
        self.assertEqual(list_1000.reduce(lambda x, y: x + y), sum(list_1000))

    def test_list_for_each(self):
        a = []
        [1, 2, 3].for_each(lambda x: a.append(x))
        self.assertEqual(a, [1, 2, 3])

    def test_list_group_by(self):
        self.assertEqual(
            [1, 2, 3, 4, 5].group_by(lambda x: x % 2), {1: [1, 3, 5], 0: [2, 4]}
        )

    def test_list_chunk(self):
        self.assertEqual([1, 2, 3, 4, 5].chunk(2), [[1, 2], [3, 4], [5]])
        self.assertEqual([1, 2, 3, 4, 5].chunk(3), [[1, 2, 3], [4, 5]])

    def test_list_all(self):
        self.assertTrue([1, 2, 3].all(lambda x: x > 0))
        self.assertFalse([1, 2, 3].all(lambda x: x > 1))

    def test_list_any(self):
        self.assertTrue([1, 2, 3].any(lambda x: x > 1))
        self.assertFalse([1, 2, 3].any(lambda x: x < 0))

    def test_list_to_map(self):
        self.assertEqual([1, 2, 3].to_map(), {0: 1, 1: 2, 2: 3})
        self.assertEqual(list_1000.to_map(), {i: i for i in list_1000})

    def test_list_to_set(self):
        self.assertEqual([1, 2, 3].to_set(), {1, 2, 3})
        self.assertEqual(list_1000.to_set(), set(list_1000))


if __name__ == "__main__":
    unittest.main()
