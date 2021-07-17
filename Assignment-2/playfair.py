def matrix(key):
    num = {}
    mat = []
    flag = 0
    lst=[]
    i, j, k = 0, 0, 0
    while i<25:
        if j>=len(key):
            flag=1
        if flag==0:
            while key[j] in num.keys():
                j+=1
            if j<len(key):
                num.setdefault(key[j],i)
                lst.append(key[j])
                j += 1
        else:
            while chr(97+k) in num.keys() or chr(97+k)=='j':
                k+=1
            if k<26:
                num.setdefault(chr(97+k),i)
                lst.append(chr(97+k))
                k+=1
        i+=1
        if i%5==0:
            mat.append(lst)
            lst = []
    print(mat)
    print(num)
    return mat, num


def playfair(double, key):
    mat, num = matrix(key)
    plain = []
    dbl = ""
    
    for s in double:
        if num[s[0]]%5 == num[s[1]]%5:
            i, j = (num[s[0]]+20)%25, (num[s[1]]+20)%25
            plain.append(mat[i//5][i%5] + mat[j//5][j%5])
        elif num[s[0]]//5 == num[s[1]]//5:
            i, j = (num[s[0]]+4)%5 + 5*(num[s[0]]//5), (num[s[1]]+4)%5 + 5*(num[s[0]]//5)
            plain.append(mat[i//5][i%5] + mat[j//5][j%5])
        else:
            i, j = num[s[1]]%5, num[s[0]]%5
            plain.append(mat[num[s[0]]//5][i] + mat[num[s[1]]//5][j])
    
    print("".join(plain).upper())
    return plain


#text = "gn"
text = 'TR XYCB MH AFC MUVY EOHPTCS, AFCSS TE QCSI NTYIMS TNA AFCSC. EMRBH XAA VAFR MIUCQPUH "LMRL_CCETOT" FN HM AKUXAHK. OTA WANA OTXT FFU EISCWNAF HME BFU MCVA UGTOTRE. BM HYLF IFU UVTY ANE HBSEI QYOQM OUVSF AM EAFTE PYHYS XNSKE IFUSC.'
text = text.lower()

double = []
s = ""
cnt = 0
i=0

while i<len(text):
    if cnt==0:
        #s = ""
        if text[i]<='z' and text[i]>='a':
            s = s+text[i]
            cnt += 1
    elif cnt==1:
        if text[i]<='z' and text[i]>='a':
            if text[i] == s[0]:
                s = s + "x"
                i -= 1
                print(text[i])
            else:
                s = s+text[i]
            double.append(s)
            s = ""
            cnt = 0
    i += 1

if len(s)!=0: 
    s = s + "x"
    double.append(s)

print(double)
key = "security"
#key = input("Enter the key for the Cipher - ")
plain = playfair(double, key)

s = ""
i=0
cnt=0

'''
while i<len(text):
    if cnt==0:
        #s = ""
        if text[i]<='z' and text[i]>='a':
            s = s+text[i]
            cnt += 1
    elif cnt==1:
        if text[i]<='z' and text[i]>='a':
            if text[i] == s[0]:
                s = s + "x"
                i -= 1
                print(text[i])
            else:
                s = s+text[i]
            double.append(s)
            s = ""
            cnt = 0
    i += 1
'''