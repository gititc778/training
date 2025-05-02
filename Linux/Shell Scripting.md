### ⚙️ BASH Shell Scripting

```bash
#!/bin/bash
```
Shebang to define the interpreter (used at the top of shell scripts).

```bash
echo "Hello, World!"
```
Print text to the terminal.

```bash
VAR="Value"
echo $VAR
```
Set and use a variable.

```bash
read name
```
Read user input into a variable called name.

```bash
if [ "$name" == "Alice" ]; then
  echo "Hi Alice"
fi
```
Simple conditional statement.

```bash
for i in {1..5}; do
  echo "Number $i"
done
```
A basic for loop.

```bash
while [ $count -le 5 ]; do
  echo "Count is $count"
  ((count++))
done
```
A basic while loop.

```bash
function greet() {
  echo "Hello $1"
}
greet "Alice"
```
Define and call a function.

```bash
touch myscript.sh && chmod +x myscript.sh
```
Create a script file and make it executable.

```bash
./myscript.sh
```
Run an executable script in the current directory.










