import re

file = open("file2.txt", "r")
for line in file:
    match =  re.search("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", line)
    if match:
        print(match.group(1), end="")
        
        
file.close()
