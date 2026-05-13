import unittest
from reference.log_analyzer import LogAnalyzer

class TestTopIps(unittest.TestCase):
    def test_top_ips(self):
        logs = [
            '1.1.1.1 - - [..] "GET" 200',
            '2.2.2.2 - - [..] "GET" 200',
            '1.1.1.1 - - [..] "GET" 200'
        ]
        res = LogAnalyzer().analyze(logs)
        self.assertEqual(res["total_requests"], 3)

if __name__ == '__main__':
    unittest.main()
