from cypari2 import Pari
pari = Pari()
pari.default("parisize", "1024M")
# (a) LTE input: v_3(1031^6 - 1) should be 1 => order lifts by exactly 3 each level
print("v3(1031^6-1) =", pari('valuation(1031^6-1,3)'))
print("1031 mod 9 =", pari('lift(Mod(1031,9))'))
print("ord mod 9 =", pari('znorder(Mod(1031,9))'))
print("ord mod 27 =", pari('znorder(Mod(1031,27))'))
print("ord mod 81 =", pari('znorder(Mod(1031,81))'))
print("ord mod 243 =", pari('znorder(Mod(1031,243))'))
# (b) discriminant of K1: only ramified prime should be 1031
print("nfdisc(x^2+1031) =", pari('nfdisc(x^2+1031)'))
print("factor disc =", pari('factor(abs(nfdisc(x^2+1031)))'))
# (c) delta inputs: zeta_3 not in K1 (disc check: K1(ζ3) degree 4)
print("poldegree compositum K1,Q(mu3) =", pari('poldegree(polcompositum(x^2+1031,x^2+x+1)[1])'))
# (d) splitting of 3 in K1 (should split: 2 primes)
print("primes above 3 in K1:", len(list(pari('idealprimedec(nfinit(x^2+1031),3)'))))
# (e) splitting of 1031 in Q1 (first layer of Qinf): should stay prime (inert), 1 prime
print("primes above 1031 in Q1:", pari('idealprimedec(nfinit(x^3-3*x+1),1031)'))
# (f) Q1 class number (lambda(Qinf)=0 input at layer 1)
print("Q1 class no:", pari('(bnfinit(x^3-3*x+1,1)).no'))
