import os
import re

# Regex pattern to capture timestamp, level, service, and message
LOG_PATTERN = re.compile(
    r"^(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})\|"
    r"(?P<level>[A-Z]+)\|"
    r"(?P<service>[^|]+)\|"
    r"(?P<message>.*)$"
)

def main():
    # 1. Locate log file using os.path relative to main.py
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(base_dir, "data", "gateway.log")
    report_dir = os.path.join(base_dir, "reports")
    report_path = os.path.join(report_dir, "log_summary.txt")

    # 2. Validate input (exists and is a file)
    if not os.path.exists(log_path) or not os.path.isfile(log_path):
        print(f"Error: Log file not found at {log_path}")
        return

    # 3. Check file size
    if os.path.getsize(log_path) == 0:
        print(f"Empty log detected with path {log_path}.")
        return

    # 4. Read contents (use 'r' mode, NOT 'w')
    with open(log_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Tracking variables
    valid_count = 0
    malformed_count = 0
    level_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    unique_services = set()

    # 5, 6, 7, 8. Parse entries, count severity, track unique services, handle malformed lines
    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            continue  # Skip empty whitespace lines

        match = LOG_PATTERN.match(line)
        if match:
            valid_count += 1
            data = match.groupdict()

            level = data["level"]
            if level in level_counts:
                level_counts[level] += 1

            unique_services.add(data["service"])
        else:
            malformed_count += 1

    # 9. Generate report
    os.makedirs(report_dir, exist_ok=True)

    services_block = "\n".join(unique_services)
    report_content = (
        "APPLICATION LOG REPORT\n"
        "-----------------------------\n\n"
        f"Total valid entries: {valid_count}\n"
        f"Malformed entries: {malformed_count}\n\n"
        "LOG LEVEL SUMMARY:\n"
        f"INFO: {level_counts['INFO']}\n"
        f"WARNING: {level_counts['WARNING']}\n"
        f"ERROR: {level_counts['ERROR']}\n\n"
        "UNIQUE SERVICES:\n"
        f"{services_block}\n\n"
        f"Total unique services: {len(unique_services)}\n"
    )

    with open(report_path, "w", encoding="utf-8") as report_file:
        report_file.write(report_content)

    print(f"Report generated successfully at {report_path}")

if __name__ == "__main__":
    main()
