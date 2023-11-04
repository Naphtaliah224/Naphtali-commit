#1
n=20
list= [ x for x in range(n+1) if x%2 ==0]
print(list)

#2
list_entier=[3,4,5,6,7,8,9]
chenn=[str(i) for i in list_entier]
print(chenn)

#3
karak=["m","a","m","a"]
karak=[mo.upper() for mo in karak ]
print(karak)

#4k
nouvo_divizib= []
list_diviz=[1,4,36,13,33,99,12,43,56,78,98,56,11,55]
nouvo_divizib=[u for u in list_diviz if u %3 ==0]
print(nouvo_divizib)

#5
list_elem=[1,2,3,4,5,6,7,8,9]
nouvo_elem=[tuple(list_elem[i:i+3]) for  i in range (0,len(list_elem),3)]
print(nouvo_elem)

#6
nouvo_doublon=[]
ansyen_doublon=[1,1,2,3,4,4,5,6,7,7,8,8,9,9,0,0,]
for k in ansyen_doublon:
    if k not in  nouvo_doublon:
        nouvo_doublon.append(k)
print(nouvo_doublon)

#7
liat3=[]
list1=[1,2,5,7,8,9,5]
list2=[1,4,6,2,9,0]
liat3=[k for k in list1 if k in list2]
print(liat3)

#8
liat3=[]
list1=[1,2,5,7,8,9,5]
list2=[1,4,6,2,9,0]
liat3=[k for k in list1 if k  not in  list2]
print(liat3)


#9
dictinnaire={'nom':'eustache','prenom':'naphtala'}
dic_kle_={'nom','prenom'}

#10
liat4=[]
li1=[1,2,4,8,9,0]
li2=[ 4,6,7,8,0]
li3=[1,2,3,4,5,6,7,8,9,0]
for o in [li1,li2,li3]:
    for p in o:
        if p not in liat4:
            liat4.append(p)
print(liat4)
