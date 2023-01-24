import random

def szoBeker():
    szo=input("Kérek egy szót: ")
    if szo=="":
        jelentes=""
    else:
        jelentes=input(szo+ " jelentése: ")

    return [szo,jelentes]

szavak=[]
def sokBeker():
    szo=szoBeker()
    while szo[0]!="":
        szavak.append(szo)
        szo=szoBeker()
    return szavak
    
def filebaIr(lista):
    f=open("szotar.txt","a")

    for e in lista:
        #print(e)
        f.write(" ".join(e))
        f.write("\n")
    f.close()

kerdesek=[]
def beolvas():
    f=open("szotar.txt","r")
    for sor in f:
        kerdesek.append(sor.replace("\n","").split(" "))

    f.close()
    
def kerdez():
    #jó válasz
    valasztott=random.choice(kerdesek)
    #print("valasztott", valasztott)
    #rossz válaszok, 3db
    rossz=[]
    for i in range(3):
        #temp="alma"
        temp=random.choice(kerdesek)
        #print("temp"temp)
       
        while not(temp not in rossz and temp!=valasztott):
            temp=random.choice(kerdesek)

        rossz.append(temp)
        #print("rossz"rossz)

    print("-"*40)
    print("Mit jelenet:"+ valasztott[0]+"?")

    rossz.append(valasztott)
    print(rossz)
    
    #válasz bekérés
    abc="abcdefghijklmnopqrstuxyvwz"
    random.shuffle(rossz)

    i=0
    for e in rossz:
        print(abc[i]+": "+e[1])
        i+=1

    valasz=input("válasz: ")
    hol=abc.index(valasz)
    print(hol)
    while hol<4:
        try:
        valasz=input("Válasz újra: ")
       hol=abc.index(valasz)
       except (e):
           pass

       
        



















        
                     


        
