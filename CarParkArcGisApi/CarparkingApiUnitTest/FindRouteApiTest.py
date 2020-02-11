import unittest

import sys

class Test_FindRouteApiTest(unittest.TestCase):
    def setUp(self):
        self.distance = GetTimeAndDistance()

    def test_A(self):
        self.fail("Not implemented")

if __name__ == '__main__':
    import xmlrunner

    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        failfast=False,
        buffer=False,
        catchbreak=False)