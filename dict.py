#1
dict_mwen = {"nom":"Eustache","prenom":"Naphtala","niveau":"licence"}
vale=[]
kle=[]
for k ,v in dict_mwen .items():
    kle.append(k)
    vale.append(v)
print("vale yo nan diksyone a:",vale)
print("kle yo nan diksyone a:",kle)

#2
itlizate=input("antre yon  vale")
if itlizate .startswith("{") or itlizate.endswith(" }"):
    print("li gen akolad  ni devan ,ni deye")
else:
    print("li pa gen akolad")
    
#3
dictio={"nom":"Eustache","prenom":"Naphtala","niveau":"licence"}
for cle in dictio:
    print(cle)
    
 #4
diction={"nom":"Eustache","prenom":"Naphtala","niveau":"licence"}
for vale in diction.values():
    print(vale)
     
 #5 pou fe kopi diktionne a
dictione={"nom":"Eustache","prenom":"Naphtala","niveau":"licence"}
kopi_dictione=dict(dictione)
 
 #6
dik=   {"name":"Lub","age":"14","assets":"laptop"}
for valeur,cle in dik.items():
    if isinstance(cle,str):
        dik[valeur] = f"_{cle}_"
print(dik)

#7
nouvo_diksyone={}
diksyone={"a":"12","b":"abc","c":"12r","d":"90"}
nouvo_diksyone=dict(diksyone)
print(nouvo_diksyone)

#8
dic={"a":1,"b":"2"}
lis_tup=[(kle,vale) for kle , vale in dic.items()]
print(lis_tup)

#9
lis_tip=[("a","1"),("b","2")]
diks=dict(lis_tip)
print(diks)

# 10
dik1={"kle1":123,"kle2":"abc","kle3":[1,2,3]}
dik2={"kle1":123,"kle2":"def","kle4":[4,5,6]}
new_dik=dik1.copy()
new_dik.update((k,v)for k, v in dik2 .items() if isinstance(v,(int ,str, list , set )))
print(new_dik)
 
 
































     
    
    


































