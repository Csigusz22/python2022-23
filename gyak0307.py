def oszlopVissza(hanyadik):
    oszlop=[]
    for e in tabla:
        oszlop.append(e[hanyadik-1])

    return oszlop:

def t(hanyadik):
    oszlop=[e[hanyadik-1::hanyadik]for e in tabla]
    return oszlop:



    
gyumolcsok=["alma","szőlő","banán","körte","epere"]

print("Ennyi gyümölcs van: []".format(len(gyumolcsok)))

print(gyumolcsok[3])
#gyumolcsok[3]+="k"
#gyumolcsok[3]+="körtek"

print(gyumolcsok.index("körte"))
#gyumolcsok[gyumolcsok.index("körtek")]+="k"
index=gyumolcsok.index("körte")
gyumolcsok[index]+="k"

print(gyumolcsok[3])

print("Rövid gyümölcsök")
#for i in range(len(gyumolcsok)):
#    if len(gyumolcsok[i])<5:
#    print(gyumolcsok)

rovid=[]
for i in range(len(gyumolcsok)):
    if len(gyumolcsok[i])<5:
        rovid.append(gyumolcsok[i])

print(rovid)

rovid=[]
for e in gyumolcsok:
    if len(e)<5:
        rovid.append(e)
print(rovid)


rovid=[e for e in gyumolcsok if len(e)<5]
print(rovid)

rovid=[]
i=0
while i<len(gyumolcsok):
    if len(gyumolcsok[i])<5:
        rovid.append(gyumolcsok[i])
    i+=1
print(rovid)

rovid=[]
i=0
while True:
    if len(gyumolcsok[i])<5:
        rovid.append(gyumolcsok[i])
    if len(gyomolcsok)-1==i:
        break

print(gyumolcsok[:2])

print(gyumolcsok[-2:])
print(gyumolcsok[len(gyumolcsok)-2:])

print(gyummolcsok[1:-1])

paratlan=gyumolcsok[1::2]
print(paratlan)


paros=gyumolcsok[::2]
print(paros)

masolat=gyumolcsok
print(masolat)
masolat.reverse()
print(", ".join(masolat))

print(", ".join(gyumolcsok[::]))

tabla=[]
for i in range(20):
    sor=[]
    for k i range(10):
        sor.append(i+1)*(k+1))
        tabla.append(sor)

print(tabla)

oszlop=[]
for e in tabla:
    oszlop.append(e[0])

print(oszlop)
print(oszlopVissza(5))
print(oszlopVissza(10))


oszlop=[e[3:]for e in tabla]
oszlop=[e[4:7]for e in tabla]
oszlop=[e[1:2:]for e in tabla]
oszlop=[e[3:4]for e in tabla]
print(oszlop)

#függvény oszlop/osztás menyisége
print(oszlop)

#print(oszlopVissza2(int(input("Kérek egy számot."))))

oszlop=[(e[2],e[6],e[0])for e in tabla]

print(oszlop)









