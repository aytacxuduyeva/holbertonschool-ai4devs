import json

class LogAnalyzer:
    def parse_line(self, line: str) -> dict:
        """Apache log sətrini parse edir. Xarab sətirlər üçün None qaytarır."""
        try:
            parts = line.split()
            if len(parts) < 9:
                return None
            
            # Status kodu adətən 9-cu elementdir (index 8)
            return {
                "ip": parts[0],
                "status": int(parts[8])
            }
        except (ValueError, IndexError):
            return None

    def analyze(self, lines: list) -> dict:
        """Log siyahısını analiz edir və statistikaları JSON formatında qaytarır."""
        total_requests = 0
        errors = 0
        unique_visitors = set()

        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            data = self.parse_line(line)
            if data:
                total_requests += 1
                unique_visitors.add(data["ip"])
                if data["status"] >= 400:
                    errors += 1
        
        # Division by zero-nun qarşısını almaq (Edge Case)
        error_rate = 0.0
        if total_requests > 0:
            error_rate = (errors / total_requests) * 100

        return {
            "total_requests": total_requests,
            "unique_visitors": len(unique_visitors),
            "error_rate": f"{error_rate:.1f}%",
            "status": "success"
        }

if __name__ == "__main__":
    # Sadə test nümunəsi
    analyzer = LogAnalyzer()
    sample_logs = [
        '192.168.1.1 - - [08/May/2026:10:00:01] "GET /home" 200 512',
        '192.168.1.2 - - [08/May/2026:10:00:02] "POST /login" 404 256',
        'invalid log line example',
        '192.168.1.1 - - [08/May/2026:10:00:03] "GET /api" 500 128'
    ]
    print(json.dumps(analyzer.analyze(sample_logs), indent=4))
