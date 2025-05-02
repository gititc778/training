### 📁 File and Directory Management (Linux CLI)

- `ls`  
  List files and directories in the current location.

- `ls -l`  
  List with detailed info (permissions, size, date, etc.).

- `cd <directory>`  
  Change into a directory.

- `cd ..`  
  Move one level up in the directory tree.

- `pwd`  
  Print the current working directory.

- `mkdir <dir_name>`  
  Create a new directory.

- `mkdir -p dir1/dir2`  
  Create nested directories in one go.

- `touch <file_name>`  
  Create an empty file or update the timestamp of an existing one.

- `cp <src> <dest>`  
  Copy a file or directory.

- `cp -r <src_dir> <dest_dir>`  
  Recursively copy a directory.

- `mv <old_name> <new_name>`  
  Rename or move a file or directory.

- `rm <file>`  
  Delete a file.

- `rm -r <dir>`  
  Recursively delete a directory and its contents.

- `rm -rf <dir>`  
  Forcefully delete a directory and its contents **(use with caution!).**

- `find . -name "*.log"`  
  Search for files matching a pattern (e.g., all `.log` files) from the current directory.

- `tree`  
  Display directory structure in tree format *(requires `tree` package).*
