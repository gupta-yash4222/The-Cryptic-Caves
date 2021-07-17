
def frequency(text):
    num = {}
    cnt = 0

    for s in text :
        if s<='z' and s>='a' :
            cnt += 1
            num.setdefault(ord(s)-97, 0)
            num[ord(s)-97] += 1

    #print([int(n) for n in list(num.keys())])

 #   for key in [int(n) for n in list(num.keys())] :
#        num[key] = (num[key]/cnt)*100    

    num = {chr(k+97): v for k, v in sorted(num.items(), key = lambda item: item[1], reverse = True)}

    ioc = 0
    for k, v in num.items():
        ioc += v*(v-1)
    
    print(ioc/(cnt*(cnt-1)))
  
    print(cnt)
    print(num)

def change(text, c1, c2):
    c2 = c2.upper()
    c1 = c1.lower()
    for i in range(len(text)):
        if text[i]==c1:
            text = text[:i] + c2  + text[i+1:]
        
    print(text) 
    return text
        
#text = "wsam ie pjo ysgtm eyipbya .P axg niphay y, mey syw ahgm ewhrg tw hmysyam wh meyiepjo ys .Ag jygtmeyk pmys ie pjo ysavw kkoyjgsy whmy sy amwh rmephmewagh y!Me yigu ynay utg smew ajya apr ywap awjfkya no a mwmnmw ghiwfeyswhve wieuwr wm aepby oyyhae wtmy uox8 fkpiya. Me y fpaavgs uwa mxSrN03u wd dvwmegnmmey dngmya. Mew awameyt "

text = 'TR XYCB MH AFC MUVY EOHPTCS, AFCSS TE QCSI NTYIMS TNA AFCSC. EMRBH XAA VAFR MIUCQPUH "LMRL_CCETOT" FN HM AKUXAHK. OTA WANA OTXT FFU EISCWNAF HME BFU MCVA UGTOTRE. BM HYLF IFU UVTY ANE HBSEI QYOQM OUVSF AM EAFTE PYHYS XNSKE IFUSC.'

print(text.find("IS"))

text = text.lower()

#To get the frequencies of the individual letters un-comment the line below
frequency(text)

#To substitute a letter by another letter. Enter a line in the formate - 
# change(text, c1, c2)     where c1 is the current letter and c2 is the letter with which you want to substitute c1. 
# text = change(text, 'm', 't' ) substitutes 't' in place of 'm' and in the changed text 't' appears in capitals. 



