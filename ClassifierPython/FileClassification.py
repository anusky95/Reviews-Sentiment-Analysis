f = open("posneg3.txt", "r")
g = open("negativeReviews3.txt", "w")
h = open("positiveReviews3.txt", "w")
for line in f:
    if line.strip():
        if not line.lstrip().startswith('"'):
            h.write(line)
        if line.lstrip().startswith('"'):
            g.write(line)
f.close()
g.close()
h.close()