from cypari2 import Pari
pari = Pari()
pari.default("parisize", "4096M")
# A0 = Q(sqrt(-1031)), certified
K0 = pari('K0=bnfinit(x^2+1031,1)')
print("A0: no =", pari('K0.no'), " cyc =", pari('K0.cyc'), " cert =", pari('bnfcertify(K0)'))
# A1 = K0 * Q1, Q1 = cubic subfield of Q(zeta_9), minpoly x^3-3*x+1
Q1red = 'x^6 - 3*x^5 + 771*x^4 - 1535*x^3 + 200463*x^2 - 201249*x + 17575221'
K1 = pari(f'K1=bnfinit({Q1red},1)')
print("A1: no =", pari('K1.no'), " cyc =", pari('K1.cyc'), " cert =", pari('bnfcertify(K1)'))
