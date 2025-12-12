# ====== Running External Commands ======
import subprocess

# Simple run (no output capture)
subprocess.run(['ls', '-la'])

# Capture output
result = subprocess.run(['hostname'], capture_output=True, text=True)
output = result.stdout.strip()  # .strip() removes newlines

# Redirect to file
with open('log.txt', 'a') as f:  # 'a' = append, 'w' = overwrite
    subprocess.run(['rsync', '-av', 'src/', 'dest/'], 
                   stdout=f, stderr=f)

# Check if command succeeded
result = subprocess.run(['some_cmd'], capture_output=True)
if result.returncode == 0:
    print("success")

# ====== File Operations ======
import os

# Make directories (like mkdir -p)
os.makedirs("/path/to/dir", exist_ok=True)

# Check if stuff exists
os.path.exists("/some/path")  # file or dir
os.path.isfile("/some/file")
os.path.isdir("/some/dir")

# Read entire file
with open('file.txt', 'r') as f:
    content = f.read()  # whole file as string
    # or
    lines = f.readlines()  # list of lines

# Write to file
with open('file.txt', 'w') as f:  # 'w' overwrites
    f.write("stuff\n")
    f.write(f"variable: {var}\n")  # f-strings work

# Append to file
with open('file.txt', 'a') as f:
    f.write("more stuff\n")

# Get last N lines (like tail)
with open('file.txt', 'r') as f:
    lines = f.readlines()
    last_10 = lines[-10:]  # list slicing

# ====== Date/Time ======
from datetime import datetime

now = datetime.now()
timestamp = now.strftime('%Y-%m-%d %H:%M:%S')  # custom format
# or
timestamp = now.strftime('%c')  # locale's date/time (like bash date)

# ====== String Stuff ======
s = "  hello  \n"
s.strip()  # removes whitespace/newlines from ends
s.split()  # splits on whitespace into list
''.join(list_of_strings)  # combines list into single string

# f-strings for variables
name = "grant"
msg = f"hello {name}"  # easier than concatenation

# ====== Path Joining ======
import os.path

path = os.path.join('/home', 'student', 'file.txt')
# handles slashes correctly, better than string concat

# ====== Common rsync flags ======
# -a = archive mode (recursive, preserves permissions/times/etc)
# -v = verbose
# --delete = delete files in dest that dont exist in src
# remember trailing slashes matter: 'src/' vs 'src'