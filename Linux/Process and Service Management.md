### ⚙️ Process and Service Management (Linux CLI)

```bash
ps aux
```
Show all running processes with detailed information.

```bash
top
```
Display real-time system resource usage.

```bash
kill <PID>
```
Terminate a process by its Process ID.

```bash
kill -9 <PID>
```
Forcefully terminate a process.

```bash
pkill <process_name>
```
Kill a process by name.


```bash
systemctl status <service>
```
Show the status of a service.

```bash
systemctl start <service>
```
Start a service.

```bash
systemctl stop <service>
```
Stop a service.

```bash
systemctl restart <service>
```
Restart a service.

```bash
systemctl enable <service>
```
Enable a service to start on boot.

```bash
systemctl disable <service>
```
Disable a service from starting on boot.

```bash
systemctl list-units --type=service
```
List all active services.
