from random import *
with open("names.txt", "r") as f:
        word = list(map(str,f.read().split()))
        print(word)
        p = "".join(choice(word))
        print(p)
