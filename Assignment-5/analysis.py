from pyfinite import ffield

F = ffield.FField(7)

inp = open("plaintxt.txt", "r")
out = open("ciphertxt.txt", "r")
fo = open("parameters.txt", "w")

def block_to_ele(s):
    return 16*(ord(s[0])-ord('f')) + 1*(ord(s[1])-ord('f'))

def block_to_byte(s):
    hex = []
    for i in range(0,len(s),2):
        hex.append(block_to_ele(s[i:i+2]))
    return hex

def Mult(a, b):
    return F.Multiply(a, b)

def Add(a, b):
    return int(a)^int(b)

def Exp(a, y):
    x = 1
    while y>0:
        if y&1:
            x = Mult(x, a)
        a = Mult(a, a)
        y = y//2
    
    return x


def LinearTransform(A, x):
    y = []
    for i in range(0,8):
        num = 0
        for j in range(0,8):
            num = Add(num, Mult(x[j], A[j][i]))
        y.append(num)
    return y

def EAEAE(pla, A, E):
    cip = [Exp(pla[i], E[i]) for i in range(0,8)]
    cip = LinearTransform(A, cip)
    for i in range(0,8):
        cip[i] = Exp(cip[i], E[i])
    cip = LinearTransform(A, cip)
    for i in range(0,8):
        cip[i] = Exp(cip[i], E[i])
    
    return cip

    



in_bin, out_bin = [], [] 
count = 0

for line in inp:
    for word in line.split():
        in_bin.append(block_to_ele(word[count:count+2]))
    break

count = 0

for line in out:
    lst = []
    for word in line.split():
        lst.append(block_to_ele(word[count:count+2]))
    count = count + 2
    out_bin.append(lst)

#print(in_bin)
#print(out_bin)

corr_aii = [[[] for i in range(8)] for i in range(8)]
corr_ei = [[] for i in range(8)]

for ind in range(0,8):
    for i in range(1,127):
        for j in range(1,128):
            flag = True
            for cip, pla in  zip(out_bin[ind], in_bin):
                #print("(", cip, pla, ")", end = " ")
            
                if cip != Exp(Mult(Exp(Mult(Exp(pla,i),j),i),j),i):
                    flag = False
                    break

            if flag == True:
                corr_aii[ind][ind].append(j)
                corr_ei[ind].append(i)
            
            #print("\n")
            #break
        #break
    
print(corr_aii)
print("\n------------------------\n")
print(corr_ei)
print("\n------------------------\n")
print("\n------------------------\n")

print("Block No. (i)        Possible (a_ii, e_i)")
print("-------------        ------------------------------------------")

for bl, (Aii, Ei) in enumerate(zip(corr_aii, corr_ei)):
    print(bl+1, end = "                    ")
    for aii, ei in zip(Aii[bl], Ei):
        print("(" + str(aii) + ", " + str(ei) + ")", end = "   ")
    print()

print("\n\n")


cnt=0

inp = open("plaintxt.txt", "r")
out = open("ciphertxt.txt", "r")

for ind, (inline, outline) in enumerate(zip(inp.readlines(), out.readlines())):
    #cnt = cnt + 1
    if ind==7:
        #print("hihi\n")
        break
    instr, outstr = [], []

    for s in inline.split():
        #print(s[ind:ind+2], end = " ")
        instr.append(block_to_ele(s[2*ind:2*ind+2]))
    #print("\n")
    for s in outline.split():
        #print(s[ind+2:ind+4], end = " ")
        outstr.append(block_to_ele(s[2*ind+2:2*ind+4]))
    #print("\n\n")
    
    for i in range(1,128):
        for e1, a1 in zip(corr_ei[ind], corr_aii[ind][ind]):
            for e2, a2 in zip(corr_ei[ind+1], corr_aii[ind+1][ind+1]):
                flag = True
                for cip, pla in zip(outstr, instr):
                    if cip != Exp(Add(Mult(Exp(Mult(Exp(pla, e1), a1), e1), i), Mult(Exp(Mult(Exp(pla, e1), i), e2), a2)), e2):
                        flag = False
                        break
                if flag == True:
                    corr_ei[ind] = [e1]
                    corr_ei[ind+1] = [e2]
                    corr_aii[ind][ind] = [a1]
                    corr_aii[ind+1][ind+1] = [a2]
                    corr_aii[ind][ind+1] = [i]

#print(cnt, "\n")
print(corr_ei)
print("\n------------------------\n")
print(corr_aii)
print("\n------------------------\n")
print("\n------------------------\n")



#print(Exp(3,3))



for p in range(0,6):
    ptr = p + 2
    inp = open("plaintxt.txt", "r")
    out = open("ciphertxt.txt", "r")

    E = [e[0] for e in corr_ei]
    A = [[0 for j in range(0,8)] for i in range(0,8)]

    for i in range(0,8):
        for j in range(0,8):
            if len(corr_aii[i][j])==0:
                A[i][j] = 0
            else:
                A[i][j] = corr_aii[i][j][0]
    
    for ind, (inline, outline) in enumerate(zip(inp.readlines(), out.readlines())):
        if ptr + ind > 7:
            continue
        instr = [block_to_byte(s) for s in inline.split()]
        outstr = [block_to_byte(s) for s in outline.split()]

        for i in range(1,128):
            flag = True
            A[ind][ind+ptr] = i
            for cip, pla in zip(outstr, instr):
                if cip[ind+ptr] != EAEAE(pla, A, E)[ind+ptr]:
                    flag = False
                    break

            if flag == True:
                corr_aii[ind][ind+ptr] = [i]
    
    inp.close()
    out.close()

print(corr_aii)
print("\n----------------------------------\n")
print(corr_ei)
print()

A = [[None]*8]*8
E = [e[0] for e  in corr_ei]

for i in range(0,8):
    for j in range(0,8):
        if len(corr_aii[i][j])==0:
            A[i][j] = 0
            fo.write(str(0) + " ")
        else:
            A[i][j] = corr_aii[i][j][0]
            fo.write(str(A[i][j]) + " ")
    fo.write("\n")

for i in range(0,8):
    fo.write(str(E[i]) + " ")
fo.write("\n")


