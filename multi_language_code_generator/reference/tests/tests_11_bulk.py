import unittest
from reference.log_analyzer import LogAnalyzer

class TestBulk(unittest.TestCase):
    def test_bulk_processing(self):
        logs = ['1.1.1.1 - - [..] "GET" 200'] * 100
        res = LogAnalyzer().analyze(logs)
        self.assertEqual(res["total_requests"], 100)
        self.assertEqual(res["unique_visitors"], 1)

if __name__ == '__main__':
    unittest.main()
