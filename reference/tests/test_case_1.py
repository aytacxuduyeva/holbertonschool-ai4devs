import pytest
from log_analyzer import LogAnalyzer

def test_case_1():
    analyzer = LogAnalyzer()
    line = '127.0.0.1 - - [10/Oct/2000:13:55:36 -0700] "GET /test_1 HTTP/1.0" 200 2326'
    assert analyzer.parse_line(line)["status"] == 200
