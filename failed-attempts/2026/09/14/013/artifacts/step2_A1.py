from cypari2 import Pari
pari = Pari()
pari.default("parisize", "2048M")
print(pari('Q1 = x^3-3*x+1; polcompositum(x^2+1031, Q1)'))
