import subprocess
import platform
import re

def ping_host(host):
    # Determine the platform and set the ping command accordingly
    param = "-n" if platform.system().lower() == "windows" else "-c"
    count = "4"
    try:
        output = subprocess.check_output(
            ["ping", param, count, host],
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        avg = parse_average_ping(output)
        return avg
    except subprocess.CalledProcessError:
        return None

def parse_average_ping(output):
    # Parse output for average time
    if platform.system().lower() == "windows":
        # Example: Average = 24ms
        match = re.search(r"Average = (\d+)", output)
        if match:
            return float(match.group(1))
    else:
        # Example: rtt min/avg/max/mdev = 10.476/10.519/10.564/0.044 ms
        match = re.search(r"= [\d\.]+/([\d\.]+)/[\d\.]+/[\d\.]+ ms", output)
        if match:
            return float(match.group(1))
    return None

def main():
    hosts_file = "hosts.txt"
    try:
        with open(hosts_file, "r") as f:
            hosts = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"File {hosts_file} not found.")
        return

    print(f"Pinging {len(hosts)} hosts from {hosts_file}...\n")
    for host in hosts:
        print(f"Pinging {host}...", end=" ")
        avg_time = ping_host(host)
        if avg_time is not None:
            print(f"Average response time: {avg_time} ms")
        else:
            print("Failed to ping or parse response.")

if __name__ == "__main__":
    main()
