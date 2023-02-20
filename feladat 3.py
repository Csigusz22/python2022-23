
def ido2mp():


#1 feladat
eredmenyek=[]

f=open("trilatlon.txt")
for egySor in f:
    temp=egySor.replace("\n","").split(";")
    eredmenyek.append(temp)
    
f.close()

eredmenyek.pop(0)

#2feladat
print("2 feladat")
print("A versenyen [] versenyző indult.".format(len(eredmenyek)))

#3 feladat
print("3 feladat")
