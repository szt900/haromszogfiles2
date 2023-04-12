import math

def szogFok(sz,m1,m2):
    return math.degrees(math.acos((m1**2+m2**2-sz**2)/(2*m1*m2)))
#0
print("Háromszögek feldolgozása fájlokban.")

#1
finp = open("haromszogek.txt", mode="rt", encoding="utf-8")
szoveg = finp.read()
sorok = szoveg.split("\n")
finp.close()

#2
szogekLines = []
for item in sorok:
    if item != '':
        reszletek = item.split(';')
        a = float(reszletek[0].replace(',','.'))
        b = float(reszletek[1].replace(',','.'))
        c = float(reszletek[2].replace(',','.'))

        alfa = szogFok(a,b,c)
        betta = szogFok(b,a,c)
        gamma = szogFok(c,a,b)

        szogekSzovegesen = (str(alfa),str(betta),str(gamma))
        szogekSor = ';'.join(szogekSzovegesen)
        # szogekSor = f"{alfa.2f};{betta.2f};{gamma.2f}\n"
        szogekLines.append(szogekSor)



#3
fout = open("szogek.txt", mode="wt", encoding="utf-8")
fout.writelines(szogekLines)
#1. módszer
tartalom = "\n".join(szogekLines)
fout.write(tartalom)



fout.close()
