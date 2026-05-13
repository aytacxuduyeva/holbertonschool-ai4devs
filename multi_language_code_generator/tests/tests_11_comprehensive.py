import unittest
from reference.log_analyzer import LogAnalyzer

class TestComprehensive(unittest.TestCase):
    def test_all_metrics(self):
        logs = [
            '10.0.0.1 - - [..] "GET" 200',
            '10.0.0.2 - - [..] "POST" 500',
            'invalid_line'
        ]
        res = LogAnalyzer().analyze(logs)
        self.assertEqual(res["total_requests"], 2)
        self.assertEqual(res["unique_visitors"], 2)

if __name__ == "__main__":
    unittest.main()
