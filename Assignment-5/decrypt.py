from pyfinite import ffield
import numpy as np

F = ffield.FField(7)

inp = open("parameters.txt", "r")

A = [[]]*8
E = []

for i, line in enumerate(inp.readlines()):
    if i == 8:
        E = [int(s) for s in line.split()]
        break
    A[i] = [int(s) for s in line.split()]


mat = np.matrix(A)
print(mat.T)


'''
for i in range(0,8):
    for j in range(0,8):
        print(A[i][j], end = " ")
    print()

print(E)
'''

print(A)
print(E)

def block_to_ele(s):
    return 16*(ord(s[0])-ord('f')) + 1*(ord(s[1])-ord('f'))

def block_to_byte(s):
    hex = []
    for i in range(0,len(s),2):
        hex.append(block_to_ele(s[i:i+2]))
    return hex

def byte_to_str(a):
    s = ""
    for x in a:
        #s = s + chr(x//16 + ord('f')) + chr(x%16 + ord('f'))
        s = s + chr(x)
    return s

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


#lhmlgplthujqlfjl fnisggfkkhmuliji
#ffffffffffffffff gggggggggggggggg

password_1 = "lhmlgplthujqlfjl"
password_2 = "fnisggfkkhmuliji"

pass_1 = block_to_byte(password_1)
pass_2 = block_to_byte(password_2)

print("\n\n")

print("Ciphertext Block 1 (\"lhmlgplthujqlfjl\") - ", pass_1)
print("Ciphertext Block 2 (\"fnisggfkkhmuliji\") - ", pass_2)

print("\n\n")

in_1 = [0 for i in range(0,8)]
in_2 = [0 for i in range(0,8)]

for ind in range(0,8):
    for i in range(1,128):
        in_1[ind] = i
        if pass_1[ind] == EAEAE(in_1, A, E)[ind]:
            break

for ind in range(0,8):
    for i in range(1,128):
        in_2[ind] = i
        if pass_2[ind] == EAEAE(in_2, A, E)[ind]:
            break

print("Plaintext Block 1 - ", in_1)
print("Plaintext Block 2 - ", in_2)

print("\n\n")
print(byte_to_str(in_1) + byte_to_str(in_2))




'''

[[84, 114, 17, 126, 98, 31, 2, 95], [0, 70, 16, 27, 38, 40, 121, 14], [0, 0, 43, 31, 12, 25, 11, 82], [0, 0, 0, 12, 117, 51, 105, 22], [0, 0, 0, 0, 112, 101, 1, 23], [0, 0, 0, 0, 0, 11, 83, 68], [0, 0, 0, 0, 0, 0, 27, 4], [0, 0, 0, 0, 0, 0, 0, 38]]
[20, 111, 36, 77, 87, 55, 23, 18]
[98, 118, 26, 110, 47, 75, 96, 70]
[8, 61, 17, 5, 82, 127, 99, 67]
[116, 112, 109, 115, 121, 98, 112, 111]
[97, 98, 48, 48, 48, 48, 48, 48]
mjmflsmimolhmflulglhifififififif
tpmsybpoab000000   ------>  tpmsybpoab  (zeroes for padding)


'''