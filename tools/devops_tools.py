def fetch_logs(service, window):
    with open("sample_logs.txt", "r") as f:
        
        return f.read()
def analyze_logs():
    return """
Analysis:
Payments service causing timeout.
Database latency increased.
"""
def lookup_runbook(query: str):

    if "timeout" in query.lower():
        return """
Restart payments service.
Check service health.
Monitor API latency.
"""

    return "No runbook found."