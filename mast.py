  #chenn karactere 
chenn=("SPREAD YOUR WINGS NOTHINGS IS IMPOSSIBLE BELIEVE")
chenn=chenn.lower()
print(chenn)

# 2 karakte 
karakte="ayibobo ayiti"
eleman=karakte.split()
print(eleman)

#3
let="l'art est de savoir ,faire savoir et de savoir-faire"
lett=let.title()
print(lett)

#4
intial="l'art est de savoir ,faire savoir et de savoir-faire"
karak=intial.split()
initial=[karak[0] for karak in karak]
nouvo_initial="".join(initial)
print(nouvo_initial)

#5
a="l'art est de savoir ,faire savoir et de savoir-faire"
b=a.replace("a","@")
print(b)

#6
mo="ayiti"
mo=mo[::-1]
inverse=mo.upper()
print(inverse)

#7
c="Ayiti kapab avanse"
d=c.find("a")
print(d)

#8
e="Ayiti kapab avanse"
f=0
for i ,j in enumerate(e):
   if j == "a"or j=="A":
      f+=i
print(f)

#9

endesk_lis={}
h="Ayiti kapab avanse"
for endeks , let in enumerate(h):
  if h.count(let)>1 and let not in endesk_lis:
    endesk_lis[let]=[i for i ,a in enumerate(h) if a==let]
print(endesk_lis)







#10
ak_espas="l'art est de savoir ,faire savoir et de savoir-faire"
san_espas=ak_espas.replace(" ","")
kantite=len(san_espas)
print(san_espas,"****",kantite)
      

      
