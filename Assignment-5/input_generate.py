fo = open("input.txt", "w")
file = open("plaintxt.txt", "w")

for i in range(0,8):
    for j in range(0,128):
        s = "ff"*i + str(chr(ord('f') + j//16)) + str(chr(ord('f') + j%16)) + "ff"*(8-i-1)
        fo.write(s + " " + "c" + " ")
        file.write(s + " ")
    fo.write("\n")
    file.write("\n")

fo.write("back\nquit")