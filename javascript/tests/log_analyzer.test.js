const LogAnalyzer = require('../log_analyzer');

test('parseLine 200 statusunu tanımalıdır', () => {
    const analyzer = new LogAnalyzer();
    const line = '127.0.0.1 - - [10/Oct/2000:13:55:36 -0700] "GET /index.html HTTP/1.0" 200 2326';
    expect(analyzer.parseLine(line).status).toBe(200);
});

test('analyze metodu səhv faizini düzgün hesablamalıdır', () => {
    const analyzer = new LogAnalyzer();
    const lines = [
        'line... 200',
        'line... 404',
        'line... 500',
        'line... 200'
    ];
    const result = analyzer.analyze(lines);
    expect(result.total_requests).toBe(4);
    expect(result.error_rate).toBe(50);
});
