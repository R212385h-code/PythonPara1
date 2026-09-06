```python
from datetime import datetime

def find_peak_usage(logs):
    hours = [0] * 24

    for log in logs:
        time = datetime.fromisoformat(log)
        hours[time.hour] += 1

    highest = max(hours)
    return hours.index(highest)


logs = [
    "2026-08-04T13:21:18",
    "2026-08-04T14:10:05",
    "2026-08-04T13:45:30",
    "2026-08-04T13:50:12",
    "2026-08-04T14:25:40"
]

print(find_peak_usage(logs))

