import unittest
import app


class MyTestCase(unittest.TestCase):

    a0 = 1
    d = 4
    n = 5
    def setUp(self):
        self.app = app.app.test_client()

    def program(self):

        k = app.program(MyTestCase.a0, MyTestCase.d, MyTestCase.n)
        res = 17
        self.assertEqual(k, res)

    def test_prog(self):

        k = app.prog(MyTestCase.a0, MyTestCase.d, MyTestCase.n)
        res = 45
        self.assertEqual(k, res)



if __name__ == '__main__':
    unittest.main()
