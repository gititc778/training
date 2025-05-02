### 📦 Software Installation (Linux CLI)

```bash
sudo apt update
```
Update the package index (Debian/Ubuntu).

```bash
sudo apt upgrade
```
Upgrade all installed packages (Debian/Ubuntu).

```bash
sudo apt install <package>
```
Install a package (Debian/Ubuntu).

```bash
sudo apt remove <package>
```
Remove a package without deleting its configuration files (Debian/Ubuntu).

```bash
sudo apt purge <package>
```
Remove a package along with its configuration files (Debian/Ubuntu).

```bash
sudo apt autoremove
```
Remove unused packages (Debian/Ubuntu).

```bash
sudo yum install <package>
```
Install a package (RHEL/CentOS).

```bash
sudo yum remove <package>
```
Remove a package (RHEL/CentOS).

```bash
sudo dnf install <package>
```
Install a package using `dnf` (Fedora/RHEL 8+).

```bash
sudo dnf remove <package>
```
Remove a package using `dnf` (Fedora/RHEL 8+).

```bash
which <command>
```
Find the location of an installed command.

```bash
dpkg -l | grep <package>
```
Check if a package is installed (Debian/Ubuntu).

```bash
rpm -q <package>
```
Check if a package is installed (RHEL/CentOS/Fedora).
