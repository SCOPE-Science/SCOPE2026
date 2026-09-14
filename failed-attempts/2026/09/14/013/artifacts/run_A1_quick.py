from cypari2 import Pari
pari = Pari()
pari.default("parisize", "4096M")
# Reduce the degree-6 compositum polynomial first
print(pari('P=polcompositum(x^2+1031, x^3-3*x+1)[1]; Q=polredabs(P); print(Q)'))
