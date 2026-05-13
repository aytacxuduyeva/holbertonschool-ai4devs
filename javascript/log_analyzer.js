class LogAnalyzer {
    parseLine(line) {
        const parts = line.split(" ");
        return { status: parseInt(parts[8]) };
    }

    analyze(lines) {
        const total = lines.length;
        const errors = lines.filter(line => this.parseLine(line).status >= 400).length;
        return {
            total_requests: total,
            error_rate: total === 0 ? 0 : (errors / total) * 100
        };
    }
}

module.exports = LogAnalyzer;
