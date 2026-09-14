from cypari2 import Pari
pari = Pari()
pari.default("parisize", "2048M")
K0 = pari('bnfinit(x^2+1031,1)')
# components: K0[7] is class group? print vector entries
# bnf_get_cl = component 8? Let's just print bnfcl structure via bnfinit .no, .cyc, .gen
print("no =", pari('K0=bnfinit(x^2+1031,1); K0.no'))
print("cyc =", pari('K0=bnfinit(x^2+1031,1); K0.cyc'))
print("cert =", pari('bnfcertify(bnfinit(x^2+1031,1))'))
