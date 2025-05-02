### 📁 File and Directory Management (Linux CLI)

```bash
ls
```
List files and directories in the current location.

```bash
ls -l
```
List with detailed info (permissions, size, date, etc.).

```bash
cd <directory>
```
Change into a directory.

```bash
cd ..
```
Move one level up in the directory tree.

```bash
pwd
```
Print the current working directory.

```bash
mkdir <dir_name>
```
Create a new directory.

```bash
mkdir -p dir1/dir2
```
Create nested directories in one go.

```bash
touch <file_name>
```
Create an empty file or update the timestamp of an existing one.

```bash
cp <src> <dest>
```
Copy a file or directory.

```bash
cp -r <src_dir> <dest_dir>
```
Recursively copy a directory.

```bash
mv <old_name> <new_name>
```
Rename or move a file or directory.

```bash
rm <file>
```
Delete a file.

```bash
rm -r <dir>
```
Recursively delete a directory and its contents.

```bash
rm -rf <dir>
```
Forcefully delete a directory and its contents (use with caution!).

```bash
find . -name "*.log"
```
Search for files matching a pattern (e.g., all `.log` files) from the current directory.

```bash
tree
```
Display directory structure in tree format (requires `tree` package).
