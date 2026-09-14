from cypari2 import Pari
pari = Pari()
pari.default("parisize", "4096M")
pari.default("nbthreads", "4")
Q = 'x^6 - 3*x^5 + 771*x^4 - 1535*x^3 + 200463*x^2 - 201249*x + 17575221'
print("bnfinit starting...")
K1 = pari(f'bnfinit({Q},1)')
print("no =", pari(f'(bnfinit({Q},1)).no'))
print("cyc =", pari(f'(bnfinit({Q},1)).cyc'))
print("cert =", pari(f'bnfcertify(bnfinit({Q},1))'))
