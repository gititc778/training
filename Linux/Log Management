### 📜 Log Management (Linux CLI)

```bash
tail /var/log/syslog
```
View the latest lines in the system log

```bash
tail -f /var/log/syslog
```
Follow new log entries in real-time.

```bash
tail -n 100 /var/log/syslog
```
Show the last 100 lines of a log file.

```bash
grep "error" /var/log/syslog
```
Search for lines containing "error" in the log.

```bash
journalctl
```
View logs managed by systemd journal.

```bash
journalctl -u <service>
```
View logs for a specific service.

```bash
journalctl -xe
```
Show detailed logs, often used after a service failure.

```bash
find /var/log -type f -name "*.log" -mtime +7
```
Find log files older than 7 days



