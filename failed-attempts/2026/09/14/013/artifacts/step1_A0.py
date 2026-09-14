from cypari2 import Pari
pari = Pari()
pari.default("parisize", "1024M")
# Certified class group of K0 = Q(sqrt(-1031)), proof flag = 1
print(pari('bnfinit(x^2+1031,1)'))
