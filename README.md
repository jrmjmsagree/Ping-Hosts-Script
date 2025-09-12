# Ping Hosts Script

This Python script reads a list of hosts from a file and pings each host, reporting the average response time for each.

## Features

- Pings multiple hosts listed in a file
- Displays the average response time for each host
- Works on Windows, Linux, and macOS

## Usage

1. **Prepare the hosts file:**

   Create a file named `hosts.txt` in the same directory. List one host per line. Example:

   ```
   google.com
   8.8.8.8
   github.com
   ```

2. **Run the script:**

   ```bash
   python ping_hosts.py
   ```

3. **View Results:**

   The script will output the average response time for each host, or notify you if a ping fails.

## Requirements

- Python 3.x

## Notes

- On some systems, running the script may require administrator privileges to send ICMP packets.
- The script uses the system's `ping` command and parses its output, so it should work on major operating systems.

## License

MIT
