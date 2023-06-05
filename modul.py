import modul
sorok=[]
f=open("modul.py")

for e in f:
    sorok.append(e.replace("\"", "").strip())
    
f.close
print(sorok)       
sorok=sorok([0].strip(", ")

szavak=[]
for e in sorok:
            szavak.append(modul.szo(e))

rejtett=random.choice(szavak)
print(rejtett.szo)

tippek=[]
while True:
    be=input("Kérek a tippet: ")
    tippek.append(be)

    if be == "stop":
        break

    vissza=rejtet.minta(be)

            
    trint(="Az  eredmény: {}".format(visssza))
    if vissza==be:
        break

