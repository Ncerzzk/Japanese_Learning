import random
row = ["a", "i", "u", "ei", "o"]
col = ["", "k", "s", "t", "n", "h", "m"]

while(True):
    x = input()
    if(x != "q"):
        row_rand = random.randint(0, len(row)-1)
        col_rand = random.randint(0, len(col)-1)
        print(col[col_rand]+row[row_rand])
    else:
        break
