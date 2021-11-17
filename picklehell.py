import pickle

with open(r"pickle.txt", "rb") as input_file:
    x = pickle.load(input_file)

print(type(x))

for lists in x:
    for tup in lists:
        print(tup[0]* tup[1], end="")
    print()
