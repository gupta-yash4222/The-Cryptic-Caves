fi = open("output.txt", "r")
fo = open("ciphertxt.txt", "w")

count = 0

for line in fi:
    for word in line.split():
        if(len(word)==16 and word != "transformations:"):
            fo.write(word + " ")
            count = count + 1
            if count%128 == 0:
                count = 0
                fo.write("\n")