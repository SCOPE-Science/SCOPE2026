from cypari2 import Pari
pari = Pari()
pari.default("parisize", "1024M")
print("kronecker(-1031,3) =", pari('kronecker(-1031,3)'))  # 1 => splits
print("factor(1031) =", pari('factor(1031)'))
print("Q1 minpoly disc:", pari('poldisc(x^3-3*x+1)'))
print("Q1 class no:", pari('(bnfinit(x^3-3*x+1,1)).no'), "cert:", pari('bnfcertify(bnfinit(x^3-3*x+1,1))'))
print("factor(2625) =", pari('factor(2625)'))
print("factor(35) =", pari('factor(35)'))
# ramification: primes above 3 in K1
print("idealprimedec K1 above 3:", pari('idealprimedec(nfinit(x^2+1031),3)'))
