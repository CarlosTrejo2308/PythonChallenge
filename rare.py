file = open("file2.txt", "r")

for line in file:
    for word in line.split():
        for char in word:
            if char.isalpha():
                print(char, end="")