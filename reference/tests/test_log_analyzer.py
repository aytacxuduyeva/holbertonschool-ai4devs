import pytest
from log_analyzer import LogAnalyzer

@pytest.fixture
def analyzer():
    return LogAnalyzer()

def test_1_status_200(analyzer):
    assert analyzer.parse_line('127.0.0.1 - - [10/Oct/2000:13:55:36 -0700] "GET / HTTP/1.0" 200 2326')["status"] == 200

def test_2_status_404(analyzer):
    assert analyzer.parse_line('127.0.0.1 - - [10/Oct/2000:13:55:36 -0700] "GET /api HTTP/1.0" 404 123')["status"] == 404

def test_3_status_500(analyzer):
    assert analyzer.parse_line('127.0.0.1 - - [10/Oct/2000:13:55:36 -0700] "POST /login HTTP/1.0" 500 0')["status"] == 500

def test_4_status_403(analyzer):
    assert analyzer.parse_line('127.0.0.1 - - [10/Oct/2000:13:55:36 -0700] "GET /admin HTTP/1.0" 403 123')["status"] == 403

def test_5_analyze_success_rate(analyzer):
    lines = ['... 200 ...', '... 200 ...']
    assert analyzer.analyze(lines)["error_rate"] == 0.0

def test_6_analyze_error_rate(analyzer):
    lines = ['... 404 ...', '... 500 ...']
    assert analyzer.analyze(lines)["error_rate"] == 100.0

def test_7_analyze_mixed(analyzer):
    lines = ['... 200 ...', '... 404 ...']
    assert analyzer.analyze(lines)["error_rate"] == 50.0

def test_8_total_count(analyzer):
    lines = ['... 200 ...', '... 200 ...', '... 200 ...']
    assert analyzer.analyze(lines)["total_requests"] == 3

def test_9_empty_list(analyzer):
    assert analyzer.analyze([])["total_requests"] == 0

def test_10_large_status(analyzer):
    assert analyzer.parse_line('127.0.0.1 - - [10/Oct/2000:13:55:36 -0700] "GET / HTTP/1.0" 999 0')["status"] == 999
