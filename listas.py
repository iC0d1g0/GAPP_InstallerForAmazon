
import string

alfabeto = string.ascii_lowercase

entrada = "Holaaaaa"


letrasrepetidas=[]
dicionario={}

for i in entrada:
    
    if i != " ": 
        if i in dicionario:
            dicionario[i]+=1
        
    else: 
        dicionario[i]=1
    for j in dicionario:
        if j > 1: 
            letrasrepetidas.append(dicionario["repetida{i}"+ j])

print("letras: ", letrasrepetidas)


